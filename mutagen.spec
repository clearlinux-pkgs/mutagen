#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mutagen
Version  : 1.42.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/30/4c/5ad1a6e1ccbcfaf6462db727989c302d9d721beedd9b09c11e6f0c7065b0/mutagen-1.42.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/4c/5ad1a6e1ccbcfaf6462db727989c302d9d721beedd9b09c11e6f0c7065b0/mutagen-1.42.0.tar.gz
Summary  : read and write audio tags for many formats
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0-or-later
Requires: mutagen-bin = %{version}-%{release}
Requires: mutagen-license = %{version}-%{release}
Requires: mutagen-man = %{version}-%{release}
Requires: mutagen-python = %{version}-%{release}
Requires: mutagen-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://cdn.rawgit.com/quodlibet/mutagen/master/docs/images/logo.svg
:align: center
:width: 400px

%package bin
Summary: bin components for the mutagen package.
Group: Binaries
Requires: mutagen-license = %{version}-%{release}
Requires: mutagen-man = %{version}-%{release}

%description bin
bin components for the mutagen package.


%package license
Summary: license components for the mutagen package.
Group: Default

%description license
license components for the mutagen package.


%package man
Summary: man components for the mutagen package.
Group: Default

%description man
man components for the mutagen package.


%package python
Summary: python components for the mutagen package.
Group: Default
Requires: mutagen-python3 = %{version}-%{release}

%description python
python components for the mutagen package.


%package python3
Summary: python3 components for the mutagen package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mutagen package.


%prep
%setup -q -n mutagen-1.42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545837146
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mutagen
cp COPYING %{buildroot}/usr/share/package-licenses/mutagen/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mid3cp
/usr/bin/mid3iconv
/usr/bin/mid3v2
/usr/bin/moggsplit
/usr/bin/mutagen-inspect
/usr/bin/mutagen-pony

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mutagen/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mid3cp.1
/usr/share/man/man1/mid3iconv.1
/usr/share/man/man1/mid3v2.1
/usr/share/man/man1/moggsplit.1
/usr/share/man/man1/mutagen-inspect.1
/usr/share/man/man1/mutagen-pony.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
