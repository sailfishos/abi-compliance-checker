Name:           abi-compliance-checker
Version:        1.98.4
Release:        1%{?dist}
Summary:        An ABI Compliance Checker

License:        GPL+ or LGPLv2+
URL:            http://ispras.linuxbase.org/index.php/ABI_compliance_checker
Source0:        https://github.com/lvc/%{name}/downloads/%{name}-%{version}.tar.gz

Requires:       gcc >= 4.5
Requires:       binutils

%{?perl_default_filter}

%description
A tool for checking backward binary compatibility of a shared C/C++ library. It
checks for changes in calling stack, changes in v-table, removed symbols, etc.


%prep
%setup -q


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*


%files
%doc LICENSE README doc/
%{_bindir}/%{name}
%{_datadir}/%{name}

