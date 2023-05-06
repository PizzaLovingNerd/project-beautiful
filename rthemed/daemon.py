import traceback
import os

import rthemed
import rthemelib
from gi.repository import Gio
from gi.repository import GLib
from pydbus import SessionBus

gnome_interface = Gio.Settings.new("org.gnome.desktop.interface")
gnome_a11y = Gio.Settings.new("org.gnome.desktop.a11y.interface")
rtheme_settings = Gio.Settings.new("io.risi.rtheme")
session_bus = SessionBus()

no_notify_users = ["root", "liveuser", "gnome-initial-setup"]
username = os.getlogin()

class Daemon:
    def __init__(self):
        self.logger = rthemed.Logger()

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
        if username in no_notify_users:
            notification = False
        variants_available = [
            x.name for x in rthemelib.get_current_theme().variants
        ]
        if rtheme_settings.get_string("variant-name") not in variants_available:
            rtheme_settings.set_string("variant-name", "main")

        subvariant = get_subvariant()
        variant = rtheme_settings.get_string("variant-name")
        theme = rthemelib.get_current_theme()

        if subvariant not in theme.get_variant_from_name(variant).get_subvariant_names():
            original_subvariant = subvariant
            self.daemon.logger.log("Failed to get subvariant.")

            if subvariant.endswith("-hc"):
                subvariant = subvariant[:-3]

            if subvariant not in theme.get_variant_from_name(variant).get_subvariant_names():
                if subvariant == "light":
                    subvariant = "dark"
                elif subvariant == "dark":
                    subvariant = "light"
                if subvariant not in theme.get_variant_from_name(variant).get_subvariant_names():
                    self.daemon.logger.log(
                        f"Failed to get subvariant. Subvariant {original_subvariant} may not be supported by your theme."
                    )
                    if notification:
                        self.send_notification(
                            "theme_error",
                            "Unable to set theme."
                        )
                    return
                if notification:
                    self.daemon.logger.log(subvariant + " not available, using " + subvariant)
                    self.send_notification(
                        "theme_error",
                        f"Failed to get subvariant. Subvariant {original_subvariant} may not be supported by your theme."
                    )

        try:
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
        except Exception as e:
            self.daemon.logger.log("Failed to apply theme.")
            self.daemon.logger.log(traceback.print_exc())
            if notification:
                self.send_notification(
                    "theme_error",
                    "Unable to set theme."
                )


class DaemonBus(object):
    """
        <node>
            <interface name='io.risi.rthemed'>
                <method name='Start' />
            </interface>
        </node>
    """

    def __init__(self, daemon):
        self.daemon = daemon
        self._daemon_running = False

    def Start(self):
        self._daemon_running = True
        self.daemon.application.start()


class InvalidDaemonBus(DaemonBus):
    def __init__(self):
        self.daemon = None
        self._daemon_running = False

    def Start(self):
        print("Cannot start daemon")


def get_subvariant():
    if gnome_a11y.get_boolean("high-contrast"):
        high_contrast = "-hc"
    else:
        high_contrast = ""
    if gnome_interface.get_string("color-scheme") == "prefer-dark":
        return "dark" + high_contrast
    else:
        return "light" + high_contrast
    