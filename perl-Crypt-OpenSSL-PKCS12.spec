#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Crypt
%define		pnam	OpenSSL-PKCS12
Summary:	Crypt::OpenSSL::PKCS12 - Perl extension to OpenSSL's PKCS12 API
Name:		perl-%{pdir}-%{pnam}
Version:	1.99
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/J/JO/JONASBN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a01e2a2c67ada903f5499bcfdb2d43f0
URL:		https://metacpan.org/dist/Crypt-OpenSSL-PKCS12
BuildRequires:	openssl-devel
BuildRequires:	perl-Crypt-OpenSSL-Guess >= 0.11
BuildRequires:	perl-devel >= 1:5.14.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	openssl-tools
BuildRequires:	perl-Crypt-OpenSSL-PKCS10
BuildRequires:	perl-Pod-Coverage >= 0.19
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This implements a small bit of OpenSSL's PKCS12 API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes.md README
%{perl_vendorarch}/%{pdir}/OpenSSL/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS12
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS12/*.so
%{_mandir}/man3/*
