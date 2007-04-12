Summary: Game with heavyly armed figthing hedgehogs
Name: hedgewars
Version: 0.8.1
Release: %mkrel 1
License: GPL
Group: Games/Strategy
URL: http://www.hedgewars.org/
Source: %{name}-src-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: fpc qt4-devel SDL_ttf-devel SDL_net-devel
BuildRequires: SDL_image-devel cmake SDL_mixer-devel  

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
%setup -q -n %{name}-%{version}

%build
PATH="/usr/lib/qt4/bin/:$PATH" cmake -DCMAKE_INSTALL_PREFIX="%_prefix"  CMakeLists.txt
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/applications/

%{__cat} <<EOF >%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=%name
Comment=Strategy action game
Exec=hedgewars
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;ActionGame;StrategyGame;
EOF

%clean
%{__rm} -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-, root, root, 0755)
%_datadir/%{name}/
%_bindir/*
%_datadir/applications/*.desktop


