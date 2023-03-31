# ddtrace + celery + gevent bug

Project to demonstrate a bug with ddtrace, celery and gevent.

Video Demo: https://www.loom.com/share/60d9c18fe7b04cca852a73bbac924b54

## Setup

Create venv and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install - requirements.txt
```

Seed database:

```
./manage.py migrate
```

Configure environment variables:

```
cp env.sample .env
# fill out values in .env file
```

Spin up redis (which is the celery broker):

```
docker compose up -d
```

## Bug

Run the server with ddtrace, celery and gevent. You don't need to have the datadog agent running (bug occurs with and without it).

```bash
ddtrace-run celery -A mysite.celery.app worker --pool=gevent
# django.core.exceptions.ImproperlyConfigured: Requested settings, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

DJANGO_SETTINGS_MODULE=mysite.settings ddtrace-run celery -A remix.celery.app worker --pool=gevent
```

## Running celery without ddtrace works fine

The following servers work fine:

```
./manage.py runserver
gunicorn mysite.wsgi
gunicorn mysite.wsgi --worker-class gevent
ddtrace-run ./manage.py runserver
ddtrace-run gunicorn mysite.wsgi
```
