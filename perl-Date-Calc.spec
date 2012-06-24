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
Summary(cs):	Date::Calc - modul pro roz���en� a efektivn� po��t�n� s datem v Perlu
Summary(da):	Date::Calc - et modul for udvidet og effektiv datoberegning i Perl
Summary(de):	Date::Calc - ein Modul f�r erweiterte und leistungsstarke Datenberechnungen in Perl
Summary(es):	Date::Calc - m�dulo para los c�lculos de datos extendidos y eficientes en Perl
Summary(fr):	Date::Calc - module de calcul de date �tendu et efficace dans Perl
Summary(it):	Date::Calc - modulo per gestire in modo completo ed efficiente i calcoli delle date in Perl
Summary(ja):	Date::Calc - Perl��γ�ĥ���Ǹ�ΨŪ�����ջ��Фΰ٤Υ⥸�塼�롣
Summary(ko):	Date::Calc - Perl�� ����Ͽ� Ȯ��ǰ� ȿ�������� ��¥�� ����ϴµ� ���Ǵ� ���
Summary(pl):	Date::Calc - obliczanie daty na podstawie kalendarza gregoria�skiego
Summary(pt):	Date::Calc - um m�dulo para o c�lculo eficiente e extendido de datas em Perl
Summary(pt_BR):	Date::Calc - um m�dulo para o c�lculo eficiente e extendido de datas em Perl
Summary(sv):	Date::Calc - en modul f�r ut�kade och effektiva datumber�kningar i Perl
Summary(tr):	Date::Calc - Perl'de geni�letilmi� ve etkili tarih hesaplamalar� i�in bir mod�l
Summary(zh_CN):	Date::Calc - ���� Perl ����չ�ĺ���Ч�����ڼ����ģ�顣
Summary(zh_TW):	Date::Calc - �Ω� Perl �������P���Ĳv����ƭp�⪺�@�ӼҲաC
Name:		perl-Date-Calc
Version:	5.4
Release:	2
# same as perl (C library also LGPL)
License:	GPL v1+ or Artistic (C library also LGPL)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ae34972694127e8f1c9a2af1c24585b
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
Tato knihovna poskytuje r�zn� typy po��t�n� s datem zalo�en� na
gregori�nsk�m kalend��i (pou��van�m nyn� ve v�ech z�padn�ch zem�ch),
��m� vyhovuje v�em relevantn�m norm�m a standard�m: ISO/R 2015-1971,
DIN 1355 a do ur�it� m�ry ISO 8601 (kde to d�v� smysl).

%description -l da
Biblioteket laver alle slags datoberegninger baseret p� den
gregorianske kalender (den som bruges i alle vestlige lande i dag), og
f�lger derved alle relevante normer og standarder: ISO/R 2015-1971,
DIN 1355 og, i nogen udstr�kning, ISO 8601 (hvis relevant).

%description -l de
Die Bibliothek liefert jede Art der Datenberechnung auf der Grundlage
des gregorianischen Kalenders (der heute in allen westlichen L�ndern
verwendet wird) und entspricht damit allen relevanten Richtlinien und
Standards: ISO/R 2015-1971, DIN 1355 und, in gewissem Ma�e, ISO 8601
(wo g�ltig).

%description -l es
La librer�a proporciona todos los tipos de c�lculos de datos basados
en el calendario gregoriano (usado en todos los pa�ses del oeste hoy
en d�a), que cumple todas las normas y est�ndare relevantes: ISO/R
2015-1971, DIN 1355 and, to some extent, ISO 8601 (en los casos en los
que se pueda aplicar).

%description -l fr
La biblioth�que fournit toutes sortes de calculs de dates bas�s sur le
calendrier gr�gorien (celui qu'utilisent aujourd'hui tous les pays
europ�ens). Il est donc adapt� � toutes les normes et tous les
standards: ISO/R 2015-1971, DIN 1355 et dans une certaine mesure ISO
8601 (lorsqu'elle est applicable).

%description -l it
La libreria fornisce ogni sorta di calcolo delle date basandosi sul
calendario Gregoriano (utilizzato in tutti i paesi occidentali), in
conformit� con le norme e gli standard pi� appropriati: ISO/R
2015-1971, DIN 1355 e, anche ISO 8601 (se applicabile).

%description -l ko
�� ���̺귯���� (���� ���翡�� ���Ǵ�) �׷������¿� ����� ���
������ ��¥ ������ �����մϴ�. ���� ������ ���� ��� ���İ� ǥ����
�ؼ��մϴ�: ISO/R, 2015-1971, DIN 1355, �׸��� ISO 8601 (���� ������
���).

%description -l pl
Ten pakiet zawiera bibliotek� C i modu� Perla (u�ywaj�cy wewn�trznie
tej biblioteki) do wszystkich rodzaj�w oblicze� na datach bazuj�cych
na kalendarzu gregoria�skim (u�ywanym we wszystkich zachodnich
pa�stwach), zgodnie z normami i standardami: ISO/R 2015-1971, DIN 1355
i, do pewnego stopnia, ISO 8601.

%description -l pt
A biblioteca oferece todo o tipo de c�lculos de data com base no
calend�rio Gregoriano (o que � usado em todos os pa�ses ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo n�vel, a ISO 8601
(onde for aplic�vel).

%description -l pt_BR
A biblioteca oferece todo o tipo de c�lculos de data com base no
calend�rio Gregoriano (o que � usado em todos os pa�ses ocidentais nos
dias de hoje), estando desta forma em conformidade com todas as
normas: a ISO/R 2015-1971, a DIN 1355 e, a certo n�vel, a ISO 8601
(onde for aplic�vel).

%description -l sv
Biblioteket klarar alla sorters datumber�kningar baserade p� den
gregorianska kalendern (den som anv�nds i alla v�stl�nder idag), och
f�ljer d�rvid alla relavanta normer och standarder: ISO/R 2015-1971,
DIN 1355 och, i viss m�n, ISO 8601 (d�r den �r till�mplig).

%description -l zh_CN
�ÿ��ṩ�˸��ཨ���ڸ��и�������(����)�ϵ�
���ڼ��㡣������������صı�׼��ISO/R
2015-1971��DIN 1355 ��ĳ�̶ֳ��ϵ� ISO 8601
(������)��

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
