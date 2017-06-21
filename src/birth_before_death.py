"""Module for checking if birth came before death"""
from utils import date_first

def birth_before_death(indiv):
    """Checks if the individuals birth is before their death"""
    if not indiv.has_key('BIRT') and not indiv.has_key('DEAT'):
        return True
    elif not indiv.has_key('BIRT'):
        return False
    elif not indiv.has_key('DEAT'):
        return True

    return date_first(indiv['BIRT'], indiv['DEAT'])
