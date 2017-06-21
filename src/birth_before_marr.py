"""Module for checking if birth came before marriage"""
from utils import date_first

def birth_before_marr_husb(fam, indiv):
    husb = fam['HUSB']

    return date_first(indiv[husb]['BIRT'], fam['MARR'])

def birth_before_marr_wife(fam, indiv):
    wife = fam['WIFE']

    return date_first(indiv[wife]['BIRT'], fam['MARR'])