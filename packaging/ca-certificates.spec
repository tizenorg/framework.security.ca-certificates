
Name:       ca-certificates
Summary:    Install basic certificates which be used applications
Version:    0.0.1
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    ca-certificates-%{version}.tar.gz
Source1001: packaging/ca-certificates.manifest 


%description
install basic certificates which be used applications




%prep
%setup -q 


%build
cp %{SOURCE1001} .



%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/etc/ssl/certs/
cp -af certs/* %{buildroot}/opt/etc/ssl/certs/


%files
%manifest ca-certificates.manifest
%defattr(-,root,root,-)
/opt/etc/ssl/certs/*
