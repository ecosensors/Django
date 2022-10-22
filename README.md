# Django
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND

## Exercises

### DocBlog
This is a simple exercise to be fanilirized with Django (See DocBlog -> src )
### EcoSensor
There are two exercises 1) leaflet and 2) Console. leaflet exercise is done following [this tutorial](https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/), step by step. Then I used this new skills to build the console application with a database which contain a bit less than 1 million of measures. the console exercise is build with some javascript libraries as Leaflet for the map, Chartjs to display the measures. The goal of that exercise is to build a Django app to replace this PHP app ([See](https://bud.eco-sensors.ch/))


# Django notes
This installation is done on MacOS

## Python3
* Make sure you have installed Command Line Developper tools
* I personally switched my default shell to bash

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
pip3 -v
```

## virtualenv
Install virtualenv
```
pip3 install virtualenv
```
Go to your project folder and create an environment
```
cd /my-project/folder
python3 -m venv .env
source .env/bin/activate   # Activate your environment
deactivate                 # Quit your environment
```

## Install django
* brew install mysq-client
* (.env) pip3 install django==4.0.6
* (.env) python3 -m django --version
* (.env) pip3 freeze > requirements.txt (permet de refaire l'install avec les dépendances enregitrées dans ce fichier)
* (.env) pip3 install -r requirements.txt
* (.env) pip3 install mysqlclient
   With OSX [See](https://forum.djangoproject.com/t/how-can-i-install-mysqlclient-on-osx/14960)


## Create an application
* (.env) ./manage.py startapp blog


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

This help to solve some problems

* [Can't add POINT NOT NULL column to MySQL table](https://gis.stackexchange.com/questions/173543/cant-add-point-not-null-column-to-mysql-table) and [this](https://dba.stackexchange.com/questions/170787/cannot-get-geometry-object-from-data-you-send-to-the-geometry-field)
* [install mysqlclient on OSX](https://forum.djangoproject.com/t/how-can-i-install-mysqlclient-on-osx/14960)
