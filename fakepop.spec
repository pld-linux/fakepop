# TODO: optflags
Summary:	Fake POP3 daemon, delivers same messages to all users
Summary(pl):	Fa³szywy demon POP3, dostarczaj±cy te same wiadomo¶ci do wszystkich
Name:		fakepop
Version:	8
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://vztech.com.br/public/software/fakepop/%{name}-src-%{version}.tar.gz
# Source0-md5:	9872ab86c626e44486ffd6016176713c
URL:		http://vztech.com.br/public/software/fakepop/
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

%description -l pl
fakepop to fa³szywy demon POP3. Zwraca wszystkim u¿ytkownikom zawsze
te same wiadomo¶ci, niezale¿nie od nazw u¿ytkowników i hase³.
Wszystkie kombinacje nazw u¿ytkownika i hase³ s± przyjmowane.

G³ównym celem fakepop jest doradzenie u¿ytkownikom, ¿e serwer
przyjmuje wy³±cznie po³±czenia pop3-ssl, a oni maj± b³êdnie
skonfigurowane pop3 bez SSL. Komunikaty mo¿na zmieniæ w katalogu
/etc/fakepop/, aby pouczyæ u¿ytkowników, jak powinni skonfigurowaæ
swoje programy pocztowe do u¿ywania pop3-ssl zamiast pop3.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

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
