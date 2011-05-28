%define upstream_name    CGI-FormBuilder
%define upstream_version 3.0501

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch:		1

Summary:	Easily generate and process stateful forms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%upstream_name/
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Template)
BuildRequires:	perl(Template)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
FormBuilder is a fully-functional form engine with numerous features.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
