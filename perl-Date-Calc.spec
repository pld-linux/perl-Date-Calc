%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Calc
Summary:	Date::Calc perl module
Summary(pl):	Modu³ perla Date::Calc
Name:		perl-Date-Calc
Version:	5.0
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Bit-Vector >= 5.7
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Calc - Gregorian calendar date calculations.

%description -l pl
Date::Calc - oblicza daty na podstawie kalendarza gregoriañskiego.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{perl_sitearch}/Date/*.pm
%dir %{perl_sitearch}/Date/Calc
%{perl_sitearch}/Date/Calc/*.pm
%dir %{perl_sitearch}/Date/Calendar
%{perl_sitearch}/Date/Calendar/*.pm
%{perl_sitearch}/Carp/Clan.pm
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
