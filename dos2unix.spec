Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		dos2unix
Version:	5.3.3
Release:	1
License:	BSD
Group:		Text tools
URL:		http://waterlan.home.xs4all.nl/dos2unix.html
Source0:	http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	perl-devel
Provides:	unix2dos = %{version}-%{release}
Provides:	mac2unix = %{version}-%{release}
Provides:	unix2mac = %{version}-%{release}
Obsoletes:	unix2dos < 5.3.1

%description
A filter used to convert DOS-style EOLs to UNIX-style EOLs and vice
versa (EOL - End Of Line character).

This package contains updated Benjamin Lin's implementations of dos2unix
and unix2dos.

Benjamin Lin's implementations of dos2unix and unix2dos are a part of many
Linux distributions such as RedHat, Fedora, Suse, Gentoo and others.
This update includes all RedHat patches and fixes several other problems.
Internationalization has been added and ports to various OS have been made.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

# doc is installed two times in doc dir
%__rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}-%{version}/*
%{_bindir}/dos2unix
%{_bindir}/unix2dos
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*
%{_mandir}/es/man1/*.1*
%{_mandir}/nl/man1/*.1*

