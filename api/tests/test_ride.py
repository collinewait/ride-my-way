"""
This module contains tests for the api end points.
"""
from unittest import TestCase
from api.app import APP
class TestRideTestCase(TestCase):
    """
    Tests run for the api end pints.
    """
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client

    def test_get_one_ride_offer(self):
        """
        Test an item is returned on a get request
        :return:
        """
        response = self.client().get('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("ride", response.json)
        self.assertIn(False, response.json.values())
        self.assertIn("error_message", response.json)
        self.assertIsInstance(response.json['ride'], dict)
        self.assertEqual(len(response.json['ride']), 7)
