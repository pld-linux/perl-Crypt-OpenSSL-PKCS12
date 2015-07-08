#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Crypt
%define		pnam	OpenSSL-PKCS12
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::OpenSSL::PKCS12 - Perl extension to OpenSSL's PKCS12 API
Name:		perl-%{pdir}-%{pnam}
Version:	0.7
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37e2c8bf80d815e9adf17cc641321287
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-PKCS12/
BuildRequires:	perl(Module::Install) >= 1.12
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Pod-Coverage >= 0.19
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This implements a small bit of OpenSSL's PKCS12 API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

rm -rf inc/Module/Install inc/Module/Install.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/%{pdir}/OpenSSL/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS12
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS12/*.so
%{_mandir}/man3/*
