#Erik Lim
#SSW 555 Agile Methods for Software Development

"""Module for checking if marriage came before death"""
from utils import date_first

def divorce_before_death_husb(fam, indiv):
    """Checks that divorce is before death of husband"""
    if not 'DIV' in fam:
        return True

    husb = fam['HUSB']
    if not 'DEAT' in indiv[husb]:
        return True

    return date_first(fam['DIV'], indiv[husb]['DEAT'])

def divorce_before_death_wife(fam, indiv):
    """Checks that divorce is before death of wife"""
    if not 'DIV' in fam:
        return True

    wife = fam['WIFE']
    if not 'DEAT' in indiv[wife]:
        return True

    return date_first(fam['DIV'], indiv[wife]['DEAT'])
