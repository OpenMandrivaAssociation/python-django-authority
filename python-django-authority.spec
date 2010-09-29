%define  oname  django-authority
Name:           python-%{oname}
Version:        0.3
Release:        %mkrel 1
Summary:        A Django app for generic per-object permissions and custom permission checks

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/jezdez/%{oname}/
Source:         http://bitbucket.org/jezdez/%{oname}/downloads/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
This is a Django app for generic per-object permissions, custom permission
checks and permission requests. It also includes view decorators and template 
tags for ease of use.

%prep
%setup -q -n %{oname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README docs/build/html/
%{python_sitelib}/*

