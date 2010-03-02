%define name simage
%define version 1.7.0
%define release %mkrel 1

%define major 20
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A support library for importing textures and sound files in various fileformats
License:	GPLv2
Group:		Graphics
URL:		http://www.coin3d.org/
Source0:	http://ftp.coin3d.org/coin/src/all/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
simage is a support library for importing textures and sound files in
various fileformats

%package -n %{libname}
Summary:	Main library for simage
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with simage.

%package -n %{develname}
Summary:	Headers for developing programs that will use simage
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %name -d 20

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use simage.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%prep
%setup -q

%build
%configure2_5x --with-mpeg2enc 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS NEWS COPYING
%_bindir/*
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/simage.pc
%_includedir/*
%_datadir/Coin/conf/*
%_datadir/aclocal/*
