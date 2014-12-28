Summary:	Unicode character map (GTK+ 2 version)
Summary(pl.UTF-8):	Mapa znaków unikodowych (wersja dla GTK+ 2)
Name:		gucharmap2
Version:	3.0.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gucharmap/3.0/gucharmap-%{version}.tar.bz2
# Source0-md5:	754e1bc0ff7c190a8e8d855b2ca4ba16
Patch0:		%{name}-doc.patch
URL:		http://live.gnome.org/Gucharmap
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-doc-utils >= 0.12.2
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.24.0
Requires:	GConf2 >= 2.24.0
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	gucharmap
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl.UTF-8
Gucharmap jest wartościową mapą znaków unikodowych.

%package libs
Summary:	gucharmap library for GTK+ 2
Summary(pl.UTF-8):	Biblioteka gucharmap dla GTK+ 2
Group:		X11/Libraries
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+2 >= 2:2.18.0

%description libs
This package contains gucharmap library for GTK+ 2.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap dla GTK+ 2.

%package devel
Summary:	Headers for gucharmap (GTK+ 2 verson)
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap (wersja dla GTK+ 2)
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+2-devel >= 2:2.18.0

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap. This version is targeted for GTK+ 2.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap. Ta wersja jest przeznaczona dla GTK+ 2.

%package static
Summary:	Static gucharmap library for GTK+ 2
Summary(pl.UTF-8):	Statyczna biblioteka gucharmap dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap library for GTK+ 2.

%description static -l pl.UTF-8
Statyczna wersja biblioteki gucharmap dla GTK+ 2.

%package apidocs
Summary:	gucharmap library API documentation (GTK+ 2 version)
Summary(pl.UTF-8):	Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 2)
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gucharmap library API documentation (GTK+ 2 version).

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 2).

%prep
%setup -q -n gucharmap-%{version}
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-introspection \
	--enable-static \
	--with-gtk=2.0 \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gucharmap --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gucharmap.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gucharmap.schemas

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f gucharmap.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING.UNICODE ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/charmap
%attr(755,root,root) %{_bindir}/gucharmap
%attr(755,root,root) %{_bindir}/gnome-character-map
%{_sysconfdir}/gconf/schemas/gucharmap.schemas
%{_desktopdir}/gucharmap.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgucharmap.so.7
%{_libdir}/girepository-1.0/Gucharmap-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap.so
%{_includedir}/gucharmap-2.0
%{_pkgconfigdir}/gucharmap-2.pc
%{_datadir}/gir-1.0/Gucharmap-2.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgucharmap.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gucharmap-2.0
