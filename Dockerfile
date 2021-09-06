FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/youngjuj/me_alone.git

WORKDIR /home/me_alone/

RUN echo "SECRET_KEY=django-insecure-&!%x*vxdce-stikd-(*dle9qi=uayrguq1jm2#)ekwgdhrh&gj" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
