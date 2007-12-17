%define name simage
%define version 1.6.1
%define release %mkrel 2

%define major 20
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d


Summary: A support library for importing textures and sound files in various fileformats
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphics
URL: http://www.coin3d.org/

%description 
simage is a support library for importing textures and sound files in
various fileformats

%package -n %{libname}
Summary: Main library for simage
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with simage.

%package -n %{libnamedev}
Summary: Headers for developing programs that will use simage
Group: Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: libsimage-devel

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use simage.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%prep
%setup -q

%build
%configure --with-mpeg2enc 
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root,0755)
%doc README AUTHORS NEWS COPYING
%_bindir/*
%_libdir/*.so
%_libdir/*.la
%_includedir/*
%_datadir/Coin/conf/*
%_datadir/aclocal/*
#%_mandir/man1/*

