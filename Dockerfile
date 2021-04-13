FROM python:3.9.0

RUN echo "testirdssadsadsfdsef"

WORKDIR /home/

RUN git clone https://github.com/zerowater-may/django_pinterest.git

WORKDIR /home/django_pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# RUN echo "SECRET_KEY=5nb@rlfrak967e6#g4pr)8&s2tf*zsquyhbh7_x52d@7g+__+@" > .env


EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
