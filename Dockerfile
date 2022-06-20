#syntax=docker/Dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

ADD . /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "server.py","--host=0.0.0.0", "--reload"]
