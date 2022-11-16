Name:           rtheme
Version:        0.2
Release:        16%{?dist}
Summary:        rtheme is a theme manager for the Linux desktop

License:        GPL v3
URL:            https://github.com/risiIndustries/rtheme
Source0:        https://github.com/risiIndustries/rtheme/archive/refs/heads/main.tar.gz

BuildArch:      noarch
BuildRequires:  python3.11-devel
BuildRequires:  python3.11-gobject
BuildRequires:  python3.11-pydbus
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake

%description
Easily Modify and create themes with a .yml file and some plugins.

%package lib
Summary:        rtheme library
Requires:       python3
Requires:       python3-gobject
%description lib
rtheme library used for cli and python3

%package d
Summary:        rtheme daemon
Requires:       systemd
Requires:       python3
Requires:       python3-pydbus
Requires:       python3-gobject
Requires:       rtheme-lib
%description d
Runs rtheme in the background and updates the theme when needed

%package plugin-gtk3
Summary:        rtheme gtk3 plugin
Requires:       python3
Requires:       python3-gobject
Requires:       rtheme-lib
Requires:       adw-gtk-theme

%description plugin-gtk3
rtheme gtk3 plugin

%package plugin-gtk4
Summary:        rtheme gtk4 plugin
Requires:       python3
Requires:       python3-gobject
Requires:       rtheme-lib

%description plugin-gtk4
rtheme gtk4 plugin

%package plugin-gnome-shell
Summary: Adds gnome shell support
Requires: python3
Requires: python3-gobject
Requires: rtheme-lib
Requires: gnome-shell-extension-risi-gnome
Requires: sassc

%description plugin-gnome-shell
Adds support for GNOME Shell

%prep
%autosetup -n rtheme-main
%build
%install

# Python Libraries
mkdir -p %{buildroot}%{python3_sitelib}
cp -a rthemelib %{buildroot}%{python3_sitelib}
cp -a rthemed %{buildroot}%{python3_sitelib}

# Themes
mkdir -p %{buildroot}%{_datadir}
cp -a themes %{buildroot}%{_datadir}/rthemes

# Data
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
mkdir -p %{buildroot}%{_datadir}/applications
cp data/io.risi.rtheme.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/io.risi.rtheme.gschema.xml
cp data/io.risi.rthemed.desktop %{buildroot}%{_datadir}/applications

# SystemD
mkdir -p %{bootroot}%{_userunitdir}
mkdir -p %{buildroot}%{_userpresetdir}
cp -a rthemed/systemd/rthemed.service %{buildroot}%{_userunitdir}/rthemed.service
cp -a rthemed/systemd/95-rthemed.preset %{buildroot}%{_userpresetdir}/95-rthemed.preset

# Binaries
mkdir %{buildroot}%{_bindir}
cp rthemed/__main__.py %{buildroot}%{_bindir}/rthemed
cp rthemelib/__main__.py %{buildroot}%{_bindir}/rthemelib

%files lib
%{python3_sitelib}/rthemelib
%{_datadir}/rthemes
%{_datadir}/glib-2.0/schemas/io.risi.rtheme.gschema.xml

%post d
%systemd_user_post rthemed.service

%preun d
%systemd_user_preun rthemed.service

%files d
%{_datadir}/applications/io.risi.rthemed.desktop
%{_bindir}/rthemed
%{_userunitdir}/rthemed.service
%{_userpresetdir}/95-rthemed.preset

%files plugin-gtk3
%{python3_sitelib}/rthemelib/plugins/gtk3.py

%files plugin-gtk4
%{python3_sitelib}/rthemelib/plugins/gtk4.py

%files plugin-gnome-shell
%{python3_sitelib}/rthemelib/plugins/gnome-shell

%changelog
* Sun Oct 9 2022 PizzaLovingNerd
- Initial build
