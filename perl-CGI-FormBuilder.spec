%define upstream_name    CGI-FormBuilder
%define upstream_version 3.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Easily generate and process stateful forms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI-FormBuilder-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Template)
BuildRequires:	perl(Template)

BuildArch:	noarch

%description
FormBuilder is a fully-functional form engine with numerous features.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled because of problem with HTML::Entities (http://rt.cpan.org//Ticket/Display.html?id=16193)
#%{__make} test

%install
%makeinstall_std

%files
%doc Changes README INSTALL
%{perl_vendorlib}/CGI
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:3.50.100-2mdv2011.0
+ Revision: 680687
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:3.50.100-1mdv2011.0
+ Revision: 504599
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:3.05.01-2mdv2010.0
+ Revision: 430308
- rebuild

* Sat Aug 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.05.01-1mdv2009.0
+ Revision: 272809
- new version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0:3.0302-3mdv2009.0
+ Revision: 255771
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0:3.0302-1mdv2008.1
+ Revision: 131272
- kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0302-1mdv2007.0
+ Revision: 73370
- import perl-CGI-FormBuilder-3.0302-1mdv2007.0

* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0:3.0302-1mdv2007.0
- New release 3.0302

* Mon May 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0:3.0301-1mdk
- New release 3.0301

* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0:3.03-1mdk
- 3.03
- better source URL
- better buildrequires syntax
- disabled test because of problem with HTML::Entities

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.0202-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.13-1mdk
- initial Mandriva package



