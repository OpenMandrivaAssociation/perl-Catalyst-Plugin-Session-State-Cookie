%define upstream_name    Catalyst-Plugin-Session-State-Cookie
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Cookie driver for Catalyst sessions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/gitweb/gitweb.cgi?p=catagits/Catalyst-Plugin-Session-State-Cookie
Source0:	https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-State-Cookie-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch
Requires:	perl(Catalyst::Plugin::Session::State)
%rename	perl-Catalyst-P-S-State-Cookie

%description
In order for the Catalyst::Plugin::Session manpage to work the session ID
needs to be stored on the client, and the session data needs to be stored
on the server.

This plugin stores the session ID on the client using the cookie mechanism.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std


%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 654413
- obsoletes wrong name pkg

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 607863
- import perl-Catalyst-Plugin-Session-State-Cookie

