%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Calc
Summary:	Date::Calc Perl module
Summary(cs):	Modul Date::Calc pro Perl
Summary(da):	Perlmodul Date::Calc
Summary(de):	Date::Calc Perl Modul
Summary(es):	Módulo de Perl Date::Calc
Summary(fr):	Module Perl Date::Calc
Summary(it):	Modulo di Perl Date::Calc
Summary(ja):	Date::Calc Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Date::Calc ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Date::Calc
Summary(pl):	Modu³ Perla Date::Calc
Summary(pt):	Módulo de Perl Date::Calc
Summary(pt_BR):	Módulo Perl Date::Calc
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Date::Calc
Summary(sv):	Date::Calc Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Date::Calc
Summary(zh_CN):	Date::Calc Perl Ä£¿é
Name:		perl-Date-Calc
Version:	5.0
Release:	9
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
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/Date*
%{_examplesdir}/%{name}-%{version}
