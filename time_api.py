#!/usr/bin/env python


from flask import Flask
from flask_restful import Resource, Api, abort
from datetime import datetime
from geopy import geocoders

app = Flask(__name__)
api = Api(app)


class ReturnTime(Resource):
    def get(self, location):
        g = geocoders.GoogleV3()
        geo_object = g.geocode(location)

        if not geo_object:
            abort(404, message="Location {} is unknown.".format(location))

        place, (lat, lon) = geo_object
        timezone = g.timezone((lat, lon))
        full_time = datetime.now(timezone)
        short_time = full_time.strftime("%H:%M")

        return {"place": place,
                "timezone": str(timezone),
                "full_time": str(full_time),
                "short_time": short_time,
                "lat": lat,
                "lon": lon
               }

api.add_resource(ReturnTime, '/<string:location>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
