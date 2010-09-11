Summary:	InfiniBand Communication Manager Assistant
Summary(pl.UTF-8):	Asystent zarządzania komunikacją InfiniBand
Name:		ibacm
Version:	1.0.3
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	a4f808580e680f23f26396b9baf9c251
URL:		http://www.openfabrics.org/
BuildRequires:	libibverbs-devel
BuildRequires:	libibumad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/ib_acme
%attr(755,root,root) %{_sbindir}/ib_acm
%{_mandir}/man1/ib_acm.1*
%{_mandir}/man1/ib_acme.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/infiniband/acm.h
%{_mandir}/man7/ib_acm.7*
