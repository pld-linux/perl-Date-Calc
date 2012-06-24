%include	/usr/lib/rpm/macros.perl
Summary:	Date-Calc perl module
Summary(pl):	Modu� perla Date-Calc
Name:		perl-Date-Calc
Version:	4.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/Date-Calc-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Date-Calc - Gregorian calendar date calculations.

%description -l pl
Date-Calc - oblicza daty na podstawie kalendarza gregoria�skiego.

%prep
%setup -q -n Date-Calc-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}
cp -a tools 	   $RPM_BUILD_ROOT/usr/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Date/Calc/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Date/Calc
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES.txt,CREDITS.txt,EXAMPLES.txt,README.txt,TOOLS.txt}.gz

%{perl_sitearch}/Date/Calc.pm
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/.packlist
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so

%{_mandir}/man3/*

/usr/src/examples/%{name}
