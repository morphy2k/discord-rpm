Name:           discord-canary
Version:        0.0.44
Release:        1%{?dist}
Summary:        Experimental canary build for Discord

License:        proprietary
URL:            https://discordapp.com/
Source0:        https://discordapp.com/api/download/canary?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz

Requires:       libXScrnSaver libcxx libatomic
AutoReqProv:    no

%description
Discord Linux - VERY Experimental Canary Release

%global debug_package %{nil}

%prep
%autosetup -n DiscordCanary

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/opt/DiscordCanary
mkdir -p $RPM_BUILD_ROOT/usr/share/applications

cp -r * $RPM_BUILD_ROOT/opt/DiscordCanary/
ln -sf /opt/DiscordCanary/DiscordCanary $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 discord-canary.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/opt/DiscordCanary/
%{_bindir}/DiscordCanary
/usr/share/applications/discord-canary.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Fri Dec  22 2017 Markus Wiegand <mail@morphy2k.io>
- Update to 0.0.44

* Thu Dec  21 2017 Markus Wiegand <mail@morphy2k.io>
- Update to 0.0.42

* Wed Dec  20 2017 Markus Wiegand <mail@morphy2k.io>
- Update to 0.0.41

* Tue Dec  19 2017 Markus Wiegand <mail@morphy2k.io>
- Init
