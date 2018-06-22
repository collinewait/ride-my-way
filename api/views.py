"""
This module provides responses to url requests.
"""
from datetime import datetime
from flask import jsonify, request
from flask.views import MethodView

class RideViews(MethodView):
    """
    This class contains methods that respond to various url end points.
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
            return jsonify({"error_message": False, "rides": self.rides})

        for ride in self.rides:
            if ride['id'] == ride_id:
                return jsonify({"Status code": 200, "ride": ride, "error_message": False})

        return jsonify({"Status code": 200, "message": "Ride not found",
                        "error_message": False})
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
