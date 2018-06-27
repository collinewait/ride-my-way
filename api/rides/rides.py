"""
This module handles specific requsts made
on the API end points
"""
from datetime import datetime
from flask import jsonify, request
from api.rides.ride import Ride
from api.rides.user import User
class RidesHandler(object):
    """
    This class contains methods that handle specific
    requests made on the API end point
    Control is obtained from the RidesView class
    """
    date_time = datetime.now()
    dapart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%H:%M")

    user1 = User("Colline", "Wait", "coll@wait.com", "0771462657", "1234")
    user2 = User("Vicky", "Von", "vic@vom.com", "0771658399", "1234")

    rides = [
        Ride(1, user1.first_name, user1.last_name, "Ntinda", dapart_date, depart_time, 2),
        Ride(2, user2.first_name, user2.last_name, "Mukon", dapart_date, depart_time, 4),
    ]

    requests = []

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
        return jsonify({}), 204

    def post_ride_offer(self):
        """
        This method saves a ride offer when a ride_id is not set
        It takes control from the post() method
        :return
        """
        keys = ("driver_firstname", "driver_lastname", "destination",
                "departure_date", "departure_time", "number_of_passengers")
        if not set(keys).issubset(set(request.json)):
            return self.request_missing_fields()

        request_condition = [
            request.json["driver_firstname"], request.json["driver_lastname"],
            request.json["destination"], request.json["departure_date"],
            request.json["departure_time"],
            request.json["number_of_passengers"]
            ]

        if not all(request_condition):
            return self.fields_missing_info()

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

    def post_request_to_ride_offer(self, ride_id):
        """
        This method saves a request to a ride offer when a ride_id is set
        It takes control from the post() method
        :return
        """
        request_keys = ("passenger_name", "passenger_id", "passenger_contact")
        if not set(request_keys).issubset(set(request.json)):
            return self.request_missing_fields()

        if not request.json["passenger_name"] or not request.json["passenger_id"]\
            or not request.json["passenger_contact"]:
            return self.fields_missing_info()

        for ride in self.rides:
            if ride.ride_id == ride_id:
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

        return jsonify({}), 204

    @staticmethod
    def fields_missing_info():
        """
        This method returns a JSON response when some fields in
        the data sent are missing
        :return
        """
        return jsonify({"status_code": 400, "data": request.json,
                        "error_message": "Some fields are empty"}), 400
    @staticmethod
    def request_missing_fields():
        """
        This method returns a JSON response when containg the
        error message that some fields are missing
        :return
        """
        return jsonify({"error_message": "some of these fields are missing"}), 400
