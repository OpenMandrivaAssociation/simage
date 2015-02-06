%define major 20
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Name:		simage
Version:	1.7.0
Release:	4
Summary:	A support library for importing textures and sound files in various fileformats
License:	GPLv2
Group:		Graphics
URL:		http://www.coin3d.org/
Source0:	http://ftp.coin3d.org/coin/src/all/%{name}-%{version}.tar.gz

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
%setup -q

%build
%configure2_5x --with-mpeg2enc 
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc README AUTHORS NEWS COPYING
%_bindir/*
%_libdir/*.so
%_libdir/pkgconfig/simage.pc
%_includedir/*
%_datadir/Coin/conf/*
%_datadir/aclocal/*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-2mdv2011.0
+ Revision: 614870
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.7.0-1mdv2010.1
+ Revision: 513688
- fix source0, use tar.gz
- cleaning builroot at %%install
- update to 1.7.0
- fix file list, %%_libdir/pkgconfig/simage.pc was missing

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request
    - import simage

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - use %%configure2_5x macro
    - new devel policy

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers


* Tue Jan 03 2006 Lenny Cartier <lenny@mandrakesoft.com> 1.6.1-2mdk
- rebuild

* Tue Nov 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.6.1-1mdk
- 1.6.1

* Mon Oct 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0a-1mdk
- from Jan Villat <rpms@djdie.net> :
	- Updated version number

* Wed May 07 2003 Jan Villat <rpms@djdie.net> 1.0.0-1mdk
- Creating correct lib... and lib..-devel packages

# end of file
