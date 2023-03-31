# ddtrace + celery + gevent bug

Project to demonstrate a bug with ddtrace, celery and gevent.

Video Demo: TODO

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
cp sample.env .env
# fill out values in .env file
```

Spin up redis (which is the celery broker):

```
docker compose up -d
```

## Bug

Run the server with ddtrace, celery and gevent. You don't need to have the datadog agent running (bug occurs with and without it).

```bash
ddtrace-run celery -A mysite.celery.app worker --pool=gevent --loglevel=info
# django.core.exceptions.ImproperlyConfigured: Requested settings, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

DJANGO_SETTINGS_MODULE=mysite.settings ddtrace-run celery -A remix.celery.app worker --pool=gevent --loglevel=info
# ModuleNotFoundError: No module named 'mysite'
```

## Other run configurations that work

The following servers work fine:

```
celery -A mysite.celery.app worker
celery -A mysite.celery.app worker --pool=gevent
ddtrace-run celery -A mysite.celery.app worker
```
