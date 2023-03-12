FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt