"""Module for checking if date came before current date"""
import time
from utils import date_first

def date_past(date):
    """Helper function for comparing date to now"""
    today = time.strftime("%d %b %Y")

    return date_first(date, today)

def birth_before_now(indiv):
    """Checks if birth occurred in the past"""
    if not 'BIRT' in indiv:
        return True

    return date_past(indiv['BIRT'])

def death_before_now(indiv):
    """Checks if death occurred in the past"""
    if not 'DEAT' in indiv:
        return True

    return date_past(indiv['DEAT'])

def marr_before_now(fams):
    """Checks if marriage occurred in the past"""
    if not 'MARR' in fams:
        return True

    return date_past(fams['MARR'])

def div_before_now(fams):
    """Checks if divorce occurred in the past"""
    if not 'DIV' in fams:
        return True

    return date_past(fams['DIV'])
