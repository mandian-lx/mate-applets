%define url_ver %(echo %{version}|cut -d. -f1,2)

# cpupower requires a kegksu support disabled. It doesn't work with our gksu-polkit
%bcond_with cpupower

Summary:	Small applications which embed themselves in the MATE panel
Name:		mate-applets
Version:	1.18.2
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

%if %{with cpupower}
BuildRequires:	cpupower-devel
%endif
BuildRequires:	intltool
BuildRequires:	libiw-devel
BuildRequires:	mate-common
BuildRequires:	mate-notification-daemon
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-audio-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(gucharmap-2.90)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(mateweather)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-settings-daemon)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	xsltproc
BuildRequires:	yelp-tools

Requires:	mate-panel
Requires:	polkit-agent
Requires:	python-gi
Requires:	typelib(MatePanelApplet)
Requires:	usermode-consoleonly

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides applets for use with the MATE panel.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%config(noreplace) %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_bindir}/*
%{_libexecdir}/mate-applets/*applet*
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/mate-applets/*
%{_datadir}/mate/ui/*
%{_datadir}/mate-panel/applets/org.mate.applets.AccessxStatusApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.BattstatApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CharpickerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CommandApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CPUFreqApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.DriveMountApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.GeyesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MateWeatherApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TimerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.NetspeedApplet.mate-panel-applet
%{_datadir}/pixmaps/*
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_datadir}/dbus-1/services/org.mate.panel.applet.InvestAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.InvestApplet.mate-panel-applet
%{_iconsdir}/hicolor/*/*/*
%{py2_puresitedir}/mate_invest
%{_mandir}/man1/mate-charpick-applet.1.xz
%{_mandir}/man1/mate-cpufreq-selector.1.xz
%{_mandir}/man1/mate-drivemount-applet.1.xz
%{_mandir}/man1/mate-geyes-applet.1.xz
%{_mandir}/man1/mate-invest-chart.1.xz
%{_mandir}/man1/mate-multiload-applet.1.xz
%{_mandir}/man1/mateweather.1.xz

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export PYTHON=python2
%configure \
	--disable-schemas-compile \
	--enable-stickynotes \
	--libexecdir=%{_libexecdir}/mate-applets \
%if %{with cpupower}
	--with-cpufreq-lib=cpupower \
%endif
	%{nil}
%make

%install
%makeinstall_std

# fix permission
chmod 0755 %{buildroot}%{python2_sitelib}/mate_invest/chart.py

# remove compiled python files
rm -fr %{buildroot}%{python2_sitelib}/mate_invest/*.{pyc,pyo}

# locales
%find_lang %{name} --with-gnome --all-name

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

