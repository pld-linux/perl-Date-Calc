%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Calc
Summary:	Date::Calc perl module
Summary(pl):	Modu� perla Date::Calc
Name:		perl-Date-Calc
Version:	5.0
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Calc - Gregorian calendar date calculations.

%description -l pl
Date::Calc - oblicza daty na podstawie kalendarza gregoria�skiego.

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

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Date/Calc.pm
%{perl_sitearch}/Carp/Clan.pm
%dir %{perl_sitearch}/auto/Date/Calc
%{perl_sitearch}/auto/Date/Calc/Calc.bs
%attr(755,root,root) %{perl_sitearch}/auto/Date/Calc/Calc.so
%{_mandir}/man3/Date*
%{_examplesdir}/%{name}-%{version}
