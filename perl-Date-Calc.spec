#
# TODO:  Tests should be enabled.
# FIXME: Removing of Carp::Clan shoud happen in %%prep.
#        But tests will fail then.
# TODO:  Inform author about the namespace conflict with perl-Bit-Vector.
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Calc
Summary:	Date::Calc - Gregorian calendar date calculations
Summary(cs.UTF-8):	Date::Calc - modul pro rozšířené a efektivní počítání s datem v Perlu
Summary(da.UTF-8):	Date::Calc - et modul for udvidet og effektiv datoberegning i Perl
Summary(de.UTF-8):	Date::Calc - ein Modul für erweiterte und leistungsstarke Datenberechnungen in Perl
Summary(es.UTF-8):	Date::Calc - módulo para los cálculos de datos extendidos y eficientes en Perl
Summary(fr.UTF-8):	Date::Calc - module de calcul de date étendu et efficace dans Perl
Summary(it.UTF-8):	Date::Calc - modulo per gestire in modo completo ed efficiente i calcoli delle date in Perl
Summary(ja.UTF-8):	Date::Calc - Perl内の拡張型で効率的な日付算出の為のモジュール。
Summary(ko.UTF-8):	Date::Calc - Perl을 사용하여 확장되고 효율적으로 날짜를 계산하는데 사용되는 모듈
Summary(pl.UTF-8):	Date::Calc - obliczanie daty na podstawie kalendarza gregoriańskiego
Summary(pt.UTF-8):	Date::Calc - um módulo para o cálculo eficiente e extendido de datas em Perl
Summary(pt_BR.UTF-8):	Date::Calc - um módulo para o cálculo eficiente e extendido de datas em Perl
Summary(sv.UTF-8):	Date::Calc - en modul för utökade och effektiva datumberäkningar i Perl
Summary(tr.UTF-8):	Date::Calc - Perl'de genişletilmiş ve etkili tarih hesaplamaları için bir modül
Summary(zh_CN.UTF-8):	Date::Calc - 用于 Perl 中扩展的和有效的日期计算的模块。
Summary(zh_TW.UTF-8):	Date::Calc - 用於 Perl 中延伸與有效率之資料計算的一個模組。
Name:		perl-Date-Calc
Version:	6.3
Release:	2
# same as perl (C library also LGPL)
License:	GPL v1+ or Artistic (C library also LGPL)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Date/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b64555b7051c1beb6b61daead2d01b3
URL:		http://search.cpan.org/dist/Date-Calc/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Bit-Vector >= 7.1
BuildRequires:	perl-Carp-Clan >= 5.3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of a C library and a Perl module (which uses the
C library, internally) for all kinds of date calculations based on the
Gregorian calendar (the one used in all western countries today),
thereby complying with all relevant norms and standards: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (where applicable).

%description -l cs.UTF-8
Tato knihovna poskytuje různé typy počítání s datem založené na
gregoriánském kalendáři (používaném nyní ve všech západních zemích),
čímž vyhovuje všem relevantním normám a standardům: ISO/R 2015-1971,
DIN 1355 a do určité míry ISO 8601 (kde to dává smysl).

%description -l da.UTF-8
Biblioteket laver alle slags datoberegninger baseret på den
gregorianske kalender (den som bruges i alle vestlige lande i dag), og
følger derved alle relevante normer og standarder: ISO/R 2015-1971,
DIN 1355 og, i nogen udstrækning, ISO 8601 (hvis relevant).

%description -l de.UTF-8
Die Bibliothek liefert jede Art der Datenberechnung auf der Grundlage
des gregorianischen Kalenders (der heute in allen westlichen Ländern
verwendet wird) und entspricht damit allen relevanten Richtlinien und
Standards: ISO/R 2015-1971, DIN 1355 und, in gewissem Maße, ISO 8601
(wo gültig).

%description -l es.UTF-8
La librería proporciona todos los tipos de cálculos de datos basados
en el calendario gregoriano (usado en todos los países del oeste hoy
en día), que cumple todas las normas y estándare relevantes: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (en los casos en los
que se pueda aplicar).

%description -l fr.UTF-8
La bibliothèque fournit toutes sortes de calculs de dates basés sur le
calendrier grégorien (celui qu'utilisent aujourd'hui tous les pays
européens). Il est donc adapté à toutes les normes et tous les
standards: ISO/R 2015-1971, DIN 1355 et dans une certaine mesure ISO
8601 (lorsqu'elle est applicable).

%description -l it.UTF-8
La libreria fornisce ogni sorta di calcolo delle date basandosi sul
calendario Gregoriano (utilizzato in tutti i paesi occidentali), in
conformità con le norme e gli standard più appropriati: ISO/R
2015-1971, DIN 1355 e, anche ISO 8601 (se applicabile).

%description -l ko.UTF-8
이 라이브러리는 (현재 서양에서 사용되는) 그레고리오력에 기반한 모든
종류의 날짜 계산법을 제공합니다. 따라서 다음과 같은 모든 형식과 표준을
준수합니다: ISO/R, 2015-1971, DIN 1355, 그리고 ISO 8601 (적용 가능한
경우).

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę C i moduł Perla (używający wewnętrznie
tej biblioteki) do wszystkich rodzajów obliczeń na datach bazujących
na kalendarzu gregoriańskim (używanym we wszystkich zachodnich
państwach), zgodnie z normami i standardami: ISO/R 2015-1971, DIN 1355
i, do pewnego stopnia, ISO 8601.

%description -l pt.UTF-8
A biblioteca oferece todo o tipo de cálculos de data com base no
calendário Gregoriano (o que é usado em todos os países ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo nível, a ISO 8601
(onde for aplicável).

%description -l pt_BR.UTF-8
A biblioteca oferece todo o tipo de cálculos de data com base no
calendário Gregoriano (o que é usado em todos os países ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo nível, a ISO 8601
(onde for aplicável).

%description -l sv.UTF-8
Biblioteket klarar alla sorters datumberäkningar baserade på den
gregorianska kalendern (den som används i alla västländer idag), och
följer därvid alla relavanta normer och standarder: ISO/R 2015-1971,
DIN 1355 och, i viss mån, ISO 8601 (där den är tillämplig).

%description -l zh_CN.UTF-8
该库提供了各类建立在格列高里日历(公历)上的
日期计算。它符合所有相关的标准：ISO/R
2015-1971、DIN 1355 和某种程度上的 ISO 8601
(若适用)。

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
%doc *.txt
%dir %{perl_vendorlib}/Date
%{perl_vendorlib}/Date/*.pm
%dir %{perl_vendorlib}/Date/Calc
%{perl_vendorlib}/Date/Calc/*.pm
%dir %{perl_vendorlib}/Date/Calendar
%{perl_vendorlib}/Date/Calendar/*.pm
%{_mandir}/man3/*
