"""Module for checking if birth came before death"""
from utils import date_first

def birth_before_death(indiv):
    """Checks if the individuals birth is before their death"""
    if 'BIRT' not in indiv and 'DEAT' not in indiv:
        return True
    elif 'BIRT' not in indiv:
        return False
    elif 'DEAT' not in indiv:
        return True

    return date_first(indiv['BIRT'], indiv['DEAT'])
