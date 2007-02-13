#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Geometry-Planar-Offset
Summary:	Math::Geometry::Planar::Offset - calculate offset polygons
Summary(pl.UTF-8):	Math::Geometry::Planar::Offset - obliczanie wielokątów offsetowych
Name:		perl-Math-Geometry-Planar-Offset
Version:	1.03
Release:	1
# same as perl (README says it is Artistic only)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65243278d2335a740b6021333b669052
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# not BR - loop
Requires:	perl-Math-Geometry-Planar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a polygon offsetting function. The offset
calculated is a 'sharp cornered offset'. Both negative and positve
offsets are supported.

%description -l pl.UTF-8
Ten moduł dostarcza funkcję do obliczania wielokątów offsetowych.
Obliczony offset jest "offsetem o ostrych rogach". Obsługiwane są
przesunięcia dodatnie i ujemne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Geometry/Planar
%{perl_vendorlib}/Math/Geometry/Planar/Offset.pm
%{_mandir}/man3/*
