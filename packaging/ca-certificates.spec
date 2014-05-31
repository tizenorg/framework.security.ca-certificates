Name:       ca-certificates
Summary:    Install basic certificates which be used applications
Version: 0.0.2
Release:    2
Group:      System/Files
License:    None
Source0:    %{name}-%{version}.tar.gz

%if "%{_repository}" == "wearable"

%description
install basic certificates which be used applications

%prep
%setup -q

%build
echo "########################################"
echo "TIZEN_PROFILE_WEARABLE"
echo "########################################"
cp -R modules_wearable/* .

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


%else

%description
install basic certificates which be used applications

%prep
%setup -q

%build
echo "########################################"
echo "TIZEN_PROFILE_MOBILE"
echo "########################################"
cp -R modules_mobile/* .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/etc/ssl
cp -arf certs %{buildroot}/opt/etc/ssl/

%files
%defattr(-,root,root,-)
/opt/etc/ssl/certs/*



%endif
