Summary:	C Prototype Utility
Summary(de):	C-Prototyp-Dienstprogramm
Summary(fr):	Utilitaire de prototypage C
Summary(pl):	Narz�dzia dla prototyp�w C
Summary(tr):	C prototip arac�
Name:		cproto
Version:	4.6
Release:	6
License:	Public Domain
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://ftp.oce.com/pub/cproto/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cproto generates function prototypes for functions defined in the
specified C source files to the standard output. The function
definitions may be in the old style or ANSI C style. Optionally,
cproto also outputs declarations for variables defined in the files.
If no file argument is given, cproto reads its input from the standard
input.

%description -l de
Cproto erzeugt Funktionsprototypen f�r in C-Quelldateien definierte
Funktionen f�r die Standardausgabe. Die Funktionsdefinitionen k�nnen
im alten oder ANSI-C-Format vorliegen. cproto kann auch Deklarationen
f�r in den Dateien definierten Variablen ausgeben. Wird kein
Dateiargument angegeben, liest cproto die Eingabe aus der
Standardeingabe.

%description -l fr
Cproto g�n�re des prototypes de fonction d�finies dans sources C
sp�cifi�es sur la sortie standard. Les fonctions d�fines peuvent �tre
en vieux style ou en style C ANSI. Optionnelement, cproto affiche
aussi les d�clarations pour les variables d�finies dans ces sources.
Si aucun argument ne lui est donn�, cproto lit ses entr�es depuis
l'entr�e standard.

%description -l pl
Cproto jest programem do generowania prototyp�w funkcji,
zdefiniowanych w plikach �r�d�owych C. Definicje funkcji mog� by�
zar�wno zgodne z ANSI C jak i ze starszymi. Cproto mo�e tak�e
dodatkowo tworzy� wynik deklaracji dla r�nych zmiennych
zdefiniowanych w pliku. Je�eli argumentem nie jest plik, cproto
pobiera argumenty ze standardowego wej�cia (stdin).

%description -l tr
Cproto, verilen C kaynak dosyalar�nda tan�mlanm�� fonksiyonlar i�in
standart ��kt�da prototipler olu�turur. �stenirse dosyalardaki
de�i�ken tan�mlamalar�n� da ��kartabilir. Programa hi�bir arg�man
verilmemi�se, cproto girdi olarak standart giri�ten bilgi okur.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CPP="/lib/cpp"
export CPP
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cproto
%{_mandir}/man1/*
