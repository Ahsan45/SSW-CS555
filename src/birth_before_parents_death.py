"""Module for checking if child is born before death of parents"""
from utils import date_first
from dateutil import parser

def date_within_9mo(date1, date2):
    """Checks if date1 comes 9 months within date2"""
    try:
        date1 = parser.parse(date1, dayfirst=True)
        date2 = parser.parse(date2, dayfirst=True)
        return (date1 - date2).days/30.4 > 9
    except ValueError:
        return False

def birth_before_parents_death(indiv, fam):
    """Returns if mother or father died before birth/conception"""
    if not 'MARR' in fam:
        return False

    if not 'CHIL' in fam:
        return True

    return wife_check(indiv, fam['CHIL'], fam) and husb_check(indiv, fam['CHIL'], fam)

def wife_check(indiv, children, fam):
    """Checks if wife died before birth of child"""
    wife = fam['WIFE']
    if not 'DEAT' in indiv[wife]:
        return True

    for child in children:
        if date_first(indiv[wife]['DEAT'], indiv[child]['BIRT']):
            return False

    return True

def husb_check(indiv, children, fam):
    """Checks if husband died before possible conception of child"""
    husb = fam['HUSB']
    if not 'DEAT' in indiv[husb]:
        return True

    for child in children:
        if date_within_9mo(indiv[child]['BIRT'], indiv[husb]['DEAT']):
            return False

    return True
