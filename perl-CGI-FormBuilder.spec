%define module	CGI-FormBuilder
%define name	perl-%{module}
%define version     3.05.01
%define up_version  3.0501
%define	release	    %mkrel 1
%define	epoch	    1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
Summary:	Easily generate and process stateful forms
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%module/
Source:		http://www.cpan.org/modules/by-module/CGI/%{module}-%{up_version}.tgz
BuildRequires:	perl(CGI)
BuildRequires:	perl(Template)
BuildRequires:	perl(HTML::Template)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
FormBuilder is a fully-functional form engine with numerous features.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled because of problem with HTML::Entities (http://rt.cpan.org//Ticket/Display.html?id=16193)
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README INSTALL
%{perl_vendorlib}/CGI
%{_mandir}/*/*



