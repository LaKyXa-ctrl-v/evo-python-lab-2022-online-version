
# Instructions for starting the project

## 1) Install poetry and activate venv

```
$ pip install poetry
$ poetry install
```
## 2) Then install the dependencies:(if you dont use poetry)

```
$ pip install -r requirements.txt
```
## 3) Create DB

```
$ python manage.py migrate
$ python manage.py loaddata db.json
```

## 4) Start server

```
$ python manage.py runserver
```

## 5) If you need start server in docker container:

```
$ docker-compose up -d
```

## 6) Open site on [local](http://localhost:8000/)

## 7) Read README.md 
_____
# Admin (if you need)

## 1) To enter the admin panel, you first need to create a superuser

```
$ python manage.py createsuperuser
```

## 2) Then log in [here](http://127.0.0.1:8000/admin)