Summary:	A nice tool for low-level managing of the parallel port
Summary(pl.UTF-8):	Proste narzędzie do niskopoziomowego zarządzania portem równoległym
Name:		lptmanager
Version:	1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lptman/%{name}-%{version}.tar.gz
# Source0-md5:	586eb102685b5be75ef7de6cabb12b4f
Patch0:		%{name}-pl-po.patch
URL:		http://lptman.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice tool for low-level managing of the parallel port and for
experimenting with it. It uses GTK+2 for the GUI and runs on Linux and
Windows (with mingw32).

%description -l pl.UTF-8
Proste narzędzie do niskopoziomowego zarządzania portem równoległym i
eksperymentowania z nim. Umożliwia włączanie/wyłączanie sygnału na
konkretnych stykach. Używa GTK+2 dla menu, działa z Linuksem oraz
Windows (mingw32).

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
