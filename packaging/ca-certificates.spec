Name:       ca-certificates
Summary:    Install basic certificates which be used applications
Version:    0.0.1
Release:    2
Group:      System/Files
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz


%description
install basic certificates which be used applications

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE.Apache-2.0 %{buildroot}/usr/share/license/%{name}

mkdir -p %{buildroot}/opt/etc/ssl
cp -arf certs %{buildroot}/opt/etc/ssl/

%files
%defattr(-,root,root,-)
/opt/etc/ssl/certs/*
%{_datadir}/license/%{name}
