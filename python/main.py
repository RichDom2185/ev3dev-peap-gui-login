#!/usr/bin/env python

import gi
import os

gi.require_version('Ev3devKit', '0.5')
from gi.repository import Ev3devKit

from prompt_window import PromptWindow


def do_activate(app):
    app.hold()
    demo_window = PromptWindow()
    demo_window.connect('quit', lambda _: app.quit())
    demo_window.show()


def main():
    app = Ev3devKit.ConsoleApp.new()

    activate_id = app.connect('activate', do_activate)

    app.run()
    app.disconnect(activate_id)
    os.system('sudo cp .credentials /var/lib/connman/nus_wifi.config')
    os.system('rm .credentials')

if __name__ == "__main__":
    main()
