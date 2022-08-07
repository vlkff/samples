Basic image page `https://hub.docker.com/r/ubuntu/apache2`

### Installation and running

1. Pull an image with

`docker pull ubuntu/apache2`

2. Run a container with

`docker run -d --rm --name apache.php -e TZ=UTC -p 8080:80 ubuntu/apache2` 

`docker run -d --name apache.php -e TZ=UTC -p 8080:80 -v /home/vlad/Projects/3dmm/samples/php/app:/var/www/html  bd6a740bc785`

3. Visit on home system `localhost:8080` to ensure all system goes.

4. Use `docker exec -ti apache.php bash` to ssh