Summary:	Simple frontend for the MPD Media Player Daemon, for use with g15daemon
Name:		g15mpd
Version:	1.0.0
Release:	9
License:	GPLv2+
Group:		Sound
Url:		http://g15daemon.sourceforge.net/
Source0:	http://downloads.sourceforge.net/g15daemon/%{name}-%{version}.tar.bz2
Patch0:		g15mpd-1.0.0-newer-mpd.patch
Patch1:		g15mpd-1.0.0-rosa-linkage.patch
BuildRequires:	g15-devel
BuildRequires:	g15daemon_client-devel
BuildRequires:	g15render-devel
BuildRequires:	pkgconfig(libmpd)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)

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

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/g15mpd

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std
rm -r %{buildroot}%{_docdir}

