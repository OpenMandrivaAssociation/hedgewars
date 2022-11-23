%define _disable_ld_no_undefined 1
Summary:	Game with heavily armed fighting hedgehogs
Name:		hedgewars
Version:	1.0.2
Release:	1
License:	GPLv2+
Group:		Games/Strategy
Url:		http://www.hedgewars.org/
Source0:	http://download.gna.org/hedgewars/%{name}-src-%{version}.tar.bz2
Patch1:		hedgewars-1.0.0-disable-pas2c.patch
BuildRequires:	chrpath
BuildRequires:	cmake
BuildRequires:	fpc
BuildRequires:	imagemagick
# Ffmpeg 5 is still not supported
BuildRequires:	ffmpeg4-devel
BuildRequires:  atomic-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(libpng)
# Luad 5.1 is needed. Thats why we use bundled one.
#BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(physfs)
BuildRequires:	cmake(Qt5LinguistTools)

%description
Each player controls a team of several hedgehogs. During the course of the
game, players take turns with one of their hedgehogs. They then use whatever
tools and weapons are available to attack and kill the opponents' hedgehogs,
thereby winning the game. Hedgehogs may move around the terrain in a variety
of ways, normally by walking and jumping but also by using particular tools
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas.

Each turn is time-limited to ensure that players do not hold up the game
with excessive thinking or moving.

A large variety of tools and weapons are available for players during the
game: Grenade, Cluster Bomb, Bazooka, UFO, Shotgun, Desert Eagle, Fire Punch,
Baseball Bat, Dynamite, Mine, Rope, Pneumatic pick, Parachute. Most weapons,
when used, cause explosions that deform the terrain, removing circular chunks.

The landscape is an island floating on a body of water, or a restricted cave
with water at the bottom. A hedgehog dies when it enters the water (either
by falling off the island, or through a hole in the bottom of it), it is
thrown off either side of the arena or when its health is reduced,
typically from contact with explosions, to zero (the damage dealt to the
attacked hedgehog or hedgehogs after a player's or CPU turn is shown only
when all movement on the battlefield has ceased).

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_libdir}/libavwrapper.so.1.0
%{_libdir}/libhwlua.so.1*
%{_libdir}/libhwlua.so.5.1.4
%{_libdir}/libphyslayer.so.1.0
%{_datadir}/appdata/hedgewars.appdata.xml
%{_mandir}/man6/hedgewars.6*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-src-%{version}
%autopatch -p1

%build
%cmake_qt5 \
	-DNOSERVER=TRUE \
	-DDATA_INSTALL_DIR="%{_datadir}/%{name}" \
	-Dtarget_binary_install_dir="%{_bindir}" \
	-Dtarget_library_install_dir="%{_libdir}" \
	-DPHYSFS_SYSTEM=ON \
	-DLUA_SYSTEM=OFF
%make_build

%install
%make_install -C build

install -D -m644 misc/%{name}_ico.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m644 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/%{name}.png
rm -rf %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_datadir}/applications/
cat <<EOF >%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Hedgewars
GenericName=Cartoony artillery game
Comment=Funny turn-based artillery game, featuring fighting Hedgehogs!
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;Qt;
EOF

install -D -m644 man/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

# remove unneeded devel libraries files
find %{buildroot} -name '*.so' -delete


chrpath -d %{buildroot}%{_bindir}/*

