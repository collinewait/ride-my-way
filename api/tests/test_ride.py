"""
This module contains tests for the api end points.
"""
from unittest import TestCase
from datetime import datetime
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

    def test_all_ride_keys_returned(self):
        """
        Test an item is returned with all the expected keys on the ride dictionary
        """
        response = self.client().get('/api/v1/rides/1')
        self.assertIn("id", response.json['ride'])
        self.assertIn("driver_firstname", response.json['ride'])
        self.assertIn("driver_lastname", response.json['ride'])
        self.assertIn("destination", response.json['ride'])
        self.assertIn("departure_date", response.json['ride'])
        self.assertIn("departure_time", response.json['ride'])
        self.assertIn("number_of_passengers", response.json['ride'])

    def test_all_ride_values_returned(self):
        """
        Test all values expected  in a ride dictionary are returned
        """
        date_time = datetime.now()
        depart_date = date_time.strftime("%x")
        depart_time = date_time.strftime("%X")
        response = self.client().get('/api/v1/rides/1')
        self.assertIn(1, response.json['ride'].values())
        self.assertIn("Colline", response.json['ride'].values())
        self.assertIn("Wait", response.json['ride'].values())
        self.assertIn("Ntinda", response.json['ride'].values())
        self.assertIn(2, response.json['ride'].values())
        self.assertIn(depart_date, response.json['ride'].values())
        self.assertIn(depart_time, response.json['ride'].values())

    def test_ride_not_found(self):
        """
        Test API returns nothing when a ride is not found
        A return contsins a status code of 200
        """
        response = self.client().get('/api/v1/rides/20')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertIn("Ride not found", response.json.values())
        self.assertIn(False, response.json.values())

    def test_error_hander_returns_json(self):
        """
        Test API returns a json format response when the user hits
        a wrong api end point
        """
        response = self.client().get('/api/v1/rides/me')
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error_message", response.json)
        self.assertIn("status_code", response.json)
        self.assertIn("url", response.json)
        self.assertIn("The requested resource was not found on the server",
                      response.json.values())
        self.assertIn(404, response.json.values())
        self.assertIn("http://localhost/api/v1/rides/me",
                      response.json.values())
