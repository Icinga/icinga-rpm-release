Name:		icinga-rpm-release
Version:	7
Release:	1%{?dist}
Summary:	Icinga Package Repository

Group:		System Environment/Base
License:	GPLv2
URL:		http://packages.icinga.org/epel/
Source0:	%{name}-%{version}.tar.gz
Source1:	http://packages.icinga.org/icinga.key
Source2:	http://packages.icinga.org/epel/ICINGA-release.repo
Source3:	http://packages.icinga.org/epel/ICINGA-snapshot.repo

BuildArch:	noarch

Requires:	redhat-release >=  %{version}

%description
This package contains the Icinga package repository GPG key
as well as configuration for yum.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG key
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ICINGA

#yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
#install -pm 644 -D %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/rpm/macros.d/macros.icinga
#install -pm 644 -D %{SOURCE5} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/90-icinga.preset

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
#/usr/lib/rpm/macros.d/macros.icinga
#%{_prefix}/lib/systemd/system-preset/90-icinga.preset


%changelog

