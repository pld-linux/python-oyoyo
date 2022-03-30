#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fast, simple IRC module suitable for clients, bots and games
Summary(pl.UTF-8):	Szybki, prosty moduł IRC odpowiedni dla klientów, botów i gier
Name:		python-oyoyo
Version:	0.0.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/oyoyo/
Source0:	https://files.pythonhosted.org/packages/source/o/oyoyo/oyoyo-%{version}dev.tar.gz
# Source0-md5:	ab5d74a96de284239cc0624dd5c1f8b5
URL:		https://pypi.org/project/oyoyo/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oyoyo IRC library is a small, simple IRC lib for Python suitable
for bots, clients and anything else you can think of (even games).

%description -l pl.UTF-8
Biblioteka IRC oyoyo to mała, prosta biblioteka dla Pythona, nadająca
się na potrzeby botów, klientów i czegokolwiek innego (nawet gier).

%package -n python3-oyoyo
Summary:	Fast, simple IRC module suitable for clients, bots and games
Summary(pl.UTF-8):	Szybki, prosty moduł IRC odpowiedni dla klientów, botów i gier
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-oyoyo
The oyoyo IRC library is a small, simple IRC lib for Python suitable
for bots, clients and anything else you can think of (even games).

%description -n python3-oyoyo -l pl.UTF-8
Biblioteka IRC oyoyo to mała, prosta biblioteka dla Pythona, nadająca
się na potrzeby botów, klientów i czegokolwiek innego (nawet gier).

%prep
%setup -q -n oyoyo-%{version}dev

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/oyoyo
%{py_sitescriptdir}/oyoyo-%{version}.dev0-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oyoyo
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/oyoyo
%{py3_sitescriptdir}/oyoyo-%{version}.dev0-py*.egg-info
%endif
