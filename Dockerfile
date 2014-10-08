FROM python:2.7

RUN pip install -r code/requirements.txt
ADD . /code
WORKDIR /code

EXPOSE  8000
CMD python manage.py runserver_plus --threaded