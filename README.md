# Airports application demo

This code belongs to Mykola GORBAN.

# Technology stack:
- Django - https://www.djangoproject.com/
- DRF (Django Rest Framework) - https://www.django-rest-framework.org/
- Celery - https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
- Docker - https://docs.docker.com/
- Docker compose - https://docs.docker.com/compose/

# ToDo:
- Django:

  - build Airport model(fields -> airports.csv)
- Django Admin:

  - List of Airports 

  - Search Airports by ident and name 

  - ability to create/update/delete an airport manually

- DRF API:

  - build GET /airports

  - build GET /airports with search by ident

- Celery task:

  - schedule a task to download and update data from https://davidmegginson.github.io/ourairports-data/airports.csv

# Requirements:
1. Application has to run in docker/docker compose
  - docker compose up
2. Create public repository on https://github.com/
  - the source code of the application has to be in the repository

# Usage (draft)

run

docker -d compose up