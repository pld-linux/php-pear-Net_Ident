%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Ident
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - identification protocol implementation
Summary(pl.UTF-8):	%{_pearname} - implementacja protokołu identyfikacji
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

%description -l pl.UTF-8
Klasa PEAR::Net_Ident to implementacja protokołu identyfikacji według
RFC 1413. Protokół identyfikacji (Identification Protocol, znany także
jako ident lub Ident Protocol) daje możliwość określenia, kto jest
użytkownikiem danego połączenia TCP. Po podaniu pary portów TCP zwraca
łańcuch znaków identyfikujący właściciela tego połączenia na systemie
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
