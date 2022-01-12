%define major 20
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Name:		simage
Version:	1.8.1
Release:	1
Summary:	A support library for importing textures and sound files in various fileformats
License:	GPLv2
Group:		Graphics
URL:		http://coin3d.github.io/
Source0:	https://github.com/coin3d/simage/releases/download/v%{version}/simage-%{version}-src.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	giflib-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(vorbisfile)

%description 
simage is a support library for importing textures and sound files in
various fileformats

%package -n %{libname}
Summary:	Main library for simage
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with simage.

%package -n %{develname}
Summary:	Headers for developing programs that will use simage
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%mklibname %name -d 20

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use simage.

%prep
%autosetup -p1 -n %{name}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc README AUTHORS NEWS COPYING
%_bindir/*
%_libdir/*.so
%_libdir/pkgconfig/simage.pc
%_includedir/*
%_datadir/Coin/conf/*
%_libdir/cmake/%{name}-%{version}
