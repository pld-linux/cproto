Summary:	C Prototype Utility
Summary(de):	C-Prototyp-Dienstprogramm
Summary(fr):	Utilitaire de prototypage C.
Summary(pl):	Narzêdzia dla prototypów C
Summary(tr):	C prototip aracý
Name:		cproto
Version:	4.6
Release:	3
Copyright:	Public Domain
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://ftp.oce.com/pub/cproto/%{name}-%{version}.tar.gz
Patch0:		cproto.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Cproto generates function prototypes for functions defined in the specified
C source files to the standard output.  The function definitions may be in
the old style or ANSI C style.  Optionally, cproto also outputs declarations
for variables defined in the files. If no file argument is given, cproto
reads its input from the standard input.

%description -l de
Cproto erzeugt Funktionsprototypen für in C-Quelldateien definierte
Funktionen für die Standardausgabe. Die Funktionsdefinitionen können im
alten oder ANSI-C-Format vorliegen. cproto kann auch Deklarationen für in
den Dateien definierten Variablen ausgeben. Wird kein Dateiargument
angegeben, liest cproto die Eingabe aus der Standardeingabe.

%description -l fr
Cproto génére des prototypes de fonction définies dans sources C spécifiées
sur la sortie standard. Les fonctions défines peuvent être en vieux style ou
en style C ANSI. Optionnelement, cproto affiche aussi les déclarations pour
les variables définies dans ces sources. Si aucun argument ne lui est donné,
cproto lit ses entrées depuis l'entrée standard.

%description -l pl
Cproto jest programem do generowania prototypów funkcji, zdefiniowanych w
plikach ¼ród³owtch C. Definicje funkcji mog± byæ zarówno zgodne z ANSI C jak
i ze starszymi. Cproto mo¿e tak¿e dodatkowo tworzyæ wynik deklaracji dla
ro¿nych zmiennych zdefiniowanych w pliku. Je¿eli argumentem nie jest plik,
cproto pobiera argumenty ze standardowego wej¶cia (stdin).

%description -l tr
Cproto, verilen C kaynak dosyalarýnda tanýmlanmýþ fonksiyonlar için standart
çýktýda prototipler oluþturur. Ýstenirse dosyalardaki deðiþken
tanýmlamalarýný da çýkartabilir. Programa hiçbir argüman verilmemiþse,
cproto girdi olarak standart giriþten bilgi okur.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cproto
%{_mandir}/man1/*

%changelog
* Fri Jun  4 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.6-3]
- new patch for cproto (from RH 6),
- added using %%configure macro in %build.

* Mon Jun 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.4-9]
- major changes,
- rewrote wrong spec file.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
