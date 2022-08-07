# Basic image https://hub.docker.com/r/ubuntu/apache2
FROM ubuntu/apache2
RUN apt-get update

# Install some utils
RUN apt-get install -y nano

# Install php
RUN apt-get install -y php libapache2-mod-php php-mysql
RUN service apache2 restart

