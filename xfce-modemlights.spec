%define oname xfce4-modemlights-plugin

Summary:	Modemlights plugin for the Xfce panel
Name:		xfce-modemlights-plugin
Version:	0.1.3.99
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-modem-lights
Source0:	http://goodies.xfce.org/releases/xfce4-modemlights-plugin/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A modemlights panel plugin for the Xfce desktop environment.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS NEWS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/pixmaps/modem-*.png
