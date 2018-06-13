*Geography test*

1. Deploying to heroku
    1. Create heroku app
    2. Run
    ```bash
    heroku buildpacks:set https://github.com/cyberdelia/heroku-geo-buildpack.git
    heroku buildpacks:add heroku/python
    ```
    3. create super user with command
    ```bash
    heroku run python manage.py createsuperuser
    ```
    
    TODO: heroku uses 2.1.3 gdal version which is not working like 2.2.2 
    where tests were made  

2. Deploying localy 
    1. Install libgdal-dev in 2.2.2 version
    2. Install requirements from requirements.txt file
    3. start application with ```gunicorn geo_test.wsgi```