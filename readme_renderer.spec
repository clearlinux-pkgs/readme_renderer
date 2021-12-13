#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : readme_renderer
Version  : 32.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/5a/3e/e368a390fe7ffcfd0bfd2ec5220ece8907b4b79d0e9f1356c7ae27f03e54/readme_renderer-32.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/3e/e368a390fe7ffcfd0bfd2ec5220ece8907b4b79d0e9f1356c7ae27f03e54/readme_renderer-32.0.tar.gz
Summary  : readme_renderer is a library for rendering "readme" descriptions for Warehouse
Group    : Development/Tools
License  : Apache-2.0
Requires: readme_renderer-license = %{version}-%{release}
Requires: readme_renderer-python = %{version}-%{release}
Requires: readme_renderer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(bleach)
BuildRequires : pypi(docutils)
BuildRequires : pypi(pygments)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Readme Renderer
===============
Readme Renderer is a library that will safely render arbitrary
render the ``long_description`` for packages. It can handle Markdown,
reStructuredText (``.rst``), and plain text.

%package license
Summary: license components for the readme_renderer package.
Group: Default

%description license
license components for the readme_renderer package.


%package python
Summary: python components for the readme_renderer package.
Group: Default
Requires: readme_renderer-python3 = %{version}-%{release}

%description python
python components for the readme_renderer package.


%package python3
Summary: python3 components for the readme_renderer package.
Group: Default
Requires: python3-core
Provides: pypi(readme_renderer)
Requires: pypi(bleach)
Requires: pypi(docutils)
Requires: pypi(pygments)

%description python3
python3 components for the readme_renderer package.


%prep
%setup -q -n readme_renderer-32.0
cd %{_builddir}/readme_renderer-32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639423145
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/readme_renderer
cp %{_builddir}/readme_renderer-32.0/LICENSE %{buildroot}/usr/share/package-licenses/readme_renderer/43a3a49bd7af636c923a5ae475395b8e29320529
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/readme_renderer/43a3a49bd7af636c923a5ae475395b8e29320529

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
