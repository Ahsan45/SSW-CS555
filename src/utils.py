"""Module for storing misc. utility functions"""
from dateutil import parser
from dateutil.relativedelta import relativedelta

def date_first(date1, date2):
    """Checks if date1 comes before date2"""
    date1 = parser.parse(date1)
    date2 = parser.parse(date2)

    return relativedelta(date2, date1).days >= 0

def find_age(start, end):
    """Parse strings as date objects and compare them to get age"""
    start = parser.parse(start)
    end = parser.parse(end)

    return relativedelta(end, start).years
