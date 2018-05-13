FROM python:3.6-slim

RUN apt-get -y update

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
RUN python setup.py develop

CMD ["gunicorn", "search_engine.wsgi", "--bind", "0.0.0.0:80", "--workers", "2", "--worker-class", "gevent", "--access-logfile=-"]
