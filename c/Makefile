all: main.o
	gcc main.o -o bin
# The required gcc flags can be found in the following tutorial:
# https://docs.gtk.org/glib/compiling.html
# Adapt accordingly for package ev3devkit-0.5
main.o: main.c
	gcc -pthread -I/usr/include/gio-unix-2.0/ -I/usr/include/libpng16 -I/usr/include/freetype2 -I/usr/include/gudev-1.0 -I/usr/include/glib-2.0 -I/usr/lib/arm-linux-gnueabi/glib-2.0/include -lev3devkit-0.5 -lgio-2.0 -Wl,--export-dynamic -lgmodule-2.0 -pthread -lgrx-3.0 -lgio-2.0 -lgudev-1.0 -lgobject-2.0 -lglib-2.0 -c main.c
clean:
	rm -rf *.o
	rm bin