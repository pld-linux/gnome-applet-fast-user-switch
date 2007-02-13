%define		_realname	fast-user-switch-applet
Summary:	GNOME applet for fast user switching
Summary(pl.UTF-8):	Aplet GNOME do szybkiego przełączania użytkowników
Name:		gnome-applet-fast-user-switch
Version:	2.16.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/fast-user-switch-applet/2.16/%{_realname}-%{version}.tar.bz2
# Source0-md5:	16fe9bb182fd96ebbc65c53c5aaf6752
Patch0:		%{name}-ac.patch
URL:		http://ignore-your.tv/fusa
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-panel-devel >= 2.16.3
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.4
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	gdm >= 1:2.16.0
# only required when --with-users-admin enabled
# TODO for now
# Requires:	gnome-system-tools >= 2.13.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fast User-Switching Applet is an applet for the GNOME panel which
provides a menu to switch between users.

%description -l pl.UTF-8
Fast User-Switching Applet to aplet panelu GNOME udostępniający menu
do przełączania między użytkownikami.

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
%dir %{_omf_dest_dir}/%{_realname}
%{_omf_dest_dir}/%{_realname}/%{_realname}-C.omf
%lang(es) %{_omf_dest_dir}/%{_realname}/%{_realname}-es.omf
%lang(fr) %{_omf_dest_dir}/%{_realname}/%{_realname}-fr.omf
%lang(pa) %{_omf_dest_dir}/%{_realname}/%{_realname}-pa.omf
%lang(sr) %{_omf_dest_dir}/%{_realname}/%{_realname}-sr.omf
%lang(sv) %{_omf_dest_dir}/%{_realname}/%{_realname}-sv.omf
%{_sysconfdir}/gconf/schemas/%{_realname}.schemas
