# CRide

CRide is a project to share ride using advanced Django REST. Building a professionally REST API. This project allows you to create different groups where its members share a destiny. The only way to access the groups is by invitation from someone who belongs to that group (circles).


## Features
- For Django 3.2.16
- Works with Python 3.6-alpine
- Docker Compose
- Celery to asynchronous processes
- Flower - Celery monitoring tool
- Caddy - HTTP server
- Redis as cache database
- 12-Factor based settings via django-environ
- Optimized development and production settings
- Send emails via Anymail (using Mailgun by default or Amazon SES if AWS is selected cloud provider, but switchable)
- Media storage using Amazon S3, Google Cloud Storage or Azure Storage
- Run tests with unittest or pytest
- Customizable PostgreSQL version


## Development

To start working we must run:

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up
```
Open the Django project
`http://localhost:8000`
`http://localhost:8000/admin/`




## Docker

You need to install Docker and Docker Compose.
You can follow this documentation: https://docs.docker.com/engine/install/ubuntu/

* cride_local_flower 
* cride_local_celerybeat
* cride_local_celeryworker
* cride_local_django
* cride_production_postgres
* python
* postgress

Admin commands
``docker-compose run --rm django COMMAND``


Enable debugger
```shell
docker-compose up
docker-compose ps
docker rm -f <ID>

docker-compose run --rm --service-ports django
docker rm -f djangoavanzado_django_1```

Remove volume database
```bash
docker-compose ps
docker-compose down
docker volume ls
docker volume rm djangoavanzado_local_postgres_data
docker-compose up
```

Run migrations
```shell
docker-compose run --rm django python manage.py makemigrations
docker-compose run --rm django python manage.py migrate
```

App commands

```shell
docker-compose run --rm django python manage.py createsuperuser
docker-compose run --rm django python manage.py shell_plus
```

Import data
```shell
docker-compose run --rm django python manage.py shell_plus

from import_circles import import_data
import_data('data.csv')
```

Httpie
```shell
pip install httpie
http google.com
http localhost:8000/circles/ -v
http localhost:8000/circles/ -b
```

Rebuild image when change dependences

```bash
docker-compose down
docker-compose build
docker-compose up
docker rm -f djangoavanzado_django_1
docker-compose run --rm  --service-ports django
```

Test API

```shell
http localhost:8000/users/signup/ email=demo@mail.com first_name=demo last_name=user password=calc12345pT password_confirmation=qwertyuiop12345 phone_number=5434234234 username=dem

http localhost:8000/users/verify/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidG9rZW5tYWlsIiwiZXhwIjoxNTg3NjU4OTExLCJ0eXBlIjoiZW1haWxfY29uZmlybWF0aW9uIn0.1jzvbYb8itHVWX-bMQ2M0e3y_FbLJhJ0DjGiORFNUTM"

http localhost:8000/users/login/ email=demo@mail.com password=calc12345pT -b

http localhost:8000/circles/ "Authorization: Token 9bbbc8f0b35a679240315c1c2f4d366a89070625" -v
http localhost:8000/circles/create/ name=Manzana slug_name=manzana -b
```

Clean the project

```bash
docker-compose run --rm django flake8
```

Run project test

```bash
docker-compose run --rm django pytest
```


## Deploy on AWS

* Create an Ubuntu instance on EC2
* Create IAM Role and apply AWS Service->EC2->AmazonS3FullAccess **This has more restrictive**
* Open HTTP/HTTPS/SSH **(Restringe by IP)**
* Configure DNS
* Save the key access for SSH

With ssh or Putty on windows connect to instance






