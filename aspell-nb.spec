Summary:	Norwegian Bokmaal dictionary for aspell
Summary(pl):	Norweski (Bokmaal) s³ownik dla aspella
Name:		aspell-nb
Version:	0.50.1
%define	subv	0
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/nb/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	d1173a5ce04f39e9c93183da691e7ce8
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
Provides:	aspell-no = %{epoch}:%{version}-%{release}
Obsoletes:	aspell-no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Norwegian Bokmaal dictionary (i.e. word list) for aspell.

%description -l pl
Norweski (Bokmaal) s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
