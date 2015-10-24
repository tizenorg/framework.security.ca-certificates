Name:       ca-certificates
Summary:    Install basic certificates which be used applications
Version:    0.0.1
Release:    2
Group:      System/Files
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
BuildRequires: cmake
BuildRequires: findutils
Requires(post): smack-utils

%description
install basic certificates which be used applications

%prep
%setup -q
cp -a %{SOURCE1001} .

%build
%cmake .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

mkdir -p %{buildroot}/usr/share/ca-certificates
cp -arf certs %{buildroot}/usr/share/ca-certificates/

mkdir -p %{buildroot}/opt/etc/ssl/certs
mkdir -p %{buildroot}/opt/share/ca-certificates

%make_install

%post
ln -sf /usr/share/ca-certificates/certs/* /opt/etc/ssl/certs/
chsmack -a "ca-certificates::ssl-certs" /opt/etc/ssl/certs/*


%files
%manifest %{name}.manifest
%defattr(0664, root, system, 0775)
%{_datadir}/license/%{name}

# original ca certs in RO
%dir /usr/share/ca-certificates/certs
/usr/share/ca-certificates/certs/*

# directory for sym linked ca certs in RW
%dir /opt/etc/ssl/certs

# crt file in RW
%dir /opt/share/ca-certificates
/opt/share/ca-certificates/ca-certificate.crt
