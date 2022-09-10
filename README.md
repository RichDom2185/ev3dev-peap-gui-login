# ev3dev-peap-gui-login

A GUI-prompt to allow convenient login to PEAP/EAP networks on the EV3, tailored specifically for National University of Singapore's `NUS_STU` WiFi network, but easily adaptable to other networks.

## Background

EV3's [brickman brick manager](https://github.com/ev3dev/brickman) already has support for password authentication when connecting to WPA/WPA2-PSK ("personal") networks via the built-in GUI. However, this prompt is missing for WPA/WPA2-EAP ("enterprise") networks, and trying to connect to one from the EV3 directly will result in an error.

Previously, the only way to set up the network configuration in order to log in to EAP networks is by manually creating a configuration file in `/var/lib/connman/<configuration_file_name>.config`, but this involved either:

- SSH-ing into the EV3 via some means, which requires the user to have some knowledge and familiarity with the command line, or
- Supplying a pre-configured file in the OS image, which is not good for security

Hence, thanks to ev3dev's [ev3devKit](https://github.com/ev3dev/ev3devKit) UI library, this binary was created to make it simpler for the user to key in their credentials and log in, via a GUI that would be very familiar to most people. [Vala](<https://en.wikipedia.org/wiki/Vala_(programming_language)>) was chosen as a programming language as it compiles to C, keeping it fast. Alternatively, a python version is also available in [this branch](/../../tree/main).

The main use case for this is for National University of Singapore's [Source Academy ev3-source](https://github.com/source-academy/ev3-source) OS image. Hence, fields for the network name and other network options are implicitly set. This can be easily modified for other networks to suit other use cases.

## Building

### Docker

```bash
docker build -t ev3dev-peap-gui-login/compiler .
docker run --rm  -v "$(pwd)":/src -w /src -u 0:0 ev3dev-peap-gui-login/compiler -o <out_file_name> main.vala

# Clean up
docker rmi ev3dev-peap-gui-login/compiler
```

### Building manually

```bash
valac --pkg linux --pkg posix --pkg ev3devkit-0.5 --pkg gio-unix-2.0 --pkg grx-3.0 --pkg glib-2.0 --pkg gudev-1.0 main.vala -o <out_file_name>
```
