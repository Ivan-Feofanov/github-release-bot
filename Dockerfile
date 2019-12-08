FROM python:alpine3.10

RUN apk add python3-dev build-base

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN gcc -v
RUN pip install pipenv
RUN pipenv install -d

ENTRYPOINT ["pipenv", "run", "uvicorn", "main:app"]