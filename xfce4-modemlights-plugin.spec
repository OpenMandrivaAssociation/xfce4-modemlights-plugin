Summary:	Modemlights plugin for the Xfce panel
Name:		xfce4-modemlights-plugin
Version:	0.1.3.99
Release:	10
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-modem-lights
Source0:	http://goodies.xfce.org/releases/xfce4-modemlights-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
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
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/pixmaps/modem-*.png


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3.99-9mdv2010.1
+ Revision: 543430
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.1.3.99-8mdv2010.0
+ Revision: 446063
- rebuild

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3.99-7mdv2009.1
+ Revision: 360400
- disable checks for format-strings

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3.99-6mdv2009.1
+ Revision: 295000
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3.99-5mdv2009.0
+ Revision: 262364
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3.99-4mdv2009.0
+ Revision: 256878
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3.99-2mdv2008.1
+ Revision: 110123
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- use upstream name

* Thu Nov 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3.99-1mdv2008.1
+ Revision: 106949
- fix file list
- update to the latest rc
- update url
- fix mixture of tabs and spaces
- spec file clean

