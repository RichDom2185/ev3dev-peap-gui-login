# ev3devKit - ev3dev toolkit for LEGO MINDSTORMS EV3
#
# Copyright 2015 David Lechner <david@lechnology.com>
#
# This program is free software you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

# ui_demo_window.py - Main window for widget demos

import gi

gi.require_version('Ev3devKit', '0.5')
from gi.repository import Ev3devKit
gi.require_version('Grx', '3.0')
from gi.repository import Grx
gi.require_version('GObject', '2.0')
from gi.repository import GObject


class PromptWindow(Ev3devKit.UiWindow):
    """Used to demonstrate most of the UI components in ev3devKit."""

    __gsignals__ = {
        # Emitted when the use selects the Quit menu item.
        'quit': (GObject.SIGNAL_RUN_LAST, None, ())
    }

    username = ''
    password = ''

    def __init__(self):
        """Creates a new instance of a demo window."""

        Ev3devKit.UiWindow.__init__(self)

        # window = Ev3devKit.UiWindow.new()

        # vbox = Ev3devKit.UiBox.vertical()
        # vbox.set_margin(6)
        # window.add(vbox)

        # self.add(window)

        # self.prompt_username()

        self.connect('shown', self.prompt_username)

        # don't close the window when we press back
        self.connect('key-pressed', self.do_key_pressed)


    def do_key_pressed(self, window, key_code):
        # ignore the backspace key press
        if key_code == Grx.Key.BACK_SPACE:
            GObject.signal_stop_emission_by_name(self, 'key-pressed')
            return True
        return False
    
    def quit(self, window):
        self.emit('quit')

    def prompt_username(self, window):
        username_dialog = Ev3devKit.UiInputDialog.new("Enter your NUSNET ID (e0XXXXXX)", "e")
        def handle_username(dialog, accepted):
            if not accepted: return
            self.username = dialog.get_text_value()
            self.prompt_password()
        username_dialog.connect('responded', handle_username)

        username_dialog.show()
    
    def prompt_password(self):
        password_dialog = Ev3devKit.UiInputDialog.new("Enter your NUSNET password", "")
        def handle_password(dialog, accepted):
            if not accepted: return
            self.password = dialog.get_text_value()
            # with open('credentials2.txt', 'w') as f:
            #         f.write(self.username + '\n' + self.password)
            # with open('/var/lib/connman/test.config', 'w') as f:
            with open('.credentials', 'w') as f:
                f.write(self.make_credential_file_string())
            self.display_credentials()
        password_dialog.connect('responded', handle_password)

        password_dialog.show()

    def make_credential_file_string(self):
        return """\
[global]
Name=NUS_STU

[service_peap]
Type=wifi
Name=NUS_STU
EAP=peap
Phase2=MSCHAPV2
Identity=%s
Passphrase=%s
""" % (self.username, self.password)
    
    def display_credentials(self):
        dialog = Ev3devKit.UiDialog.new()

        message_label = Ev3devKit.UiLabel.new(
            "Saved!\nUsername: " + self.username + "\nPassword: " + self.password
        )
        message_label.set_margin(4)

        quit_button = Ev3devKit.UiButton.new()
        quit_button.set_horizontal_align(Ev3devKit.UiWidgetAlign.CENTER)
        quit_button.set_vertical_align(Ev3devKit.UiWidgetAlign.END)
        label = Ev3devKit.UiLabel.new("Quit")
        quit_button.add(label)

        # pressing the button closes the dialog
        def on_button_pressed(button):
            dialog.close()
            self.emit('quit')

        handler_id = quit_button.connect('pressed', on_button_pressed)
        # have to disconnect this signal when the dialog is closed to break
        # the reference cycle on the dialog object.
        def on_dialog_closed(dialog):
            quit_button.disconnect(handler_id)

        dialog.connect('closed', on_dialog_closed)
        vbox = Ev3devKit.UiBox.vertical()
        vbox.set_padding_top(2)
        vbox.set_padding_bottom(6)
        vbox.set_spacing(2)

        vbox.add(message_label)
        vbox.add(quit_button)
        dialog.add(vbox)

        dialog.show()
