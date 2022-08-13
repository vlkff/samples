# Package managers

## Apt

See package info

## Pacman

`-S` used to work with remote repo

`-Q` for installed packages

Search package in repo `pacman -Ss <package-name>`

All installed packages `pacman -Q`

See package info `pacman -Qi <name>`

See package-related files `pacman -Fl <name>`


How to remove orprahed packages?
E.g. now I install apache with `apr-1.7.0-3  apr-util-1.6.1-9` dependencies.

## Snaps

Snaps are applications packaged with all their dependencies to run on all popular Linux distributions from a single build. 
They update automatically and roll back gracefully.

Snaps are discoverable and installable from the Snap Store, an app store with an audience of millions.

`snap` util may not be included in standard distro

`snap list` - all installed snaps

