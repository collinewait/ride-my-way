"""
This module handles specific requsts made
on the API end points
"""
from datetime import datetime
from flask import jsonify
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
        returns ride offers in a json format
        :return
        """
        return jsonify({"message": "results retrieved successfully",
                        "rides": [x.__dict__ for x in self.rides]})
