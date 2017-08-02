"""Module for validating dates"""
from dateutil import parser

def valid_date(date):
    """Returns true if a date is valid"""
    try:
        parser.parse(date)
        return True
    except ValueError:
        return False
