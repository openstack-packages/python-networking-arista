%global vendor Arista
%global srcname networking_arista
%global docpath doc/build/html

Name:           python-%{srcname}
Version:        2015.1.2
Release:        1%{?dist}
Summary:        %{vendor} OpenStack Neutron driver

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-mock
BuildRequires:  python-neutron-tests
BuildRequires:  python-oslo-sphinx
#BuildRequires:  python-oslotest
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-testrepository
BuildRequires:  python-testtools

Requires:       python-babel
Requires:       python-pbr


%description
This package contains %{vendor} networking driver for OpenStack Neutron.


%prep
%setup -q -n %{srcname}-%{upstream_version}


%build
rm requirements.txt test-requirements.txt
%{__python2} setup.py build
%{__python2} setup.py build_sphinx
rm %{docpath}/.buildinfo


#%check
#%{__python2} setup.py testr


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%files
%license LICENSE
%doc %{docpath}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
