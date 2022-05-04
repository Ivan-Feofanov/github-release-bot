FROM python:3.11.0a7-slim

RUN apk add python3-dev build-base

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN gcc -v
RUN pip install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
