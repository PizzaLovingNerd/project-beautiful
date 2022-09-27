#!/usr/bin/env bash

sudo rm -rf /usr/lib64/python3.10/site-packages/rthemelib
sudo rm -rf /usr/lib64/python3.10/site-packages/rthemegtk
sudo rm -rf /usr/lib64/python3.10/site-packages/rthemed
sudo rm -rf /usr/share/rtheme
sudo rm /usr/share/glib-2.0/schemas/io.risi.rtheme.gschema.xml

sudo mkdir -p /usr/lib64/python3.10/site-packages/
sudo mkdir -p /usr/share/rtheme

sudo cp -a ../rthemelib /usr/lib64/python3.10/site-packages/rthemelib
sudo cp -a ../rthemegtk /usr/lib64/python3.10/site-packages/rthemegtk
sudo cp -a ../rthemed /usr/lib64/python3.10/site-packages/rthemed
sudo cp -a ../data/io.risi.rtheme.gschema.xml /usr/share/glib-2.0/schemas/io.risi.rtheme.gschema.xml
sudo cp -a ../data/*.desktop /usr/share/applications/

sudo glib-compile-schemas /usr/share/glib-2.0/schemas/ &>/dev/null

python3 __main__.py $1