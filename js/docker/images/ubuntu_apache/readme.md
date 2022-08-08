Basic image page `https://hub.docker.com/r/ubuntu/apache2`

We taking this image just for a common practice

### Installation and running

1. Build an image

`docker build -t samples/apache.js .`

2. Run a container

`docker run -di --name samples.apache.js -e TZ=UTC -p 8080:80 -v /home/vlad/Projects/3dmm/samples/js/app:/var/www/html samples/apache.js` 

3. Visit on home system `localhost:8080` to ensure all system goes.

4. Use `docker exec -ti apache.js bash` to ssh
