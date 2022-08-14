# Django notes

## Créé un environement
$ python3 -m venv .env

## Install django
* brew install mysq-client
* (.env) pip3 install django==4.0.6
* (.env) python3 -m django --version
* (.env) pip3 freeze > requirements.txt (permet de refaire l'install avec les dépendances enregitrées dans ce fichier)
* (.env) pip3 install -r requirements.txt
* (.env) pip3 install mysqlclient
   With OSX (See)[https://forum.djangoproject.com/t/how-can-i-install-mysqlclient-on-osx/14960]


## Create an application
* (.env) ./manage.py startapp blog

s