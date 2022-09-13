import rthemed
import rthemelib
from gi.repository import Gio
from gi.repository import GLib

gnome_interface = Gio.Settings.new("org.gnome.desktop.interface")
gnome_a11y = Gio.Settings.new("org.gnome.desktop.a11y.interface")
rtheme_settings = Gio.Settings.new("io.risi.rtheme")


class Daemon:
    def __init__(self):
        self.logger = rthemed.Logger()
        rthemelib.logger = self.logger
        self.application = DaemonApplication(self)
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
            self.register()
            self.set_default()
        except GLib.Error as e:
            self.daemon.logger.log("Failed to register application: " + str(e))
            self.daemon.logger.log("rThemeD may already be running")
            print(self)
            print(self.get_default())

        rtheme_settings.connect("changed::theme-name", self.refresh_theme, True)
        rtheme_settings.connect("changed::variant-name", self.refresh_theme, True)
        gnome_interface.connect("changed::color-scheme", self.refresh_theme, True)
        gnome_a11y.connect("changed::high-contrast", self.refresh_theme, True)

        GLib.MainLoop().run()

    def do_activate(self):
        pass

    def send_notification(self, notification_id, text, *args, **kwargs):
        notification = Gio.Notification.new("rthemed")
        notification.set_title("rTheme")
        notification.set_priority(Gio.NotificationPriority.URGENT)
        notification.set_body(text)
        super().send_notification(notification_id, notification, *args, **kwargs)

    def refresh_theme(self, notification: bool = True, *args, **kwargs):
        rthemed.apply_theme()
        if notification:
            self.send_notification(
                "changed_theme",
                "A theme change was detected. The theme has been refreshed.\n\n"
                "Some (or all) of your applications may need to be restarted for the changes to take effect."
            )
