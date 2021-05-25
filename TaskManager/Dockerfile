# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Installing python dependencies
COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copying src code to Container
COPY . /usr/app
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Ports
EXPOSE 8000


# Environemnt variables
ENV DJANGO_ENV  development
ENV GUNICORN_BIND  0.0.0.0:8000
ENV GUNICORN_WORKERS 4
ENV GUNICORN_WORKERS_CONNECTIONS 1001

# Running Python Application
CMD python manage.py runserver 0.0.0.0:8000
