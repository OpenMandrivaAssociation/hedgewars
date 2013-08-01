Summary:	Game with heavily armed fighting hedgehogs
Name:		hedgewars
Version:	0.9.19.3
Release:	1
License:	GPLv2
Group:		Games/Strategy
Url:		http://www.hedgewars.org/
Source0:	http://download.gna.org/hedgewars/%{name}-src-%{version}.tar.bz2
Patch0:		hedgewars-src-0.9.19.1-cmake.patch
BuildRequires:	cmake
BuildRequires:	fpc
BuildRequires:	imagemagick
BuildRequires:	ffmpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_ttf)
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

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
%cmake_qt4 \
	-DNOSERVER:BOOL=ON
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_datadir}/applications/
cat <<EOF >%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{name}
Comment=Strategy action game
Exec=hedgewars
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ActionGame;StrategyGame;Qt;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert misc/%{name}.png -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
