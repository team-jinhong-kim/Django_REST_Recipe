FROM python:3.7-alpine
MAINTAINER Jake Kim

# Disable python output buffer
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Create "app" Directory
RUN mkdir /app
# Switch Default Working Directory
WORKDIR /app
copy ./app .app

# Security configurtation
# -D: permission : Running only

RUN adduser -D user
USER user
