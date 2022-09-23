from pydbus.generic import signal
from rthemed.daemon import Daemon


class DaemonBus(object):
    """
        <node>
            <interface name='io.risi.rthemed'>
                <method name='Enable' />
                <method name='Disable' />
                <method name='Reload' />
                <method name='Start' />
                <method name='Stop' />
                <method name='ViewLogs'>
                    <arg type='s' name='logs' direction='out' />
                </method>
                <property name="Status" type="s" access="read">
                    <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
                </property>
            </interface>
        </node>
    """

    def Enable(self):
        return

    def Disable(self):
        return

    def Reload(self):
        return

    def Start(self):
        return

    def Stop(self):
        return

    def ViewLogs(self):
        return self._daemonStatus

    def __init__(self, daemon: Daemon):
        self._daemonStatus = "value"
        Daemon.send_notification(self, "changed_theme", "text")

    @property
    def Status(self):
        return self._daemonStatus

    PropertiesChanged = signal()
