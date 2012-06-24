%define	pdir	Date
%define	pnam	Calc
%include	/usr/lib/rpm/macros.perl
Summary:	Date-Calc perl module
Summary(pl):	Modu� perla Date-Calc
Name:		perl-Date-Calc
Version:	5.0
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date-Calc - Gregorian calendar date calculations.

%description -l pl
Date-Calc - oblicza daty na podstawie kalendarza gregoria�skiego.

%prep
%setup -q -n Date-Calc-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tools $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Date/Calc.pm
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/Date*
%{_examplesdir}/%{name}-%{version}
