#!/bin/env python3

import rthemelib
import rthemed.daemon
import sys
from gi.repository import Gio, GLib
from pydbus import SessionBus

bus = SessionBus()
try:
    daemonbus = bus.get("io.risi.rthemed", "/io/risi/rthemed")
except GLib.Error:
    daemonbus = rthemed.daemon.InvalidDaemonBus()
    print("rthemed is not running.")

rtheme_settings = Gio.Settings.new("io.risi.rtheme")

def check_arguments(arg):
    if not len(sys.argv) - 1 == arg:
        print(rthemelib.constants.HELP_PROMPT)
        exit(1)

def main():
    if len(sys.argv) < 2:
        print(rthemelib.constants.HELP_PROMPT)
        exit(1)

    match sys.argv[1]:
        case "status":
            check_arguments(1)
            if daemonbus.Status()[0]:
                print("rthemed is currently running.")
            else:
                print("rthemed is not running.")

        case "start":
            print("Starting rthemed...")
            daemon = rthemed.daemon.DaemonBus(rthemed.daemon.Daemon())
            daemon.Start()
        case default:
            print(rthemelib.constants.HELP_PROMPT)
