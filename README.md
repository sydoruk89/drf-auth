# Authentication & Production Server

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

Django REST Framework to create an API, then “containerize” it with Docker and adding Permissions, Postgresql Database and  Authentication and switching to a Production Server.

## Architecture

* Python 3.8.3
* Poetry
* Django
* Docker
* Postgres 11
* Gunicorn

## Usage 
### Features - Django REST Framework
* Added JWT Authentication to API.
    - Adjusted project’s permissions so that only authenticated user’s have access to API.
* Kept existing authentication so DRF Browsable API still usable.
    - That includes keeping the styling
    - Installed needed libraries in project configuration and/or site settings.

### Features - Docker
* Created a boilerplate Dockerfile and docker-compose.yml
* Switched to using Gunicorn instead of Django’s built in development server.
    - added 4 workers to avoid sluggishness
* Adjusted docker-compose.yml so that data is persisted in a volume outside of container.