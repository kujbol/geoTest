FROM python:3.6-stretch

# Update base container install
RUN apt-get update
RUN apt-get upgrade -y

# Add unstable repo to allow us to access latest GDAL builds
RUN echo deb http://http.us.debian.org/debian sid main non-free contrib >> /etc/apt/sources.list
RUN apt-get update

# Existing binutils causes a dependency conflict, correct version will be installed when GDAL gets intalled
RUN apt-get remove -y binutils

# Install GDAL dependencies
RUN apt-get -t unstable install -y python3-dev libgdal-dev g++

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# This will install latest version of GDAL
RUN gdal-config --version
RUN pip install GDAL==2.2.3
RUN pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
RUN python setup.py develop

CMD ["gunicorn", "search_engine.wsgi", "--bind", "0.0.0.0:80", "--workers", "2", "--worker-class", "gevent", "--access-logfile=-"]
