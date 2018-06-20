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
