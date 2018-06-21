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
        if not request or not request.json:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "content not JSON"}), 400

        if not request.json["driver_firstname"] or not request.json["driver_lastname"]\
                or not request.json["destination"]:
            return jsonify({"status_code": 400, "data": request.json,
                            "error_message": "Some fields are empty"}), 400

        if not request.json["departure_date"] or not request.json["departure_time"]\
                 or not request.json["number_of_passengers"]:

            return jsonify({"status_code": 400, "data": request.json,
                            "error_message": "Some fields are empty"}), 400

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
