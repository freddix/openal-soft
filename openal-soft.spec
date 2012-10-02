Summary:	OpenAL implementation
Name:		openal-soft
Version:	1.14
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kcat.strangesoft.net/openal-releases/%{name}-%{version}.tar.bz2
# Source0-md5:	3d8b86c21a2f87a2a5e60f78f3b3f03d
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	pulseaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAL Soft is a cross-platform software implementation
of the OpenAL 3D audio API.

%package devel
Summary:	Header files for openal library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for openal library.

%prep
%setup -q

sed -i -e "/Requires.*/d" openal.pc.in

%build
cd build
%cmake .. \
	-DEXAMPLES=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makehrtf
%attr(755,root,root) %{_bindir}/openal-info
%attr(755,root,root) %ghost %{_libdir}/libopenal.so.?
%attr(755,root,root) %{_libdir}/libopenal.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenal.so
%{_includedir}/AL
%{_pkgconfigdir}/*.pc

