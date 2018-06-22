"""
This module contains tests for the api end points.
"""
from unittest import TestCase
from flask import json
from api.app import APP

class TestRideTestCase(TestCase):
    """
    Tests run for the api end pints.
    """
    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_post_joins_a_ride_offer(self):
        """
        This method tests the joinig of a ride offer
        """

        response = self.client().post('/api/v1/rides/1/requests', data=json.dumps(
            dict(passenger_name="Jack", passenger_id=123, passenger_contact="0771462657"
                )), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("request", response.json)
        self.assertIn("message", response.json)
        self.assertEqual("request sent successfully", response.json['message'])
        self.assertTrue(response.json['request'])
