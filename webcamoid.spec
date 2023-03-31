%global __provides_exclude_from ^%{_libdir}/avkys

%define major 9
%define libname %mklibname avkys %{major}
%define devname %mklibname avkys -d

Summary:	Full featured and multiplatform webcam suite
Name:		webcamoid
Version:	9.0.0
Release:	2
License:	GPLv3
Group:		Video
Url:		https://github.com/webcamoid/webcamoid
Source0:	https://github.com/webcamoid/webcamoid/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
Full featured and multiplatform webcam suite.

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_libdir}/avkys
%{_mandir}/%{name}.1.*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Webcamoid library
Group:		System/Libraries

%description -n %{libname}
Webcamoid library.

%files -n %{libname}
%{_libdir}/libavkys.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for webcamoid
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for webcamoid.

%files -n %{devname}
%doc README.md
%license COPYING
%{_libdir}/libavkys.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build
