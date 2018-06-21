"""
This module contains tests for the api end points.
"""
from unittest import TestCase
from datetime import datetime
from flask import json
from api.app import APP

class TestRideTestCase(TestCase):
    """
    Tests run for the api end pints.
    """
    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_post_creates_a_ride_offer(self):
        """
        This method tests for the creation of a ride offer
        """
        date_time = datetime.now()
        depart_date = date_time.strftime("%x")
        depart_time = date_time.strftime("%X")

        response = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver_firstname="Jack", driver_lastname="Ma", destination="Mbarara",
                 departure_date=depart_date, departure_time=depart_time,
                 number_of_passengers=2)), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("ride", response.json)
        self.assertIn("message", response.json)
        self.assertEqual("Ride added successfully", response.json['message'])
        self.assertTrue(response.json['ride'])

    def test_non_json_data_not_sent(self):
        """
        This method tests that non json data is not sent
        """
        date_time = datetime.now()
        depart_date = date_time.strftime("%x")
        depart_time = date_time.strftime("%X")

        response = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver_firstname="Jack", driver_lastname="Ma", destination="Mbarara",
                 departure_date=depart_date, departure_time=depart_time,
                 number_of_passengers=2)), content_type='text/plain')

        self.assertEqual(response.status_code, 400)
        self.assertIn("error_message", response.json)
        self.assertEqual("content not JSON", response.json['error_message'])
        self.assertTrue(response.json)