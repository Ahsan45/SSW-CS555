#!/usr/bin/env python
__author__ = "Matthew Nuzzo"
from datetime import datetime
import time
#for getting time between dates
from dateutil.relativedelta import *
from dateutil import parser 

def getDates(person):
    birthday = None
    death = None
    if person.has_key("BIRT") and person.has_key("DEAT"):
        birthday = person["BIRT"]
        death = person["DEAT"]
    elif person.has_key("BIRT"):
        birthday = person["BIRT"]
        death = time.strftime("%d/%m/%Y")
    return birthday, death

def check150(birth, death):
    if birth is None:
        return False	
    birth = parser.parse(birth)
    if death is None:
        death = parser.parse(time.strftime("%d %b %Y"))
        age = relativedelta(death.date(), birth.date()).years
        if age <= 150:
            return True
        else:
            return False
    else:
        death = parser.parse(death)	
        age = relativedelta(death, birth).years
        if age <= 150:
    	    return True
        else:
    	    return False
#print check150('09-04-1996','06-09-2017')



