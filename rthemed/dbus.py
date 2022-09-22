from pydbus.generic import signal

class DaemonBus(object):
    """
        <node>
            <interface name='io.risi.rthemed'>
                <method name='EnableDaemon' />
                <method name='DisableDaemon' />
                <method name='ReloadDaemon' />
                <method name='StartDaemon' />
                <method name='StopDaemon' />
                <method name='ViewDaemonLogs'>
                    <arg type='s' name='logs' direction='out' />
                </method>
                <property name="DaemonStatus" type="s" access="read">
                    <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
                </property>
            </interface>
        </node>
    """

    def EnableDaemon(self):
        return

    def DisableDaemon(self):
        return

    def ReloadDaemon(self):
        return

    def StartDaemon(self):
        return

    def StopDaemon(self):
        return

    def ViewDaemonLogs(self):
        return self._daemonStatus

    def __init__(self):
        self._daemonStatus = "value"

    @property
    def DaemonStatus(self):
        return self._daemonStatus

    PropertiesChanged = signal()
