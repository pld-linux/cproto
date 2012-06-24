Summary:	C Prototype Utility
Summary(de):	C-Prototyp-Dienstprogramm
Summary(es):	Utilitario de prototipos C
Summary(fr):	Utilitaire de prototypage C
Summary(pl):	Narz�dzia do prototyp�w C
Summary(pt_BR):	Utilit�rio de prototipa��o C
Summary(ru):	���������� ��������� ������� � ���������� ���������� �� ���� �� C
Summary(tr):	C prototip arac�
Summary(uk):	�����դ ��������� ����æ� �� �������æ� �ͦ���� � ���� �� C
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
Cproto erzeugt Funktionsprototypen f�r in C-Quelldateien definierte
Funktionen f�r die Standardausgabe. Die Funktionsdefinitionen k�nnen
im alten oder ANSI-C-Format vorliegen. cproto kann auch Deklarationen
f�r in den Dateien definierten Variablen ausgeben. Wird kein
Dateiargument angegeben, liest cproto die Eingabe aus der
Standardeingabe.

%description -l es
cproto crea prototipos de funci�n para funciones definidas en los
archivos fuente C para salida padr�n. Las definiciones de las
funciones pueden ser en el antiguo estilo o en el estilo ANSI C.
Opcionalmente, cproto tambi�n produce declaraciones para variables
definidas en los archivos. Si no se ofrece argumento de archivo,
cproto lee de la entrada padr�n.

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

%description -l pt_BR
O cproto gera prot�tipos de fun��o para fun��es definidas nos arquivos
fonte C para sa�da padr�o. As defini��es das fun��es podem ser no
velho estilo ou no estilo ANSI C. Opcionalmente, cproto tamb�m produz
declara��es para vari�veis definidas nos arquivos. Se n�o � fornecido
argumento de arquivo, cproto l� da entrada padr�o.

%description -l ru
Cproto ���������� ��������� ��� �������, ������������ � ���������
�������� ����� �� C � ������� �� �� ����������� �����. ������� �����
���� ���������� ��� � "������", ��� � � ����� ANSI C. �����������
cproto ����� ������� ���������� ����������, ������������ � ����
������. ���� ����(�) �� ������, cproto ����� ������ �� ������������
�����.

%description -l uk
Cproto �����դ ��������� ��� ����æ�, ���������� � �������� ��Ȧ�����
���̦ �� C �� �������� �� �� ����������� ��צ�. ����æ� ������
����������� �� � "�������" ���̦, ��� � � ���̦ ANSI C. ��æ�������
cproto ����� �������� �������æ� �ͦ����, ���������� � ��� ������.
���� ����(�) �� ����Φ, cproto ���� ��Φ ڦ ������������ �����.

%description -l tr
Cproto, verilen C kaynak dosyalar�nda tan�mlanm�� fonksiyonlar i�in
standart ��kt�da prototipler olu�turur. �stenirse dosyalardaki
de�i�ken tan�mlamalar�n� da ��kartabilir. Programa hi�bir arg�man
verilmemi�se, cproto girdi olarak standart giri�ten bilgi okur.

%description -l ru
Cproto ���������� ��������� ��� �������, ������������ � ���������
�������� ����� �� C � ������� �� �� ����������� �����. ������� �����
���� ���������� ��� � "������", ��� � � ����� ANSI C. �����������
cproto ����� ������� ���������� ����������, ������������ � ����
������. ���� ����(�) �� ������, cproto ����� ������ �� ������������
�����.

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
