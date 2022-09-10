// build command : valac --pkg linux --pkg posix --pkg ev3devkit-0.5 --pkg gio-unix-2.0 --pkg grx-3.0 --pkg glib-2.0 --pkg gudev-1.0 main.vala -o bin
using Ev3devKit.Ui;

static string generate_credential_file_string (string username, string password)
{
    return """[global]
Name=NUS_STU

[service_peap]
Type=wifi
Name=NUS_STU
EAP=peap
Phase2=MSCHAPV2
Identity=%s
Passphrase=%s""".printf (username, password);
}

static int main (string[] args)
{
    string username = "";
    string password = "";
    try {
        Posix.system ("rm -f .credentials"); // remove old credentials file

        var app = new Ev3devKit.ConsoleApp ();

        var activate_id = app.activate.connect (() => {
            app.hold ();

            var main_window = new Window (); // blank background
            var username_dialog = new InputDialog ("Enter your NUSNET ID (e0XXXXXX)", "e");
            var password_dialog = new InputDialog ("Enter your NUSNET password", "");
            var message_dialog = new Dialog ();

            main_window.shown.connect (() => {
                username_dialog.show ();
            });

            username_dialog.responded.connect (() => {
                username = username_dialog.text_value;
                username_dialog.close ();
                password_dialog.show ();
            });

            password_dialog.responded.connect (() => {
                password = password_dialog.text_value;
                password_dialog.close ();

                var file = File.new_for_path (".credentials");
                string credential_file_string = generate_credential_file_string (username, password);
                {
                    var file_stream = file.create (FileCreateFlags.NONE);
                    var data_stream = new DataOutputStream (file_stream);
                    data_stream.put_string (credential_file_string);
                } // Stream closes automatically at this point.

                var message_label = new Label ("Saved!\nUsername: " + username + "\nPassword: " + password);
                message_label.margin = 4;

                var quit_button = new Button ();
                quit_button.horizontal_align = WidgetAlign.CENTER;
                quit_button.vertical_align = WidgetAlign.END;

                var quit_button_label = new Label ("Quit");
                quit_button.add (quit_button_label);

                var handler_id = quit_button.pressed.connect (() => {
                    message_dialog.close ();
                    app.quit ();
                });
                message_dialog.closed.connect (() => {
                    quit_button.disconnect (handler_id);
                });

                var vbox = new Box.vertical ();
                vbox.padding_top = 2;
                vbox.padding_bottom = 6;
                vbox.spacing = 2;
                vbox.add (message_label);
                vbox.add (quit_button);
                message_dialog.add (vbox);

                message_dialog.show ();
            });

            main_window.show ();
        });

        app.run ();
        app.disconnect (activate_id);

        Posix.system ("sudo cp .credentials /var/lib/connman/nus_wifi.config");
        Posix.system ("rm -f .credentials");

        return 0;
    } catch (GLib.Error err) {
        critical ("%s", err.message);
        Process.exit (err.code);
    }
}