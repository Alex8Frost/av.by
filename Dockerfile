FROM python:3.11

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt