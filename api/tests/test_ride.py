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

    def test_api_gets_all_ride_offers(self):
        """Test API can get all ride offers (GET request)."""
        response = self.client().get('/api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("rides", response.json)
        self.assertIsInstance(response.json['rides'], list)
        self.assertTrue(response.json["rides"])
        self.assertIsInstance(response.json["rides"][0], dict)
        self.assertIn(1, response.json["rides"][0].values())
        self.assertIn(2, response.json["rides"][1].values())
