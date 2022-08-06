## Commands

### Images

`docker build -t <image> .` - build an image

`docker images` - list images

### Containers

`docker container ls` - see containers

`docker run <container> whoami` - run sample command in a new container and destroy

`docker run -d p 6001:6001 <container> whoami`

To remove last exited container matched to some grep-expression

`docker rm $(docker ps -f status=exited| grep '3dmm' | sed 's/\|/ /'|awk '{print $1}'|tail -n 1 )`

#### Running 'persistent' container

To run 'persistent', named, autoremoved container in a background

For true persistence use volumes or bindings

`docker run --rm -d -i --name <new-container-name> <image-from-name>`

e.g.

`docker run -d -i --name 3dmm.container.mariadb 3dmm.container.mariadb bash`

add --rm option to autoremove it on exit

Use `docker stop <name>` and `docker start <name>` to stop&run it. It will persist it's state.

It also would persist it's state on system reboot, but need manual start

### Inside containers

`docker exec -ti 3dmm.container.mariadb bash` To 'ssh' to container
