#
# TODO:  Tests should be enabled.
# FIXME: Removing of Carp::Clan shoud happen in %prep.
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
Summary(cs):	Date::Calc - modul pro roz¹íøené a efektivní poèítání s datem v Perlu
Summary(da):	Date::Calc - et modul for udvidet og effektiv datoberegning i Perl
Summary(de):	Date::Calc - ein Modul für erweiterte und leistungsstarke Datenberechnungen in Perl
Summary(es):	Date::Calc - módulo para los cálculos de datos extendidos y eficientes en Perl
Summary(fr):	Date::Calc - module de calcul de date étendu et efficace dans Perl
Summary(it):	Date::Calc - modulo per gestire in modo completo ed efficiente i calcoli delle date in Perl
Summary(ja):	Date::Calc - PerlÆâ¤Î³ÈÄ¥·¿¤Ç¸úÎ¨Åª¤ÊÆüÉÕ»»½Ð¤Î°Ù¤Î¥â¥¸¥å¡¼¥ë¡£
Summary(ko):	Date::Calc - PerlÀ» »ç¿ëÇÏ¿© È®ÀåµÇ°í È¿À²ÀûÀ¸·Î ³¯Â¥¸¦ °è»êÇÏ´Âµ¥ »ç¿ëµÇ´Â ¸ðµâ
Summary(pl):	Date::Calc - obliczanie daty na podstawie kalendarza gregoriañskiego
Summary(pt):	Date::Calc - um módulo para o cálculo eficiente e extendido de datas em Perl
Summary(pt_BR):	Date::Calc - um módulo para o cálculo eficiente e extendido de datas em Perl
Summary(sv):	Date::Calc - en modul för utökade och effektiva datumberäkningar i Perl
Summary(tr):	Date::Calc - Perl'de geniþletilmiþ ve etkili tarih hesaplamalarý için bir modül
Summary(zh_CN):	Date::Calc - ÓÃÓÚ Perl ÖÐÀ©Õ¹µÄºÍÓÐÐ§µÄÈÕÆÚ¼ÆËãµÄÄ£¿é¡£
Summary(zh_TW):	Date::Calc - ¥Î©ó Perl ¤¤©µ¦ù»P¦³®Ä²v¤§¸ê®Æ­pºâªº¤@­Ó¼Ò²Õ¡C
Name:		perl-Date-Calc
Version:	5.3
Release:	4
# same as perl (C library also LGPL)
License:	GPL v1+ or Artistic (C library also LGPL)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0548d1238b026920986c27956524a5d5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Bit-Vector >= 5.7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of a C library and a Perl module (which uses the
C library, internally) for all kinds of date calculations based on the
Gregorian calendar (the one used in all western countries today),
thereby complying with all relevant norms and standards: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (where applicable).

%description -l cs
Tato knihovna poskytuje rùzné typy poèítání s datem zalo¾ené na
gregoriánském kalendáøi (pou¾ívaném nyní ve v¹ech západních zemích),
èím¾ vyhovuje v¹em relevantním normám a standardùm: ISO/R 2015-1971,
DIN 1355 a do urèité míry ISO 8601 (kde to dává smysl).

%description -l da
Biblioteket laver alle slags datoberegninger baseret på den
gregorianske kalender (den som bruges i alle vestlige lande i dag), og
følger derved alle relevante normer og standarder: ISO/R 2015-1971,
DIN 1355 og, i nogen udstrækning, ISO 8601 (hvis relevant).

%description -l de
Die Bibliothek liefert jede Art der Datenberechnung auf der Grundlage
des gregorianischen Kalenders (der heute in allen westlichen Ländern
verwendet wird) und entspricht damit allen relevanten Richtlinien und
Standards: ISO/R 2015-1971, DIN 1355 und, in gewissem Maße, ISO 8601
(wo gültig).

%description -l es
La librería proporciona todos los tipos de cálculos de datos basados
en el calendario gregoriano (usado en todos los países del oeste hoy
en día), que cumple todas las normas y estándare relevantes: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (en los casos en los
que se pueda aplicar).

%description -l fr
La bibliothèque fournit toutes sortes de calculs de dates basés sur le
calendrier grégorien (celui qu'utilisent aujourd'hui tous les pays
européens). Il est donc adapté à toutes les normes et tous les
standards: ISO/R 2015-1971, DIN 1355 et dans une certaine mesure ISO
8601 (lorsqu'elle est applicable).

%description -l it
La libreria fornisce ogni sorta di calcolo delle date basandosi sul
calendario Gregoriano (utilizzato in tutti i paesi occidentali), in
conformità con le norme e gli standard più appropriati: ISO/R
2015-1971, DIN 1355 e, anche ISO 8601 (se applicabile).

%description -l ko
ÀÌ ¶óÀÌºê·¯¸®´Â (ÇöÀç ¼­¾ç¿¡¼­ »ç¿ëµÇ´Â) ±×·¹°í¸®¿À·Â¿¡ ±â¹ÝÇÑ ¸ðµç
Á¾·ùÀÇ ³¯Â¥ °è»ê¹ýÀ» Á¦°øÇÕ´Ï´Ù. µû¶ó¼­ ´ÙÀ½°ú °°Àº ¸ðµç Çü½Ä°ú Ç¥ÁØÀ»
ÁØ¼öÇÕ´Ï´Ù: ISO/R, 2015-1971, DIN 1355, ±×¸®°í ISO 8601 (Àû¿ë °¡´ÉÇÑ
°æ¿ì).

%description -l pl
Ten pakiet zawiera bibliotekê C i modu³ Perla (u¿ywaj±cy wewnêtrznie
tej biblioteki) do wszystkich rodzajów obliczeñ na datach bazuj±cych
na kalendarzu gregoriañskim (u¿ywanym we wszystkich zachodnich
pañstwach), zgodnie z normami i standardami: ISO/R 2015-1971, DIN 1355
i, do pewnego stopnia, ISO 8601.

%description -l pt
A biblioteca oferece todo o tipo de cálculos de data com base no
calendário Gregoriano (o que é usado em todos os países ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo nível, a ISO 8601
(onde for aplicável).

%description -l pt_BR
A biblioteca oferece todo o tipo de cálculos de data com base no
calendário Gregoriano (o que é usado em todos os países ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo nível, a ISO 8601
(onde for aplicável).

%description -l sv
Biblioteket klarar alla sorters datumberäkningar baserade på den
gregorianska kalendern (den som används i alla västländer idag), och
följer därvid alla relavanta normer och standarder: ISO/R 2015-1971,
DIN 1355 och, i viss mån, ISO 8601 (där den är tillämplig).

%description -l zh_CN
¸Ã¿âÌá¹©ÁË¸÷Àà½¨Á¢ÔÚ¸ñÁÐ¸ßÀïÈÕÀú(¹«Àú)ÉÏµÄ
ÈÕÆÚ¼ÆËã¡£Ëü·ûºÏËùÓÐÏà¹ØµÄ±ê×¼£ºISO/R
2015-1971¡¢DIN 1355 ºÍÄ³ÖÖ³Ì¶ÈÉÏµÄ ISO 8601
(ÈôÊÊÓÃ)¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
