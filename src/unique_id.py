"""Module to check if all Individual/family ID's unique"""
from collections import Counter

def unique_id(people):
    rawIDs = get_ID(people)
    
    return check_id(rawIDs, people)
    
def check_id(ID, people):
    if len(ID) < len(people):  
        return False
    
    return True

def check_ID_conflict(args, objects):
    """Function to check BDay of conflicted ID's. If BDays match, it will be assumed that conflict
    arose from name change, marriage, etc."""
    bday = []
    for key in objects.iterkeys():
        bday.append(key['BIRT'])
    if len(bday)>len(set(bday)):
        return False
    else:
        return True
