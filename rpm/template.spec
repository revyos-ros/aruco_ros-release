Name:           ros-indigo-aruco-ros
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS aruco_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.uco.es/investiga/grupos/ava/node/26
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-aruco
Requires:       ros-indigo-aruco-msgs
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-aruco
BuildRequires:  ros-indigo-aruco-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
The ARUCO Library has been developed by the Ava group of the Univeristy of
Cordoba(Spain). It provides real-time marker based 3D pose estimation using AR
markers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 10 2015 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

* Fri Aug 07 2015 Bence Magyar <bence.magyar@pal-robotics.com> - 0.0.1-0
- Autogenerated by Bloom

