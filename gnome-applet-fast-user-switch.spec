%define		_realname	fast-user-switch-applet

Summary:	GNOME applet for fast user switching
Summary(pl):	Aplet GNOME do szybkiego prze³±czania u¿ytkowników
Name:		gnome-applet-fast-user-switch
Version:	2.14.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/fast-user-switch-applet/2.14/%{_realname}-%{version}.tar.bz2
# Source0-md5:	81eb5d66cc9f7425ba4accae2e8f3573
Patch0:		%{name}-ac.patch
URL:		http://ignore-your.tv/fusa
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-panel-devel >= 2.10
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	gdm
# only required when --with-users-admin enabled
# TODO for now
# Requires:	gnome-system-tools >= 2.13.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fast User-Switching Applet is an applet for the GNOME panel which
provides a menu to switch between users.

%description -l pl
Fast User-Switching Applet to aplet panelu GNOME udostêpniaj±cy menu
do prze³±czania miêdzy u¿ytkownikami.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p1

%build
gnome-doc-prepare --copy --force
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--with-gdm-config=%{_sysconfdir}/gdm/custom.conf \
	--with-gdm-setup=%{_sbindir}/gdmsetup
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{_realname}.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall %{_realname}.schemas

%postun
%scrollkeeper_update_postun

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_libdir}/%{_realname}
%{_datadir}/%{_realname}
%{_datadir}/gnome-2.0
%{_libdir}/bonobo/servers/*.server
%{_omf_dest_dir}/%{_realname}/%{_realname}-C.omf
%lang(es) %{_omf_dest_dir}/%{_realname}/%{_realname}-es.omf
%lang(pa) %{_omf_dest_dir}/%{_realname}/%{_realname}-pa.omf
%lang(sr) %{_omf_dest_dir}/%{_realname}/%{_realname}-sr.omf
%{_sysconfdir}/gconf/schemas/%{_realname}.schemas
