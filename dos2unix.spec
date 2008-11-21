Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		dos2unix
Version:	1.0.3
Release:	%mkrel 1
License:	GPL
Group:		Text tools
URL:		http://www.megaloman.com/~hany/software/hd2u/
Source0:	http://hany.sk/~hany/_data/hd2u/hd2u-%{version}.tgz
Source1:	http://hany.sk/~hany/_data/hd2u/hd2u-%{version}.tgz.sig
BuildRequires:	popt-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
hd2u is "Hany's Dos2Unix converter". It provides 'dos2unix'.

'dos2unix' is filter used to convert DOS-style EOLs to UNIX-style
EOLs and vice versa (EOL - End Of Line character).

%prep
%setup -q -n hd2u-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -m755 dos2unix -D %{buildroot}%{_bindir}/dos2unix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%{_bindir}/dos2unix
