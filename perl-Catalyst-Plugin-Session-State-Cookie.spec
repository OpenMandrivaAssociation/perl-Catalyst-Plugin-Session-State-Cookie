%define upstream_name    Catalyst-Plugin-Session-State-Cookie
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Cookie driver for Catalyst sessions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Plugin::Session)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Obsoletes: perl-Catalyst-P-S-State-Cookie < %{version}-%{release}

%description
In order for the Catalyst::Plugin::Session manpage to work the session ID
needs to be stored on the client, and the session data needs to be stored
on the server.

This plugin stores the session ID on the client using the cookie mechanism.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


