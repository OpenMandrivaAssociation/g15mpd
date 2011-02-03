Name:                   g15mpd
Version:                1.0.0
Release:                %mkrel 7
Summary:                Simple frontend for the MPD Media Player Daemon, for use with g15daemon
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15mpd-%{version}.tar.bz2
Patch0:			g15mpd-1.0.0-newer-mpd.patch
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          libmpd-devel
BuildRequires:          libx11-devel
BuildRequires:		libxtst-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A simple frontend for the MPD Media Player Daemon, for use with g15daemon.

Features:
- Artist/Title Info is displayed
- Track time elapsed/total time is displayed, with a completion bar.
- Random and Repeat modes are available.
- Multimedia keys are usable when run from X.

Caveats:
- Requires MPD to be running in the background.
- In order for multimedia keys to function, the frontend must be run from
  X11, either in a console, or at X login.
- Requires that X11 has been configured to understand the mediakeys, either
  via the g15daemon xmodmap file, or a similar keyboard being selected in X
  configuration.
- Currently, playlist management is not available, so another mpd frontend
  will be required to create one.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(-,root,root,0755)
%{_bindir}/g15mpd
