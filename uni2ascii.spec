Summary:	Conversion tools between UTF-8 Unicode and 7-bit ASCII equivalents
Summary(pl.UTF-8):	Narzędzia do konwersji pomiędzy UTF-8 a 7-bitowymi zamiennikami ASCII
Name:		uni2ascii
Version:	4.11
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://billposer.org/Software/Downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	d9633bfb0d58e652c972e20b91b7a2db
URL:		http://billposer.org/Software/uni2ascii.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uni2ascii and ascii2uni provide conversion in both directions between
UTF-8 Unicode and more than thirty 7-bit ASCII equivalents, including
RFC 2396 URI format and RFC 2045 Quoted Printable format.

%description -l pl.UTF-8
uni2ascii oraz ascii2uni pozwalają na konwersję w obu kierunkach
pomiędzy kodowaniem Unicode UTF-8 a ponad trzydziestoma 7-bitowymi
zamiennikami ASCII, w których skład wchodzi format RFC 2396 URI oraz
format RFC 2045 Quoted Printable.
%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ascii2uni.1*
%{_mandir}/man1/uni2ascii.1*
