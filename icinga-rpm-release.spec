
# This package add the icinga release repository and gpg key.
# The debug repository is disabled by default.
# TODO: Add support for OpenSUSE, SLES.
Name:		icinga-rpm-release

%if 0%{?el5}
Version: 5
%elif 0%{?el6}
Version: 6
%elif 0%{?el7}
Version: 7
%elif 0%{?fedora} == 21
Version: 21
%elif 0%{?fedora} == 22
Version: 22
%elif 0%{?fedora} == 23
Version: 23
%else
Version: 99
%endif

Release:	1%{?dist}
Summary:	Icinga Package Repository

Group:		System Environment/Base
License:	GPLv2
URL:		http://packages.icinga.org/epel/
Source0:	%{name}-%{version}.tar.gz
Source1:	icinga.key
Source2:	redhat-ICINGA-release.repo
Source3:	redhat-ICINGA-snapshot.repo
Source4:	fedora-ICINGA-release.repo
Source5:	fedora-ICINGA-snapshot.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

%if 0%{?fedora}
Requires:	fedora-release >=  %{version}
%else
Requires:	redhat-release >=  %{version}
%endif

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

%if 0%{?fedora}
install -pm 644 %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%else
install -pm 644 %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog

