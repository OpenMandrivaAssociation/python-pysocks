%global oname	PySocks

Name:		python-pysocks
Summary:	A Python SOCKS client module
Version:	1.7.0
Release:	1
Group:		Development/Python
License:	BSD
URL:		https://github.com/Anorov/PySocks
Source0:	https://files.pythonhosted.org/packages/source/p/pysocks/PySocks-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)

BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)

%description
A Python SOCKS client module.

%package -n python2-pysocks
Summary:	A Python SOCKS client module
Group:		Development/Python
Provides:	python-pysocks = %{version}-%{release}

%description -n python2-pysocks
A Python SOCKS client module.

%package -n python3-pysocks
Summary:	A Python SOCKS client module
Group:		Development/Python

%description -n python3-pysocks
A Python SOCKS client module.

%prep
%setup -q -n %{oname}-%{version}

rm -rf %{oname}.egg-info

rm -rf %{py3dir}
cp -a . %{py3dir}

find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py2_build

pushd %{py3dir}
%py_build
popd

%install
pushd %{py3dir}
%py_install
popd

%py2_install

%files -n python2-pysocks
%license LICENSE
%doc README.md
%{python2_sitelib}/socks.py*
%{python2_sitelib}/sockshandler.py*
%{python2_sitelib}/%{oname}-%{version}-py%{python2_version}.egg-info

%files -n python3-pysocks
%license LICENSE
%doc README.md
%{python_sitelib}/socks.py
%{python_sitelib}/__pycache__/*
%{python_sitelib}/sockshandler.py
%{python_sitelib}/%{oname}-%{version}-py%{python3_version}.egg-info
