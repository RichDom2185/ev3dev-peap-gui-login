// #include "src/ev3devkit-0.5.h"
// #include "src/grx-3.0.h"
#include <ev3devkit-0.5.h>
#include <grx-3.0.h>
#include <stdio.h>

static void activate(Ev3devKitConsoleApp *app)
{
    // Ev3devKitConsoleAppClass *klass = EV3DEVKIT_CONSOLE_APP_GET_CLASS(app);

    // if (klass->activate)
    //     klass->activate(app);

    // EV3DEV_KIT_UI_WINDOW
    Ev3devKitUiInputDialog *usernameDialog;
    Ev3devKitUiInputDialog *passwordDialog;
    Ev3devKitUiMessageDialog *messageDialog;
    const gchar *username;
    const gchar *password;

    usernameDialog = ev3dev_kit_ui_input_dialog_new("Enter your NUSNET ID (e0XXXXXX)", "e");
    passwordDialog = ev3dev_kit_ui_input_dialog_new("Enter your NUSNET password", "");
    
    username = ev3dev_kit_ui_input_dialog_get_text_value(usernameDialog);
    password = ev3dev_kit_ui_input_dialog_get_text_value(passwordDialog);

    Ev3devKitUiWindow *window = ev3dev_kit_ui_window_new();

    messageDialog = ev3dev_kit_ui_message_dialog_new("Testing", "test sentece");

    // ev3dev_kit_ui_window_show(EV3DEV_KIT_UI_WINDOW(usernameDialog));
    // sleep(3);
    // ev3dev_kit_ui_window_close(EV3DEV_KIT_UI_WINDOW(messageDialog));
    ev3dev_kit_ui_widget_draw_content(EV3DEV_KIT_UI_WIDGET(window));
    ev3dev_kit_ui_window_show(window);
    ev3dev_kit_ui_widget_draw_content(EV3DEV_KIT_UI_WIDGET(window));
    sleep(3);
    ev3dev_kit_ui_window_close(window);
}

int main(int argc, char *argv[])
{
    Ev3devKitConsoleApp *app;
    int status;

    GError *error;

    app = ev3dev_kit_console_app_new(&error);

    activate(app);

    return status;
}