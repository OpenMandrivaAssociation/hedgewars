Summary:	Game with heavyly armed figthing hedgehogs
Name:		hedgewars
Version:	0.9.18
Release:	1
License:	GPLv2
Group:		Games/Strategy
URL:		http://www.hedgewars.org/
Source:		http://download.gna.org/hedgewars/%{name}-src-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	fpc
BuildRequires:	imagemagick
BuildRequires:	lua-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel

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

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_miconsdir}
convert -resize 16x16 misc/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
convert -resize 48x48 misc/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
cp misc/%{name}.png %{buildroot}%{_iconsdir}

mkdir -p %{buildroot}%{_datadir}/applications/
%{__cat} <<EOF >%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
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

%files
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/*


%changelog
* Mon Nov 21 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.17-1mdv2011.0
+ Revision: 732126
- New version 0.9.17

* Sun Oct 23 2011 Zombie Ryushu <ryushu@mandriva.org> 0.9.16-1
+ Revision: 705741
- Upgrade to 0.9.16

* Fri Mar 25 2011 Zombie Ryushu <ryushu@mandriva.org> 0.9.15-1
+ Revision: 648447
- Upgrade to 0.9.15

* Mon Nov 15 2010 Jani Välimaa <wally@mandriva.org> 0.9.14.1-1mdv2011.0
+ Revision: 597795
- new version 0.9.14.1

* Sun Apr 04 2010 Jani Välimaa <wally@mandriva.org> 0.9.13-1mdv2010.1
+ Revision: 531441
- add missing BR
- new version 0.9.13

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 0.9.12-1mdv2010.1
+ Revision: 463331
- New version 0.9.12

* Sat May 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.11-1mdv2010.0
+ Revision: 381531
- update to new version 0.9.11

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 0.9.10-3mdv2010.0
+ Revision: 376438
- fix icon size

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 0.9.10-2mdv2010.0
+ Revision: 376395
- rebuild

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 0.9.10-1mdv2010.0
+ Revision: 376358
- add missing buildrequires
- version 0.9.10
- add missing icons

* Sat Mar 21 2009 Emmanuel Andry <eandry@mandriva.org> 0.9.9-1mdv2009.1
+ Revision: 360006
- New version 0.9.9

* Tue Jan 13 2009 Zombie Ryushu <ryushu@mandriva.org> 0.9.8-1mdv2009.1
+ Revision: 328973
- New Version 0.9.8

* Mon Jan 05 2009 trem <trem@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 325153
- new release 0.9.7

* Sun Aug 10 2008 Funda Wang <fwang@mandriva.org> 0.9.6-1mdv2009.0
+ Revision: 270331
- add openssl-devel as BR
- clearify license
- New version 0.9.6

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.8.1-2mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Emmanuel Andry <eandry@mandriva.org>
    - drop x-mandrivalinux tag


* Wed Jan 24 2007 Michael Scherer <misc@mandriva.org> 0.8.1-1mdv2007.0
+ Revision: 112942
- Import hedgewars

