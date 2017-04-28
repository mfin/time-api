# time-api [![Build Status](https://travis-ci.org/mfin/time-api.svg?branch=master)](https://travis-ci.org/mfin/time-api)
Simple "return me time for some place" API

## JSON response
```JSON
$ curl 'https://simple-time-api.herokuapp.com/ljubljana'  # you can throw just about any string at it!

{
    "full_time": "2016-08-24 21:15:34.927857+02:00", 
    "lat": 46.0569465, 
    "lon": 14.5057515, 
    "place": "Ljubljana, Slovenia", 
    "short_time": "21:15", 
    "timezone": "Europe/Ljubljana"
}
```

## Run it with Docker
```
docker build -t time-api .
docker run -d -p 5000:5000/tcp time-api
```
