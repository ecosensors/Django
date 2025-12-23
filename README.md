# Django
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND

(The following README and the related Django App, are histories of all steps to make my App running, during my learning time on Django)

The project is still on progress ... :)

## Exercises

### DocBlog
This is a simple exercise to be familirized with Django (See DocBlog -> src )

### EcoSensor
There are two exercises 1) leaflet and 2) Console. leaflet exercise is done following [this tutorial](https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/), step by step. Then I used this new skills to build the console application with a database which contain a bit less than 1 million of measures. the console exercise is build with some javascript libraries as Leaflet for the map, Chartjs to display the measures. The goal of that exercise is to build a Django app to replace this PHP app ([See](https://bud.eco-sensors.ch/))


# Prepare and install Django
This installation is done on MacOS Monterey (12.6), on a MacOS Ventura 13.0.1 and Tahoe (26.2)
I use MAMP 6.6 as local server and PHP 7.4.21, MySQL 5.7.34 and PHPMyAdmin 5.1.0.

Before the next steps, I imported a .sql file to the database 'db_console', with a bit less of 1 millions of measures.

## Python3
* Make sure you have installed Command Line Developper tools
```
xcode-select --install
```

> On Tahoe, I have not switch the shell.
> If you use zsh, bellow replace .bash_profile by .zsh_sessionsl to bash

```
chsh -s /bin/bash
```
and I added the following simple lines to .bash_profile
```
# nano .bash_profile
export PS1="\[\033[1;31m\]\u:\[\033[0m\]\w$ "
alias ll='ls -laG'
```

* Make sure you installed Python3 and pip3
```
python3 --version
pip3 -V
```
* Install brew if it is not done (Replace [user] by your usename)
```
brew --version
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
At the end of the installation, you will be asked to run three additional command

## virtualenv
Install virtualenv
```
pip3 install virtualenv
```
Go to your project folder and create an environment
```
cd /my-project/folder
python3 -m venv .env        # Create an environement named .env
source .env/bin/activate    # Activate your environment
deactivate                  # Quit your environment
```

## Installation of  Django
### Preparation
Make sure you have installed mysql-client
```
brew install mysql-client
```

You need to edit the .bash_profile file and add the following line
```
PATH="/usr/local/opt/mysql-client/bin:$PATH"
```
and then reload your bach_profile
```
source ~/.bash_profile
```

Then go to your environment
```
cd /my-project/folder
source .env/bin/activate   # Activate your environment
```
and install mysqlclient on your OSX

```
(.env) pip3 install mysqlclient
```


### Installation
```
(.env) pip3 install django==4.1.4
(.env) python3 -m django --version
```

Note, you can have a requierements.txt file with all needed packages
```
(.env) pip3 install -r requirements.txt # Install packages listed in the requirements file
(.env) pip3 freeze > requirements.txt # Extract the installed package into the requirements.txt file
```
example of a requierements.txt file
```
asgiref==3.6.0
sqlparse==0.4.3
django==4.1.4
djangorestframework==3.14.0
djangorestframework-gis==1
django-filter==22.1.0
djangorestframework-simplejwt==5.2.2
```


You can now create a Django project and app.

## To create a Django project
```
(.env) django-admin startproject console
```

## To create a Django application
```
(.env) cd console
(.env) ./manage.py startapp map
```

## To configure the database parameters
Go to 'console' folder and the edit settings.py file. Replace the following lines:
(Keep in mind, I am using MAMP as an Apache local server)

```
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'db_console',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',

    }
}
```

### Specification
As my application use geospacial coordinate, the command `./manage.py inspectdb`will generate a error:

> django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library

This is because djangorestframework-gis and GDAL need to be install on my OSX

#### Installation of djangorestframework-gis
```
pip3 install djangorestframework-gis
```

#### Installation of GDAL
Info:
[GDAL](https://gdal.org/)
[GDAL - Linux](https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/geolibs/#gdal)
[GDAL - Homebrew](https://formulae.brew.sh/formula/gdal)


Mac OSX:

```
brew install gdal
```
The above command is enough to cancel the GIDAL library error, but you should be interested about pip3 download gdal (see above link)

### Check the database and create the models.py file

You can now test the database
```
source .env/bin/activate   # Activate your environment
(.env) ./manage.py inspectdb
```
models.py
```
cd /your/project/location/
(.env) ./manage.py inspectdb > models.py
```

Keep in mind, I am using an existing database with a lot of measures. The stations are in different fields and I localise them with latitude and longitude. I need to create a 'location' column in my table of my database and I need to adapt/update the models.py file, as well. For that reason, I need to generate new database schema changes based on my models.py file.


First, let’s create the migration files
```
(.env) ./manage.py makemigrations
```
Now let’s use that information to update the database
```
(.env) ./manage.py migrate
```
Create a superuser (you will be asked to chose an username and a password and an e-mail)
```
./manage.py createsuperuser
```

Start your app
```
(.env) ./manage.py runserver 127.0.0.1:8080
```

Before using the database cache, you must create the cache table with this command:
```
./manage.py createcachetable
```

## Help
Uesfull links:

* [Leaflet](https://leafletjs.com/)
* [Django-rest-framework](https://www.django-rest-framework.org/)
* [Django - Leaflet - PostGis - GeoDjango - Part 1](https://www.paulox.net/2020/12/08/maps-with-django-part-1-geodjango-spatialite-and-leaflet/)
* [Django - Leaflet - PostGis - GeoDjango - Part 2](https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/)
* [Install GDAL on macOS](https://mits003.github.io/studio_null/2021/07/install-gdal-on-macos/)
* [Queryset](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#latest)
* [Django & Vuejs (1)](https://www.sitepoint.com/web-app-prototype-django-vue/)
* [Django & Vuejs (2)](https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/)
* [Install Django on Mac](https://appdividend.com/2022/06/15/how-to-install-django-in-mac/)

This help to solve some problems

* [Can't add POINT NOT NULL column to MySQL table](https://gis.stackexchange.com/questions/173543/cant-add-point-not-null-column-to-mysql-table) and [this](https://dba.stackexchange.com/questions/170787/cannot-get-geometry-object-from-data-you-send-to-the-geometry-field)
* [install mysqlclient on OSX](https://forum.djangoproject.com/t/how-can-i-install-mysqlclient-on-osx/14960)
