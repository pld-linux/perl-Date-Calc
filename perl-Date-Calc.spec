#
# TODO:  Tests should be enabled.
# FIXME: Removing of Carp::Clan shoud happen in %prep.
#        But tests will fail then.
# TODO:  Inform author about the namespace conflict with perl-Bit-Vector.
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Calc
Summary:	Date::Calc - Gregorian calendar date calculations
Summary(pl):	Modu³ Date::Calc - obliczaj±cy daty na podstawie kalendarza gregoriañskiego
Name:		perl-Date-Calc
Version:	5.3
Release:	2
License:	GPL/LGPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Bit-Vector >= 5.7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of a C library and a Perl module (which uses the
C library, internally) for all kinds of date calculations based on the
Gregorian calendar (the one used in all western countries today),
thereby complying with all relevant norms and standards:
ISO/R 2015-1971, DIN 1355 and, to some extent, ISO 8601 (where
applicable).

%description -l pl
Ten pakiet zawiera bibliotekê C i modu³ Perla (u¿ywaj±cy wewnêtrznie
tej biblioteki) do wszystkich rodzajów obliczeñ na datach bazuj±cych
na kalendarzu gregoriañskim (u¿ywanym we wszystkich zachodnich
pañstwach), zgodnie z normami i standardami: ISO/R 2015-1971, DIN 1355
i, do pewnego stopnia, ISO 8601.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

#%%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tools $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f GNU_{,L}GPL.txt Artistic.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{perl_vendorarch}/Date
%{perl_vendorarch}/Date/*.pm
%dir %{perl_vendorarch}/Date/Calc
%{perl_vendorarch}/Date/Calc/*.pm
%dir %{perl_vendorarch}/Date/Calendar
%{perl_vendorarch}/Date/Calendar/*.pm
%dir %{perl_vendorarch}/auto/Date
%dir %{perl_vendorarch}/auto/Date/Calc
%{perl_vendorarch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/Date*
%{_examplesdir}/%{name}-%{version}
