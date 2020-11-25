FROM python:3.8.3-alpine

WORKDIR /debt_book
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install djangorestframework
RUN apk add postgresql

COPY requirements.txt /debt_book/
RUN pip3 install -r requirements.txt

RUN apk --no-cache add curl
RUN mkdir -p /debt_book

COPY . /debt_book
