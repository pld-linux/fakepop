Summary:	Fake POP3 daemon, delivers same messages to all users
Summary(pl.UTF-8):	Fałszywy demon POP3, dostarczający te same wiadomości do wszystkich
Name:		fakepop
Version:	8
Release:	0.1
License:	GPL
Group:		Networking/Daemons/POP3
Source0:	http://vztech.com.br/public/software/fakepop/%{name}-src-%{version}.tar.gz
# Source0-md5:	9872ab86c626e44486ffd6016176713c
URL:		http://vztech.com.br/public/software/fakepop/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
Provides:	pop3daemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fakepop is a fake POP3 daemon. It returns always the same messages to
all users, it does not care about usernames and passwords. All
user/pass combinations are accepted.

The main purpose of fakepop is to advice users that your server only
accepts pop3-ssl and they have wrongly configured pop3 without SSL.
You can customize messages in /etc/fakepop/ directory to teach your
users how they should configure their mail clients to use pop3-ssl
instead of pop3.

%description -l pl.UTF-8
fakepop to fałszywy demon POP3. Zwraca wszystkim użytkownikom zawsze
te same wiadomości, niezależnie od nazw użytkowników i haseł.
Wszystkie kombinacje nazw użytkownika i haseł są przyjmowane.

Głównym celem fakepop jest doradzenie użytkownikom, że serwer
przyjmuje wyłącznie połączenia pop3-ssl, a oni mają błędnie
skonfigurowane pop3 bez SSL. Komunikaty można zmienić w katalogu
/etc/fakepop/, aby pouczyć użytkowników, jak powinni skonfigurować
swoje programy pocztowe do używania pop3-ssl zamiast pop3.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE `pkg-config --cflags glib-2.0`"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/fakepop
install -D fakepop      $RPM_BUILD_ROOT%{_sbindir}/in.fakepop
install -D in.fakepop.8 $RPM_BUILD_ROOT%{_mandir}/man8/in.fakepop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.*
%dir %{_sysconfdir}/fakepop
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
