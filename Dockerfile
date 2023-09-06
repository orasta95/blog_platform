FROM python:3.11-alpine

LABEL maintainer = "github/orasta95"

RUN mkdir app/

COPY ./docker-project/ app/

EXPOSE 8000

RUN python3 -m venv .venv/ &&\
    /.venv/bin/pip install --upgrade pip &&\
    apt --update &&\