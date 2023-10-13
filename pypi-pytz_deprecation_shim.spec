#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytz_deprecation_shim
Version  : 0.1.0.post0
Release  : 17
URL      : https://files.pythonhosted.org/packages/94/f0/909f94fea74759654390a3e1a9e4e185b6cd9aa810e533e3586f39da3097/pytz_deprecation_shim-0.1.0.post0.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/f0/909f94fea74759654390a3e1a9e4e185b6cd9aa810e533e3586f39da3097/pytz_deprecation_shim-0.1.0.post0.tar.gz
Summary  : Shims to make deprecation of pytz easier
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pytz_deprecation_shim-license = %{version}-%{release}
Requires: pypi-pytz_deprecation_shim-python = %{version}-%{release}
Requires: pypi-pytz_deprecation_shim-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tzdata)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
===========================================================
        
        ``pytz`` has served the Python community well for many years, but it is no
        longer the best option for providing time zones. ``pytz`` has a non-standard
        interface that is `very easy to misuse

%package license
Summary: license components for the pypi-pytz_deprecation_shim package.
Group: Default

%description license
license components for the pypi-pytz_deprecation_shim package.


%package python
Summary: python components for the pypi-pytz_deprecation_shim package.
Group: Default
Requires: pypi-pytz_deprecation_shim-python3 = %{version}-%{release}

%description python
python components for the pypi-pytz_deprecation_shim package.


%package python3
Summary: python3 components for the pypi-pytz_deprecation_shim package.
Group: Default
Requires: python3-core
Provides: pypi(pytz_deprecation_shim)
Requires: pypi(tzdata)

%description python3
python3 components for the pypi-pytz_deprecation_shim package.


%prep
%setup -q -n pytz_deprecation_shim-0.1.0.post0
cd %{_builddir}/pytz_deprecation_shim-0.1.0.post0
pushd ..
cp -a pytz_deprecation_shim-0.1.0.post0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656402729
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytz_deprecation_shim
cp %{_builddir}/pytz_deprecation_shim-0.1.0.post0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytz_deprecation_shim/a17821d024ce62859b8750020c3b7cbb2e6a57af
cp %{_builddir}/pytz_deprecation_shim-0.1.0.post0/licenses/LICENSE_APACHE %{buildroot}/usr/share/package-licenses/pypi-pytz_deprecation_shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytz_deprecation_shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-pytz_deprecation_shim/a17821d024ce62859b8750020c3b7cbb2e6a57af

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
