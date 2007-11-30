%define		_realname	fast-user-switch-applet
Summary:	GNOME applet for fast user switching
Summary(pl.UTF-8):	Aplet GNOME do szybkiego przełączania użytkowników
Name:		gnome-applet-fast-user-switch
Version:	2.20.0
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/fast-user-switch-applet/2.20/%{_realname}-%{version}.tar.bz2
# Source0-md5:	1d1fd25b5599f7656e3fa89aa913137c
Patch0:		%{name}-ac.patch
Patch1:		%{name}-gdm-socket.patch
URL:		http://ignore-your.tv/fusa
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-panel-devel >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gdm >= 1:2.20.0
Suggests:	gnome-system-tools >= 2.20.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%patch1 -p1

sed -i -e 's#sr\@Latn#sr\@latin#' po/LINGUAS
mv po/sr\@{Latn,latin}.po

%build
%{__gnome_doc_prepare}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--with-gdm-config=%{_sysconfdir}/gdm/custom.conf \
	--with-gdm-setup=%{_sbindir}/gdmsetup \
	--with-users-admin=/usr/bin/users-admin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname} --with-gnome --with-omf

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
%{_datadir}/gnome-2.0/ui/GNOME_FastUserSwitchApplet.xml
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/%{_realname}.schemas
