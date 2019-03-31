FROM python:latest
MAINTAINER "Abdul Sharif"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT [ "python", "/app/app.py"]
