"""
This module provides responses to url requests.
"""
from datetime import datetime
from flask import jsonify, request
from flask.views import MethodView

class RideViews(MethodView):
    """
    This clas contains methods that respond to various url end points.
    """
    date_time = datetime.now()
    depart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%X")
    rides = [
        {
            "id": 1, "driver_firstname": "Colline", "driver_lastname": "Wait",
            "destination": "Ntinda", "departure_date": depart_date,
            "departure_time": depart_time, "number_of_passengers": 2
        },
        {
            "id": 2, "driver_firstname": "Vicky", "driver_lastname": "Von",
            "destination": "Mukon", "departure_date": depart_date,
            "departure_time": depart_time, "number_of_passengers": 4
        },
    ]

    requests = []

    def post(self, ride_id):
        """
        This method handles requests made to join a ride
        :retun:
        """
        if not request or not request.json:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "content not JSON"}), 400

        for ride in self.rides:
            if ride['id'] == ride_id:
                ride_request = {
                    "request_id": len(self.requests) + 1,
                    "ride_id": ride_id,
                    "passenger_name": request.json['passenger_name'],
                    "passenger_id": request.json['passenger_id'],
                    "passenger_contact": request.json['passenger_contact'],
                }
                self.requests.append(ride_request)
                return jsonify({"Status code": 201, "request": ride_request,
                                "message": "request sent successfully"}), 201

        return jsonify({"Status code": 202, "error_message": "Ride not found",}), 202
