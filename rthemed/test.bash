#!/usr/bin/env bash

# Get the current Python version in the format MAJOR.MINOR
PYTHON_VERSION=$(python -c 'import platform; major, minor, patch = platform.python_version_tuple(); print("{}.{}".format(major, minor));')
SITE_PACKAGES=$(python -m site --user-site)

echo "Using Python $PYTHON_VERSION, with site packages at $SITE_PACKAGES"

rm -rf $SITE_PACKAGES/rthemelib
rm -rf $SITE_PACKAGES/rthemegtk
rm -rf $SITE_PACKAGES/rthemed
sudo rm -rf /usr/share/rtheme
sudo rm /usr/share/glib-2.0/schemas/io.risi.rtheme.gschema.xml

mkdir -p $SITE_PACKAGES
sudo mkdir -p /usr/share/rtheme

cp -a ../rthemelib $SITE_PACKAGES/rthemelib
cp -a ../rthemegtk $SITE_PACKAGES/rthemegtk
cp -a ../rthemed $SITE_PACKAGES/rthemed
sudo cp -a ../data/io.risi.rtheme.gschema.xml /usr/share/glib-2.0/schemas/io.risi.rtheme.gschema.xml
sudo cp -a ../data/*.desktop /usr/share/applications/

sudo glib-compile-schemas /usr/share/glib-2.0/schemas/ &>/dev/null

python3 __main__.py $1