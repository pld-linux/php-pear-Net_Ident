%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Ident
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - identification protocol implementation
Summary(pl):	%{_pearname} - implementacja protoko³u identyfikacji
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	69dd46d5b0a63af10ebbd1d7efadf86e
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Net_Ident/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Ident implements Identification Protocol according to
RFC 1413. The Identification Protocol (a.k.a., "ident", a.k.a., "the
Ident Protocol") provides a means to determine the identity of a user
of a particular TCP connection. Given a TCP port number pair, it
returns a character string which identifies the owner of that
connection on the server's system.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa PEAR::Net_Ident to implementacja protoko³u identyfikacji wed³ug
RFC 1413. Protokó³ identyfikacji (Identification Protocol, znany tak¿e
jako ident lub Ident Protocol) daje mo¿liwo¶æ okre¶lenia, kto jest
u¿ytkownikiem danego po³±czenia TCP. Po podaniu pary portów TCP zwraca
³añcuch znaków identyfikuj±cy w³a¶ciciela tego po³±czenia na systemie
serwera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
