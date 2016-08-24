FROM python:3.5.2-alpine
MAINTAINER Matjaž Finžgar <matjaz@finzgar.net>

WORKDIR /app

RUN apk --update add openssl ca-certificates

COPY . /app
RUN pip install -r /app/requirements.txt

EXPOSE 5000
CMD [ "python", "time-api.py" ]
