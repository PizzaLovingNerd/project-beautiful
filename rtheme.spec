Name:           rtheme
Version:        0.1
Release:        1%{?dist}
Summary:        rtheme is a theme manager for the Linux desktop

License:        GPL v3
URL:            https://github.com/risiIndustries/rtheme
Source0:        https://github.com/risiIndustries/rtheme/archive/refs/heads/main.tar.gz

BuildArch:      noarch

%description
Easily Modify and create themes with a .yml file and some plugins.

%package lib
Summary:        rtheme library
Requires:       python3.10
Requires:       python3.10-gobject
%description lib
rtheme library used for cli and python3

%package d
Summary:        rtheme daemon
Requires:       python3.10
Requires:       python3.10-gobject
Requires:       rtheme-lib
%description d
Runs rtheme in the background and updates the theme when needed

%package plugin-gtk3
Summary:        rtheme gtk3 plugin
Requires:       python3.10
Requires:       python3.10-gobject
Requires:       rtheme-lib
Requires:       adw-gtk

%description plugin-gtk3
rtheme gtk3 plugin

%package plugin-gtk4
Summary:        rtheme gtk4 plugin
Requires:       python3.10
Requires:       python3.10-gobject
Requires:       rtheme-lib

%description plugin-gtk4

%prep
%autosetup -n rtheme-main
%build
meson build

%install
%meson_install

%files lib
%{python3_sitelib}/rthemelib
%{_datadir}/rthemes
%{_datadir}/glib-2.0/schemas/io.risi.rtheme.gschema.xml

%files d
%{_datadir}/rthemed
%{_datadir}/applications/rthemed.desktop
%{_bindir}/rthemed

%files plugin-gtk3
%{python3_sitelib}/rthemelib/plugins/gtk3.py

%files plugin-gtk4
%{python3_sitelib}/rthemelib/plugins/gtk4.py

%changelog
* Sun Oct 9 2022 PizzaLovingNerd
- Initial build