#
# TODO:  Tests should be enabled.
# FIXME: Removing of Carp::Clan shoud happen in %prep.
#        But tests will fail then.
# TODO:  Inform author about the namespace conflict with perl-Bit-Vector.
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Calc
Summary:	Date::Calc - Gregorian calendar date calculations.
Summary(pl):	Date::Calc - oblicza daty na podstawie kalendarza gregoriañskiego.
Name:		perl-Date-Calc
Version:	5.1
Release:	1
License:	GPL/LGPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Bit-Vector >= 5.7
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of a C library and a Perl module (which uses the
C library, internally) for all kinds of date calculations based on the
Gregorian calendar (the one used in all western countries today), thereby
complying with all relevant norms and standards: S<ISO/R 2015-1971>,
S<DIN 1355> and, to some extent, S<ISO 8601> (where applicable).

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%dir %{perl_sitearch}/Date
%{perl_sitearch}/Date/*.pm
%dir %{perl_sitearch}/Date/Calc
%{perl_sitearch}/Date/Calc/*.pm
%dir %{perl_sitearch}/Date/Calendar
%{perl_sitearch}/Date/Calendar/*.pm
%dir %{perl_sitearch}/auto/Date
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/Date*
%{_examplesdir}/%{name}-%{version}
