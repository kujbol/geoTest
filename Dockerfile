FROM andrejreznik/python-gdal

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install GDAL==2.2.2
RUN pip install gevent

COPY . /app
RUN cp /usr/local/bin/python3 /usr/local/bin/python

