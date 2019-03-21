FROM python:latest
MAINTAINER "ABDUGOFIR"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
