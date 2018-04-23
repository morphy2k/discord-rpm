Name:           discord-ptb
Version:        0.0.8
Release:        1%{?dist}
Summary:        Discord Public Test Build

License:        proprietary
URL:            https://discordapp.com/
Source0:        https://discordapp.com/api/download/ptb?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz

Requires:       libXScrnSaver libcxx libatomic
AutoReqProv:    no

%description
Discord Linux - Public Test Build

%global debug_package %{nil}

%prep
%autosetup -n DiscordPTB

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/opt/DiscordPTB
mkdir -p $RPM_BUILD_ROOT/usr/share/applications

cp -r * $RPM_BUILD_ROOT/opt/DiscordPTB/
ln -sf /opt/DiscordPTB/DiscordPTB $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 discord-ptb.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/opt/DiscordPTB/
%{_bindir}/DiscordPTB
/usr/share/applications/discord-ptb.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Apr  23 2018 Markus Wiegand <mail@morphy2k.io>
- Update to 0.0.8

* Tue Jan  16 2018 Markus Wiegand <mail@morphy2k.io>
- Update to 0.0.7

* Tue Dec  19 2017 Markus Wiegand <mail@morphy2k.io>
- Init
