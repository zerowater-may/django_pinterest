FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/zerowater-may/django_pinterest.git

WORKDIR /home/

RUN ls

WORKDIR /home/django_pinterest/

RUN ls

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=5nb@rlfrak967e6#g4pr)8&s2tf*zsquyhbh7_x52d@7g+__+@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]