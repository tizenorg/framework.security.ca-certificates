#sbs-git:slp/pkgs/c/ca-certificates ca-certificates 0.0.1 93a79fb3ff2d8233e4775b96f0d7592db74aea03

Name:       ca-certificates
Summary:    Install basic certificates which be used applications
Version: 0.0.1
Release:    2
Group:      System/Files
License:    None
Source0:    %{name}-%{version}.tar.gz


%description
install basic certificates which be used applications

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}

mkdir -p %{buildroot}/opt/etc/ssl
cp -arf certs %{buildroot}/opt/etc/ssl/

%files
%defattr(-,root,root,-)
/opt/etc/ssl/certs/*
%{_datadir}/license/%{name}
