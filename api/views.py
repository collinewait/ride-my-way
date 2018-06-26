"""
This module provides responses to url requests.
"""
from datetime import datetime
from flask import jsonify, request
from flask.views import MethodView
from api.rides.rides import RidesHandler

class RideViews(MethodView):
    """
    This class contains methods that respond to various url end points.
    """
    date_time = datetime.now()
    dapart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%H:%M")

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

    requests = []

    rides_handler = RidesHandler()

    def get(self, ride_id):
        """
        All ride offers are returned when no ride_id is specified at the end point
        :param ride_id: Ride id
        :return: Json format
        """
        if not ride_id:
            return self.rides_handler.return_all_rides()

        for ride in self.rides:
            if ride['id'] == ride_id:
                return jsonify({"Status code": 200, "ride": ride,
                                "message": "result retrieved successfully"})

        return jsonify({"Status code": 200, "message": "Ride not found",
                        "error_message": False})
    def post(self, ride_id):
        """"
        Handles post requests
        saves a ride offer if ride_id is not set
        and saves a request to a ride if ride_id is set
        :return:
        """
        if not request or not request.json:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "content not JSON"}), 400

        if ride_id:

            return self.post_request_to_ride_offer(ride_id)

        return self.post_ride_offer()

    def post_ride_offer(self):
        """
        This method saves a ride offer when a ride_id is not set
        It takes control from the post() method
        :return
        """
        keys = ("driver_firstname", "driver_lastname", "destination",
                "departure_date", "departure_time", "number_of_passengers")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"error_message": "some of these fields are missing"}), 400

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

    def post_request_to_ride_offer(self, ride_id):
        """
        This method saves a request to a ride offer when a ride_id is set
        It takes control from the post() method
        :return
        """
        if not request.json["passenger_name"] or not request.json["passenger_id"]\
            or not request.json["passenger_contact"]:
            return jsonify({"status_code": 400, "data": request.json,
                            "error_message": "Some fields are empty"}), 400

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
