FROM python:3.8.1-alpine3.11

RUN apk add --no-cache alpine-sdk \
    mysql-client \
    mysql-dev \
    build-base \
    bash \
    tzdata
