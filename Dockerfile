FROM python:3.7-alpine
MAINTAINER Raymond Yau Solideveloper

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D raymond
USER raymond
