%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Ident
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - identification protocol implementation
Summary(pl):	%{_pearname} - implementacja protoko³u identyfikacji
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dc2b3e0179c485816c171f8822ff0381
URL:		http://pear.php.net/package/Net_Ident/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Net_Ident to implementacja protoko³u identyfikacji wed³ug
RFC 1413. Protokó³ identyfikacji (Identification Protocol, znany tak¿e
jako ident lub Ident Protocol) daje mo¿liwo¶æ okre¶lenia, kto jest
u¿ytkownikiem danego po³±czenia TCP. Po podaniu pary portów TCP zwraca
³añcuch znaków identyfikuj±cy w³a¶ciciela tego po³±czenia na systemie
serwera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
