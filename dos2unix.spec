Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		dos2unix
Version:	6.0.3
Release:	1
License:	BSD
Group:		Text tools
URL:		http://waterlan.home.xs4all.nl/dos2unix.html
Source0:	http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	perl-devel
Provides:	unix2dos = %{EVRD}
Provides:	mac2unix = %{EVRD}
Provides:	unix2mac = %{EVRD}
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
%make CC=%{__cc}

%install
%makeinstall_std

# doc is installed two times in doc dir
%__mv %{buildroot}%{_docdir}/%{name}-%{version}/ %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/*
%{_bindir}/dos2unix
%{_bindir}/unix2dos
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*
%{_mandir}/es/man1/*.1*
%{_mandir}/nl/man1/*.1*



%changelog
* Sun Sep 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 6.0.2-1
+ Revision: 816595
- update to 6.0.2

* Thu May 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 6.0-1
+ Revision: 797879
- update to 6.0

* Sun Mar 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.3.3-1
+ Revision: 784256
- version update 5.3.3

* Thu Feb 09 2012 Andrey Bondrov <abondrov@mandriva.org> 5.3.2-1
+ Revision: 772258
- New version 5.3.2

* Sun Nov 27 2011 Andrey Bondrov <abondrov@mandriva.org> 5.3.1-1
+ Revision: 733690
- Switch from Hany's to updated Benjamin Lin's implementations

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5
+ Revision: 663844
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2011.0
+ Revision: 604810
- rebuild

* Thu Jan 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.3-3mdv2010.1
+ Revision: 494638
- fix mkrel after fix licence
- fix licence

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2010.0
+ Revision: 413375
- rebuild

* Fri Nov 21 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.3-1mdv2009.1
+ Revision: 305410
- new release: 1.0.3
- spec cleanup

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 220680
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 149208
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 28 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 72866
- 1.0.2

* Fri May 18 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.0.1-1mdv2008.0
+ Revision: 28366
- Updated to 1.0.1.
- Removed INSTALL from the list of documentation files provided
  (useless).


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 10:03:19 (63295)
- rebuild

* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 10:00:56 (63293)
- Import dos2unix

* Tue Aug 08 2006 Lenny Cartier <lenny@mandriva.com> 1.0.0-2mdv2007.0
- rebuild

* Wed May 10 2006 Spencer Anderson <sdander@mandriva.org> 1.0.0-1mdk
- 1.0.0

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.9.1-3mdk
- Rebuild

* Wed May 12 2004 Marcel Pol <mpol@mandrake.org> 0.9.1-1mdk
- 0.9.1

* Sun May 02 2004 Marcel Pol <mpol@mandrake.org> 0.8.1-3mdk
- rebuild

