### Explore kernel and distro

Get a kernel version
uname -a

Recognize distro my testing package managers presence
apt-get -v || pacman -v

#### Specific distro checks

Ubuntu 

lsb_release -d || cat /etc/issue

#### Explore privileges

`cat /etc/passwd` see users

`cat  /etc/group` see groups

#### Explore system vars

export -p

#### Explore network

Open ports

`cat /etc/services` see all system opened ports

`ss -a` - to see sockets info

`netstat -a`

Firewall

#### Installed software

#### Available resources

#### If we inside docker container

docker container inspect <name>