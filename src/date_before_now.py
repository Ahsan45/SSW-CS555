"""Module for checking if date came before current date"""
import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

def date_past(date1):
    today = datetime.datetime.now().date()
    date1 = parser.parse(date1)

    return relativedelta(today, date1).days >= 0

def birth_before_now(indiv):
    if not 'BIRT' in indiv:
        return True

    return date_past(indiv['BIRT'])

def death_before_now(indiv):
    if not 'DEAT' in indiv:
        return True

    return date_past(indiv['DEAT'])

def marr_before_now(fams):
    if not 'MARR' in fams:
        return True

    return date_past(fams['MARR'])

def div_before_now(fams):
    if not 'DIV' in fams:
        return True

    return date_past(fams['DIV'])
