"""Module for checking if birth came before marriage"""
from utils import date_first

def birth_before_marr_husb(fam, indiv):
    """Checks if husband's birth is before marriage"""
    husb = fam['HUSB']
    return date_first(indiv[husb]['BIRT'], fam['MARR'])

def birth_before_marr_wife(fam, indiv):
    """Checks if wife's birth is before marriage"""
    wife = fam['WIFE']
    return date_first(indiv[wife]['BIRT'], fam['MARR'])
