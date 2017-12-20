Name:           discord
Version:        0.0.3
Release:        1%{?dist}
Summary:        Discord stable release

License:        proprietary
URL:            https://discordapp.com/
Source0:        https://discordapp.com/api/download?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz

Requires:       libXScrnSaver libcxx libatomic
AutoReqProv:    no

%description
Discord Linux - Stable release

%global debug_package %{nil}

%prep
%autosetup -n Discord

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/opt/Discord
mkdir -p $RPM_BUILD_ROOT/usr/share/applications

cp -r * $RPM_BUILD_ROOT/opt/Discord/
ln -sf /opt/Discord/Discord $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 discord.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/opt/Discord/
%{_bindir}/Discord
/usr/share/applications/discord.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Tue Dec  19 2017 Markus Wiegand <mail@morphy2k.io>
- Init
