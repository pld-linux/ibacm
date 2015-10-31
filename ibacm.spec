# TODO: PLDize init script
Summary:	InfiniBand Communication Manager Assistant
Summary(pl.UTF-8):	Asystent zarządzania komunikacją InfiniBand
Name:		ibacm
Version:	1.1.0
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	https://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	0e31f454343f5adb677c443125680eae
URL:		https://www.openfabrics.org/
BuildRequires:	libibverbs-devel
BuildRequires:	libibumad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# module needs symbols from binary
%define		skip_post_check_so	.*%{_libdir}/ibacm/.*

%description
ibacm assists with establishing communication over InfiniBand.

%description -l pl.UTF-8
ibacm pomaga przy nawiązywaniu łączności poprzez InfiniBand.

%package devel
Summary:	Header files for IB ACM service
Summary(pl.UTF-8):	Pliki nagłówkowe usługi IB ACM
Group:		Development/Libraries
Requires:	libibverbs-devel
# doesn't require base

%description devel
Header files for IB ACM service.

%description devel -l pl.UTF-8
Pliki nagłówkowe usługi IB ACM.

%prep
%setup -q

%build
%configure \
	rdmascript=rdma \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ibacm/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/ib_acme
%attr(755,root,root) %{_sbindir}/ibacm
#%attr(754,root,root) /etc/rc.d/init.d/ibacm
%dir %{_libdir}/ibacm
%attr(755,root,root) %{_libdir}/ibacm/libibacmp.so*
%{_mandir}/man1/ibacm.1*
%{_mandir}/man1/ib_acme.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/infiniband/acm.h
%{_includedir}/infiniband/acm_prov.h
%{_mandir}/man7/ibacm.7*
%{_mandir}/man7/ibacm_prov.7*
