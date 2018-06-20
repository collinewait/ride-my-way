"""
This module provides responses to url requests.
"""
from datetime import datetime
from flask import jsonify
from flask.views import MethodView

class RideViews(MethodView):
    """
    This clas contains methods that respond to various url end points.
    """

    date_time = datetime.now()
    dapart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%X")

    rides = [
        {
            "id": 1, "driver_firstname": "Colline", "driver_lastname": "Wait",
            "destination": "Ntinda", "departure_date": dapart_date,
            "departure_time": depart_time, "number_of_passengers": 2
        },
        {
            "id": 2, "driver_firstname": "Vicky", "driver_lastname": "Von",
            "destination": "Mukon", "departure_date": dapart_date,
            "departure_time": depart_time, "number_of_passengers": 4
        },

    ]

    def get(self, ride_id):
        """
        All ride offers are returned when no ride_id is specified at the end point
        :param ride_id: Ride id
        :return: Json format
        """
        if not ride_id:
            return jsonify({"rides": self.rides})

        return None
