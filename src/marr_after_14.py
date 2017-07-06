"""Module for checking if both spouses are at least 14 when married"""
from utils import find_age
import time

def husb_marr_after_14(indiv, fam):
    """Checks if husband is older than 14 when married"""
    if not 'MARR' in fam:
        return False
    
    husb = fam['HUSB']
    return find_age(indiv[husb]['BIRT'], fam['MARR']) >= 14
    
def wife_marr_after_14(indiv, fam):
    """Checks if wife is older than 14 when married"""
    if not 'MARR' in fam:
        return False
    
    wife = fam['WIFE']
    return find_age(indiv[wife]['BIRT'], fam['MARR']) >= 14