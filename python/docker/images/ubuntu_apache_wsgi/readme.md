https://ubiq.co/tech-blog/install-mod_wsgi-ubuntu/

https://modwsgi.readthedocs.io

To build an image

`docker build -t samples/apache.wsgi .`

To run container

`docker run -d --name samples.apache.wsgi -e TZ=UTC -p 8080:80 -v /home/vlad/Projects/3dmm/samples/python/app:/var/www/html  samples/apache.wsgi`

To ssh

`docker exec -ti samples.apache.wsgi bash`