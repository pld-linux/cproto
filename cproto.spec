Summary:	C Prototype Utility
Summary(de):	C-Prototyp-Dienstprogramm
Summary(es):	Utilitario de prototipos C
Summary(fr):	Utilitaire de prototypage C
Summary(pl):	NarzЙdzia do prototypСw C
Summary(pt_BR):	UtilitАrio de prototipaГЦo C
Summary(ru):	Генерирует прототипы функций и декларации переменных из кода на C
Summary(tr):	C prototip aracЩ
Summary(uk):	Генеру╓ прототипи функц╕й та декларац╕╖ зм╕нних з коду на C
Name:		cproto
Version:	4.6
Release:	16
License:	Public Domain
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/cproto/%{name}-%{version}.tar.gz
# Source0-md5:	5968d18e9508b2892471e6ef16e140e3
Patch0:		%{name}.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-varargs.patch
URL:		http://cproto.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cproto generates function prototypes for functions defined in the
specified C source files to the standard output. The function
definitions may be in the old style or ANSI C style. Optionally,
cproto also outputs declarations for variables defined in the files.
If no file argument is given, cproto reads its input from the standard
input.

%description -l de
Cproto erzeugt Funktionsprototypen fЭr in C-Quelldateien definierte
Funktionen fЭr die Standardausgabe. Die Funktionsdefinitionen kЖnnen
im alten oder ANSI-C-Format vorliegen. cproto kann auch Deklarationen
fЭr in den Dateien definierten Variablen ausgeben. Wird kein
Dateiargument angegeben, liest cproto die Eingabe aus der
Standardeingabe.

%description -l es
cproto crea prototipos de funciСn para funciones definidas en los
archivos fuente C para salida padrСn. Las definiciones de las
funciones pueden ser en el antiguo estilo o en el estilo ANSI C.
Opcionalmente, cproto tambiИn produce declaraciones para variables
definidas en los archivos. Si no se ofrece argumento de archivo,
cproto lee de la entrada padrСn.

%description -l fr
Cproto gИnИre des prototypes de fonction dИfinies dans sources C
spИcifiИes sur la sortie standard. Les fonctions dИfines peuvent Йtre
en vieux style ou en style C ANSI. Optionnelement, cproto affiche
aussi les dИclarations pour les variables dИfinies dans ces sources.
Si aucun argument ne lui est donnИ, cproto lit ses entrИes depuis
l'entrИe standard.

%description -l pl
Cproto jest programem do generowania prototypСw funkcji,
zdefiniowanych w plikach ╪rСdЁowych C. Definicje funkcji mog╠ byФ
zarСwno zgodne z ANSI C jak i ze starszymi. Cproto mo©e tak©e
dodatkowo tworzyФ wynik deklaracji dla rС©nych zmiennych
zdefiniowanych w pliku. Je©eli argumentem nie jest plik, cproto
pobiera argumenty ze standardowego wej╤cia (stdin).

%description -l pt_BR
O cproto gera protСtipos de funГЦo para funГУes definidas nos arquivos
fonte C para saМda padrЦo. As definiГУes das funГУes podem ser no
velho estilo ou no estilo ANSI C. Opcionalmente, cproto tambИm produz
declaraГУes para variАveis definidas nos arquivos. Se nЦo И fornecido
argumento de arquivo, cproto lЙ da entrada padrЦo.

%description -l ru
Cproto генерирует прототипы для функций, определенных в указанном
исходном файле на C и выводит их на стандартный вывод. Функции могут
быть определены как в "старом", так и в стиле ANSI C. Опционально
cproto также выводит декларации переменных, определенных в этих
файлах. Если файл(ы) не заданы, cproto берет данные со стандартного
ввода.

%description -l uk
Cproto генеру╓ прототипи для функц╕й, визначених у заданому вих╕дному
файл╕ на C та виводить ╖х на стандартний вив╕д. Функц╕╖ можуть
визначатись як у "старому" стил╕, так ╕ в стил╕ ANSI C. Опц╕онально
cproto також виводить декларац╕╖ зм╕нних, визначених в цих файлах.
Якщо файл(и) не задан╕, cproto бере дан╕ з╕ стандартного вводу.

%description -l tr
Cproto, verilen C kaynak dosyalarЩnda tanЩmlanmЩЧ fonksiyonlar iГin
standart ГЩktЩda prototipler oluЧturur. щstenirse dosyalardaki
deПiЧken tanЩmlamalarЩnЩ da ГЩkartabilir. Programa hiГbir argЭman
verilmemiЧse, cproto girdi olarak standart giriЧten bilgi okur.

%description -l ru
Cproto генерирует прототипы для функций, определенных в указанном
исходном файле на C и выводит их на стандартный вывод. Функции могут
быть определены как в "старом", так и в стиле ANSI C. Опционально
cproto также выводит декларации переменных, определенных в этих
файлах. Если файл(ы) не заданы, cproto берет данные со стандартного
ввода.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoconf}
%configure \
	CPPFLAGS="-DYYSTYPE=YYSTYPE"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/cproto
%{_mandir}/man1/*
