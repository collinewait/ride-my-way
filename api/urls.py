"""
This module handels requests to urls.
"""
from api.views import RideViews

class Urls(object):
    """
   Class to generate urls
    """
    @staticmethod
    def generate_url(app):
        """
         Generates urls on the app context
        :param: app: takes in the app variable
        :return: urls
        """
        ride_view = RideViews.as_view('ride_api')
        app.add_url_rule('/api/v1/rides/', view_func=ride_view, methods=['POST',])
