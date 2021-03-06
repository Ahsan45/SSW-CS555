#!/usr/bin/env python
__author__ = "Matthew Nuzzo"
import time
from dateutil import parser
#for getting time between dates
from dateutil.relativedelta import relativedelta

def check150(birth, death):
    """Check that age of individual is less than 150"""
    try:
        if birth is None:
            return False
        birth = parser.parse(birth)

        if death is None:
            death = parser.parse(time.strftime("%d %b %Y"))
        else:
            death = parser.parse(death)

        age = relativedelta(death, birth).years
        return age <= 150
    except ValueError:
        return False
