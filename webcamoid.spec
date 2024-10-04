%global __provides_exclude_from ^%{_libdir}/avkys

%define major 9
%define libname %mklibname avkys %{major}
%define devname %mklibname avkys -d

Summary:	Full featured and multiplatform webcam suite
Name:		webcamoid
Version:	9.2.3
Release:	1
License:	GPLv3
Group:		Video
Url:		https://github.com/webcamoid/webcamoid
Source0:	https://github.com/webcamoid/webcamoid/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:  qmake-qt6
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(VulkanHeaders)
BuildRequires:  pkgconfig(xkbcommon-x11)
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
%{_datadir}/metainfo/io.github.webcamoid.Webcamoid.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_libdir}/qt/plugins/avkys/
%{_mandir}/man1/webcamoid.1.*

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
