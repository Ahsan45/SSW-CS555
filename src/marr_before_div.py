"""Module for checking if marriage came before divorce"""
from utils import date_first

def marr_before_div(fam):
    """Checks if the family's marriage is before its divorce"""
    if 'MARR' not in fam and 'DIV' not in fam:
        return True
    elif 'MARR' not in fam:
        return False
    elif 'DIV' not in fam:
        return True

    return date_first(fam['MARR'], fam['DIV'])
