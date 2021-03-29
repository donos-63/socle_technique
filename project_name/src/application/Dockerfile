# This is a simple Dockerfile to use while developing
# It's not suitable for production

FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt setup.py tox.ini ./
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -e .

COPY myapi myapi/
COPY migrations migrations/

EXPOSE 5000
