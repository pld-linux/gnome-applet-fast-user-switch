%define		_realname	fast-user-switch-applet

Summary:	GNOME applet for fast user switching
Summary(pl):	Aplet GNOME do szybkiego prze³±czania u¿ytkowników
Name:		gnome-applet-fast-user-switch
Version:	2.13.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/fast-user-switch-applet/2.13/%{_realname}-%{version}.tar.bz2
# Source0-md5:	528fe2b5202198f0f18d00acc18cca15
URL:		http://ignore-your.tv/fusa
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdm >= 2.13.0.8
BuildRequires:	gettext-devel
BuildRequires:	gnome-panel-devel >= 2.10
BuildRequires:	gnome-system-tools >= 2.13.2
BuildRequires:	intltool >= 0.33
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	gnome-panel-devel >= 2.10
Requires:	gnome-system-tools >= 2.13.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fast User-Switching Applet is an applet for the GNOME panel which
provides a menu to switch between users.

%description -l pl
Fast User-Switching Applet to aplet panelu GNOME udostêpniaj±cy menu
do prze³±czania miêdzy u¿ytkownikami.

%prep
%setup -q -n %{_realname}-%{version}

%build
%configure \
	--disable-schemas-install \
	--with-gdm-setup=%{_sbindir}/gdmsetup \
	--with-gdm-config=%{_sysconfdir}/gdm/custom.conf \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{_realname}.schemas

%preun
%gconf_schema_uninstall %{_realname}.schemas

%files -f %{_realname}.lang
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README
%{_datadir}/%{_realname}
%{_gtkdocdir}/%{_realname}
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/%{_realname}.schemas
