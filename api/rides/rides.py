"""
This module handles specific requsts made
on the API end points
"""
from datetime import datetime
from flask import jsonify, request
from api.rides.ride import Ride
class RidesHandler(object):
    """
    This class contains methods that handle specific
    requests made on the API end point
    Control is obtained from the RidesView class
    """
    date_time = datetime.now()
    dapart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%H:%M")

    rides = [
        Ride(1, "Colline", "Wait", "Ntinda", dapart_date, depart_time, 2),
        Ride(2, "Vicky", "Von", "Mukon", dapart_date, depart_time, 4),
    ]

    def return_all_rides(self):
        """
        This method returns all ride offers made
        returns ride offers in a JSON format
        :return
        """
        return jsonify({"message": "results retrieved successfully",
                        "rides": [x.__dict__ for x in self.rides]})

    def return_single_ride(self, ride_id):
        """
        This remothod returns a single ride offer in
        a JSON format
        :param ride_id: Ride id
        :return
        """
        for ride in self.rides:
            if ride.ride_id == ride_id:
                return jsonify({"Status code": 200, "ride": ride.__dict__,
                                "message": "result retrieved successfully"})
        return jsonify({"Status code": 200, "message": "Ride not found",
                        "error_message": False})

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

        ride = Ride(
            len(self.rides) + 1,
            request.json['driver_firstname'],
            request.json['driver_lastname'],
            request.json['destination'],
            request.json['departure_date'],
            request.json['departure_time'],
            request.json['number_of_passengers']
            )
        self.rides.append(ride)
        return jsonify({"status_code": 201, "ride": ride.__dict__,
                        "message": "Ride added successfully"}), 201
