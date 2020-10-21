#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : readme_renderer
Version  : 28.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/a3/c4/03d640fbdb4d22830c98d1c76065f2cc40bc00994c7b7d365562d6b5492e/readme_renderer-28.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a3/c4/03d640fbdb4d22830c98d1c76065f2cc40bc00994c7b7d365562d6b5492e/readme_renderer-28.0.tar.gz
Summary  : readme_renderer is a library for rendering "readme" descriptions for Warehouse
Group    : Development/Tools
License  : Apache-2.0
Requires: readme_renderer-license = %{version}-%{release}
Requires: readme_renderer-python = %{version}-%{release}
Requires: readme_renderer-python3 = %{version}-%{release}
Requires: Pygments
Requires: bleach
Requires: cmarkgfm
Requires: docutils
Requires: six
BuildRequires : Pygments
BuildRequires : bleach
BuildRequires : buildreq-distutils3
BuildRequires : cmarkgfm
BuildRequires : docutils
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
===============
        
        Readme Renderer is a library that will safely render arbitrary
        ``README`` files into HTML. It is designed to be used in Warehouse_ to
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
Requires: pypi(six)

%description python3
python3 components for the readme_renderer package.


%prep
%setup -q -n readme_renderer-28.0
cd %{_builddir}/readme_renderer-28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603296286
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/readme_renderer
cp %{_builddir}/readme_renderer-28.0/LICENSE %{buildroot}/usr/share/package-licenses/readme_renderer/43a3a49bd7af636c923a5ae475395b8e29320529
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
