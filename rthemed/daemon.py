import rthemed
import rthemelib
from gi.repository import Gio
from gi.repository import GLib
from pydbus import SessionBus

gnome_interface = Gio.Settings.new("org.gnome.desktop.interface")
gnome_a11y = Gio.Settings.new("org.gnome.desktop.a11y.interface")
rtheme_settings = Gio.Settings.new("io.risi.rtheme")
session_bus = SessionBus()


class Daemon:
    def __init__(self):
        self.logger = rthemed.Logger()
        rthemelib.logger = self.logger

        self.logger.log("silently applied theme.")
        self.application = DaemonApplication(self)
        self.application.refresh_theme(notification=False)
        self.application.run()

    def handle_error(self, error):
        self.send_notification("error", error)
        self.logger.log(error)


class DaemonApplication(Gio.Application):
    def __init__(self, daemon: Daemon):
        super().__init__(application_id="io.risi.rthemed",
                         flags=Gio.ApplicationFlags.IS_SERVICE)
        self.daemon = daemon
        try:
            session_bus.publish("io.risi.rthemed", DaemonBus(self.daemon))
        except RuntimeError:
            print("Failed to publish daemon to session bus.\nrThemed already running?")

        rtheme_settings.connect("changed::theme-name", self.refresh_theme, True)
        rtheme_settings.connect("changed::variant-name", self.refresh_theme, True)
        gnome_interface.connect("changed::color-scheme", self.refresh_theme, True)
        gnome_a11y.connect("changed::high-contrast", self.refresh_theme, True)

    def start(self):
        try:
            self.register()
            self.set_default()
            self.daemon.logger.log("rthemed started.")
            GLib.MainLoop().run()

        except GLib.Error as e:
            self.daemon.logger.log("Failed to register application: " + str(e))
            self.daemon.logger.log("rThemeD may already be running")

    def stop(self):
        self.daemon.logger.log("stopping rthemed.")
        GLib.MainLoop().quit()
        self.quit()

    def send_notification(self, notification_id, text, *args, **kwargs):
        notification = Gio.Notification.new("rthemed")
        notification.set_title("rTheme")
        notification.set_priority(Gio.NotificationPriority.URGENT)
        notification.set_body(text)
        super().send_notification(notification_id, notification, *args, **kwargs)


    def refresh_theme(self, notification: bool = True, *args, **kwargs):
        variants_available = [
            x.name for x in rthemelib.get_current_theme().variants
        ]
        if rtheme_settings.get_string("variant-name") not in variants_available:
            rtheme_settings.set_string("variant-name", "main")

        rthemelib.apply_theme(
            rthemelib.get_current_theme(),
            rtheme_settings.get_string("variant-name"),
            get_subvariant()
        )
        self.daemon.logger.log("applied theme.")
        if notification:
            self.send_notification(
                "changed_theme",
                "A theme change was detected. The theme has been refreshed.\n\n"
                "Some (or all) of your applications may need to be restarted for the changes to take effect."
            )
            self.daemon.logger.log(f"Theme refreshed to {rtheme_settings.get_string('theme-name')}")


class DaemonBus(object):
    """
        <node>
            <interface name='io.risi.rthemed'>
                <method name='Start' />
                <method name='Stop' />
                <method name='ViewLogs'>
                    <arg type='as' name='logs' direction='out' />
                </method>
                <method name='Status'>
                    <arg type='(bas)' name='logs' direction='out' />
                </method>
            </interface>
        </node>
    """

    def __init__(self, daemon):
        self.daemon = daemon
        self._daemon_running = False

    def Start(self):
        self._daemon_running = True
        self.daemon.application.start()

    def Stop(self):
        self.daemon.application.stop()
        self._daemon_running = False
        self.daemon.logger.log("rthemed stopped.")

    def ViewLogs(self):
        return self.daemon.logger.get_logs()

    def Status(self):
        return self._daemon_running, self.daemon.logger.get_logs()[:-1]


class InvalidDaemonBus(DaemonBus):
    def __init__(self):
        self.daemon = None
        self._daemon_running = False

    def Start(self):
        print("Cannot start daemon")

    def Stop(self):
        print("Cannot stop daemon. Maybe already stopped?")

    def ViewLogs(self):
        return ["Cannot connect to Daemon. Daemon not running?"]

    def Status(self):
        return False, ["Cannot connect to Daemon."]



def get_subvariant():
    if gnome_a11y.get_boolean("high-contrast"):
        high_contrast = "-hc"
    else:
        high_contrast = ""
    if gnome_interface.get_string("color-scheme") == "prefer-dark":
        return "dark" + high_contrast
    else:
        return "light" + high_contrast
    