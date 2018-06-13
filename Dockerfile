FROM python:3.6-slim

RUN apt-get -y update
RUN apt-get install --assume-yes libgdal-dev

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
RUN python setup.py develop

CMD ["gunicorn", "search_engine.wsgi", "--bind", "0.0.0.0:80", "--workers", "2", "--worker-class", "gevent", "--access-logfile=-"]
