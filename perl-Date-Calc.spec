%include	/usr/lib/rpm/macros.perl
Summary:	Date-Calc perl module
Summary(pl):	Modu� perla Date-Calc
Name:		perl-Date-Calc
Version:	4.3
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/Date-Calc-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date-Calc - Gregorian calendar date calculations.

%description -l pl
Date-Calc - oblicza daty na podstawie kalendarza gregoria�skiego.

%prep
%setup -q -n Date-Calc-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
