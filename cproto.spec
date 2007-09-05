Summary:	C Prototype Utility
Summary(de.UTF-8):	C-Prototyp-Dienstprogramm
Summary(es.UTF-8):	Utilitario de prototipos C
Summary(fr.UTF-8):	Utilitaire de prototypage C
Summary(pl.UTF-8):	Narzędzia do prototypów C
Summary(pt_BR.UTF-8):	Utilitário de prototipação C
Summary(ru.UTF-8):	Генерирует прототипы функций и декларации переменных из кода на C
Summary(tr.UTF-8):	C prototip aracı
Summary(uk.UTF-8):	Генерує прототипи функцій та декларації змінних з коду на C
Name:		cproto
Version:	4.6
Release:	17
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

%description -l de.UTF-8
Cproto erzeugt Funktionsprototypen für in C-Quelldateien definierte
Funktionen für die Standardausgabe. Die Funktionsdefinitionen können
im alten oder ANSI-C-Format vorliegen. cproto kann auch Deklarationen
für in den Dateien definierten Variablen ausgeben. Wird kein
Dateiargument angegeben, liest cproto die Eingabe aus der
Standardeingabe.

%description -l es.UTF-8
cproto crea prototipos de función para funciones definidas en los
archivos fuente C para salida padrón. Las definiciones de las
funciones pueden ser en el antiguo estilo o en el estilo ANSI C.
Opcionalmente, cproto también produce declaraciones para variables
definidas en los archivos. Si no se ofrece argumento de archivo,
cproto lee de la entrada padrón.

%description -l fr.UTF-8
Cproto génére des prototypes de fonction définies dans sources C
spécifiées sur la sortie standard. Les fonctions défines peuvent être
en vieux style ou en style C ANSI. Optionnelement, cproto affiche
aussi les déclarations pour les variables définies dans ces sources.
Si aucun argument ne lui est donné, cproto lit ses entrées depuis
l'entrée standard.

%description -l pl.UTF-8
Cproto jest programem do generowania prototypów funkcji,
zdefiniowanych w plikach źródłowych C. Definicje funkcji mogą być
zarówno zgodne z ANSI C jak i ze starszymi. Cproto może także
dodatkowo tworzyć wynik deklaracji dla różnych zmiennych
zdefiniowanych w pliku. Jeżeli argumentem nie jest plik, cproto
pobiera argumenty ze standardowego wejścia (stdin).

%description -l pt_BR.UTF-8
O cproto gera protótipos de função para funções definidas nos arquivos
fonte C para saída padrão. As definições das funções podem ser no
velho estilo ou no estilo ANSI C. Opcionalmente, cproto também produz
declarações para variáveis definidas nos arquivos. Se não é fornecido
argumento de arquivo, cproto lê da entrada padrão.

%description -l ru.UTF-8
Cproto генерирует прототипы для функций, определенных в указанном
исходном файле на C и выводит их на стандартный вывод. Функции могут
быть определены как в "старом", так и в стиле ANSI C. Опционально
cproto также выводит декларации переменных, определенных в этих
файлах. Если файл(ы) не заданы, cproto берет данные со стандартного
ввода.

%description -l uk.UTF-8
Cproto генерує прототипи для функцій, визначених у заданому вихідному
файлі на C та виводить їх на стандартний вивід. Функції можуть
визначатись як у "старому" стилі, так і в стилі ANSI C. Опціонально
cproto також виводить декларації змінних, визначених в цих файлах.
Якщо файл(и) не задані, cproto бере дані зі стандартного вводу.

%description -l tr.UTF-8
Cproto, verilen C kaynak dosyalarında tanımlanmış fonksiyonlar için
standart çıktıda prototipler oluşturur. İstenirse dosyalardaki
değişken tanımlamalarını da çıkartabilir. Programa hiçbir argüman
verilmemişse, cproto girdi olarak standart girişten bilgi okur.

%description -l ru.UTF-8
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
