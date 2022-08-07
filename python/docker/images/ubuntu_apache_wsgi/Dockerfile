#
# Basic image https://hub.docker.com/r/ubuntu/apache2
# About mod_wsgi for apache  https://modwsgi.readthedocs.io/en/master/index.html
#

FROM ubuntu/apache2
RUN apt-get update

# Some tools
RUN apt -y install -y vim nano

# Up all we need to run python in apache2
RUN apt -y install python3
RUN apt -y install python3-pip
RUN apt install -y apache2-utils libexpat1 ssl-cert
RUN apt install -y libapache2-mod-wsgi-py3
RUN service apache2 restart



# pip3 install mod_wsgi

# pip3 install mod_wsgi-httpd
