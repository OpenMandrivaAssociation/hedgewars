%define major 0.9.25
%define minor 5

Summary:	Game with heavily armed fighting hedgehogs
Name:		hedgewars
Version:	%{major}
Release:	1
License:	GPLv2+
Group:		Games/Strategy
Url:		http://www.hedgewars.org/
Source0:	http://download.gna.org/hedgewars/%{name}-src-%{version}.tar.bz2
#Patch0:		hedgewars-src-0.9.20-cmake3.patch
# Used to fix linkage issues when building with -DBUILD_SHARED_LIBS:BOOL=OFF
#Patch1:		hedgewars-src-0.9.20-static.patch
#Patch2:		hedgewars-src-0.9.20.5-gcc_s.patch
BuildRequires:	chrpath
BuildRequires:	cmake
BuildRequires:	fpc
BuildRequires:	imagemagick
BuildRequires:	ffmpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lua)
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
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-src-%{major}
#patch0 -p1
#patch1 -p1
#patch2 -p1

%build
%cmake_qt5 \
	-DNOSERVER=TRUE \
	-DDATA_INSTALL_DIR="%{_gamesdatadir}/%{name}" \
	-Dtarget_binary_install_dir="%{_gamesbindir}" \
	-Dtarget_library_install_dir="%{_libdir}" \
	-DPHYSFS_SYSTEM=ON
%make_build

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_datadir}/applications/
cat <<EOF >%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{name}
Comment=Strategy action game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ActionGame;StrategyGame;Qt;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert --strip misc/%{name}.png -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

# Don't package static libs, no use for them
rm -f %{buildroot}%{_libdir}/*.a

chrpath -d %{buildroot}%{_gamesbindir}/*

