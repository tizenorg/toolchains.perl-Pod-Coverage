#specfile originally created for Fedora, modified for Moblin Linux
Name:           perl-Pod-Coverage
Version:        0.20
Release:        1
Summary:        Checks if the documentation of a module is comprehensive
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Coverage/
Source0:        %{name}-%{version}.tar.gz
Source1001:     packaging/perl-Pod-Coverage.manifest 
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Devel::Symdump) >= 2.01
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Developers hate writing documentation.  They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the
long run.  Even if not, perlmodstyle tells you to, so you must obey.

This module provides a mechanism for determining if the pod for a given
module is comprehensive.

%prep
%setup -q 

%build
cp %{SOURCE1001} .
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%manifest perl-Pod-Coverage.manifest
%defattr(-,root,root,-)
%doc Changes examples/
%{_bindir}/*
%{perl_vendorlib}/*
#%doc %{_mandir}/man3/*
