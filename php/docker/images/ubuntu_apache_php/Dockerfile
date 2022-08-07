# Basic image https://hub.docker.com/r/ubuntu/apache2
FROM ubuntu/apache2
RUN apt update

# Install some utils
RUN apt install -y nano vim less

# Install php
RUN apt install -y php libapache2-mod-php php-mysql
RUN service apache2 restart
