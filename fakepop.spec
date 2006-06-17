Summary:	fake pop3 daemon. delivers same messages to all users
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
fakepop is a fake pop3 daemon. It returns always the same messages to
all users, it does not care about usernames and passwords. All
user/pass combinations are accepted.

The main purpose of fakepop is to advice users that your server only
accepts pop3-ssl and they have wrongly configured pop3 without ssl.
You can customize messages in /etc/fakepop/ directory to teach your
users how they should configure their mail clients to use pop3-ssl
instead of pop3.

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
%{_sysconfdir}/fakepop
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man8/*
