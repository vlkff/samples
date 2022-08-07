
# References

Quickstart page https://docs.docker.com/get-started/05_persisting_data/

Guide https://docs.docker.com/storage/volumes/



## My brief volumes explanation

Volume is docker-managed directory on a host machine. 

First time when created it's empty.

When first time container runs with mounted volume, the volume override container's fs and bind it.

While container working it may write some data which appears 



## Questions

May be volume

How to create a volume with files from a host path ?

using this `volume create -d local -o 'device=/home/vlad/Projects/3dmm/samples' -o 'type=none' -o 'type=bind' samples-root` I have created a volume but not success to mount it to container.
Maybe the way just to create a symlink at a host.


How to create a volume with files from a path in a container ?