![workflow](https://github.com/yurlovaviktoriya/yamdb_final/workflows/run-test/badge.svg)

# YaMDB

YaMDb service is a database of reviews about films, books and music. The code of this service implements REST API.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine using [Docker Compose](https://docs.docker.com/compose/).


### Prerequisites

What things you need to install the software and how to install them.

 - [Docker](https://docs.docker.com/engine/install/);
 - [Docker Compose](https://docs.docker.com/compose/install/).
 
 ### Installing
Application launch:
```
docker-compose up
```  
See container id
```
docker ps
```
Open web container
```
docker exec -it <CONTAINER ID> bash
```
Perform migrations
```
python manage.py migrate
```
Сreate superuser
```
python manage.py createsuperuser
```  
Import data into DB
```
python manage.py loaddata dump.json
```
## Built With

- [Django](https://www.djangoproject.com/) is a high-level Python Web framework;
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs;
- [Gunicorn](https://gunicorn.org/) is a Python WSGI HTTP Server for UNIX.
## Authors

- [**egor-karitskiy**](https://github.com/egor-karitskiy);
- [**yurlovaviktoriya**](https://github.com/yurlovaviktoriya);
- [**GlamorousNutlet**](https://github.com/GlamorousNutlet);
- [**soberlook**](https://github.com/soberlook).

