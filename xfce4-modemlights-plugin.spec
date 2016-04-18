Summary:	Modemlights plugin for the Xfce panel
Name:		xfce4-modemlights-plugin
Version:	0.1.3.99
Release:	14
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-modem-lights
Source0:	http://goodies.xfce.org/releases/xfce4-modemlights-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.4.0

%description
A modemlights panel plugin for the Xfce desktop environment.

%prep
%setup -q

%build
%define Werror_cflags %nil

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS NEWS
%{_libexecdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/pixmaps/modem-*.png
