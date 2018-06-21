"""
This module provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView

class RideViews(MethodView):
    """
    This clas contains methods that respond to various url end points.
    """
    rides = []
    def post(self):
        """"
        Handles post requests
        :return:
        """

        ride = {
            "id": len(self.rides) + 1,
            "driver_firstname": request.json['driver_firstname'],
            "driver_lastname": request.json['driver_lastname'],
            "destination": request.json['destination'],
            "departure_date": request.json['departure_date'],
            "departure_time": request.json['departure_time'],
            "number_of_passengers": request.json['number_of_passengers'],
        }
        self.rides.append(ride)
        return jsonify({"status_code": 201, "ride": ride,
                        "message": "Ride added successfully"}), 201
