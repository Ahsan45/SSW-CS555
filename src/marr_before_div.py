"""Module for checking if marriage came before divorce"""
from utils import date_first

def marr_before_div(fam):
    """Checks if the family's marriage is before its divorce"""
    if not fam.has_key('MARR') and not fam.has_key('DIV'):
        return True
    elif not fam.has_key('MARR'):
        return False
    elif not fam.has_key('DIV'):
        return True

    return date_first(fam['MARR'], fam['DIV'])
