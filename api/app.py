"""
Main root app of the api
"""

import sys
import os

from flask import Flask
from flask_cors import CORS

sys.path.append(os.path.pardir)

from api.config import HOST, PORT, DEBUG, ENVIRONMENT, TESTING
from api.urls import Urls

APP = Flask(__name__)
APP.testing = TESTING
APP.env = ENVIRONMENT

Urls.generate_url(APP)

CORS(APP)
if __name__ == '__main__':
    APP.run(debug=DEBUG, host=HOST, port=PORT)
