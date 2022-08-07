## Setting up a 'Hello world web app'

### Where I am:
- run container with apache, python3 and pip3
- found that there are 3 ways: 
  - 1 Set up python script as CGI for apache
  - 2 Install mod_wsgi apache module
-  For mod_wsgi usage there 3 ways to install it
  - compile
  - using pip
  - using libapache2-mod-wsgi-py3 ubuntu package
- Then I learned apache2 configuration in general  
- I installed it using libapache2-mod-wsgi-py3 and ensured that apache get it
   - by inspecting appeared mods_enabled/wsgi.conf
- Then I updated 000-default.conf with a few lines that seems may define which py file to run on http request
- Then I faced and issue of 404 and found that py file is running but crash with en error
`Target WSGI script '/var/www/html/index.py' does not contain WSGI application 'application'`
looks like the 'application' object or module or something that mod_wsgi requiring.   

### What I need to do next
  - up a container for JS playground - it would be easy :)
  - create an example for php modularity using include, require and namespaces
  - create an example for JS modularity
  - learn a python basics by https://docs.python.org/3/tutorial/index.html
  - learn how these modules or somethng work in a python
  - create an example for py modularity for cli script
  - try to apache for now and use some dev-purpose lightweight web server
  - read https://docs.python.org/3/library/http.server.html
  - read https://docs.python.org/3/library/internet.html
  

### Links may help set a python server when I resume it

Configuring python as CGI in apache
https://www.8host.com/blog/ustanovka-svyazki-apachemysqlpython-bez-frejmvorka-na-server-ubuntu-14-04/


https://groups.google.com/g/modwsgi/c/1LCwZnWjUVA?pli=1

https://stackoverflow.com/questions/28048342/how-do-i-configure-the-name-of-my-wsgi-application-on-aws-elastic-beanstalk

http://www.dark-hamster.com/web/programming-web/python-programming-web/solve-error-wsgi-py-not-contain-wsgi-application-application-executing-django-application/

https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/

https://stackoverflow.com/questions/30674644/installing-mod-wsgi-for-python3-on-ubuntu

https://stackoverflow.com/questions/19344252/how-to-install-configure-mod-wsgi-for-py3