%global oname	PySocks

Name:		python-pysocks
Summary:	A Python SOCKS client module
Version:	1.7.1
Release:	6
Group:		Development/Python
License:	BSD
URL:		https://github.com/Anorov/PySocks
Source0:	https://files.pythonhosted.org/packages/bd/11/293dd436aea955d45fc4e8a35b6ae7270f5b8e00b53cf6c024c83b657a11/PySocks-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%rename python3-pysocks

%description
A Python SOCKS client module.

%prep
%autosetup -p1 -n %{oname}-%{version}

rm -rf %{oname}.egg-info

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/socks.py
%{python_sitelib}/sockshandler.py
%{python_sitelib}/%{oname}-%{version}-py%{python3_version}.egg-info
