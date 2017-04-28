FROM python:3.6.1-alpine
MAINTAINER Matjaž Finžgar <matjaz@finzgar.net>

WORKDIR /app

RUN apk --update add openssl ca-certificates

COPY . /app
RUN pip install -r /app/requirements.txt

EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", ":5000", "time_api:app"]
