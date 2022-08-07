Basic image page `https://hub.docker.com/r/ubuntu/apache2`

### Installation and running

1. Build an image

`docker build -t samples/apache.php .`

2. Run a container

`docker run -di --name samples.apache.php -e TZ=UTC -p 8080:80 -v /home/vlad/Projects/3dmm/samples/php/app:/var/www/html samples/apache.php` 

3. Visit on home system `localhost:8080` to ensure all system goes.

4. Use `docker exec -ti apache.php bash` to ssh