"""
This module is a ride model with its attributes
"""
class User(object):
    """
    This class represents a User entity
    """
    def __init__(self, *args):
        self.first_name = args[0]
        self.last_name = args[1]
        self.email_address = args[2]
        self.phone_number = args[3]
        self.password = args[4]
