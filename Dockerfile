FROM python:3.6.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip install -r requirements.txt
