"""Module for checking if birth came before death"""
from dateutil import parser
from dateutil.relativedelta import relativedelta

def date_first(date1, date2):
    """Checks if date1 comes before date2"""
    date1 = parser.parse(date1)
    date2 = parser.parse(date2)

    return relativedelta(date2, date1).days >= 0

def birth_before_death(indiv):
    """Checks if the individuals birth is before their death"""
    if not indiv.has_key('BIRT') and not indiv.has_key('DEAT'):
        return True
    elif not indiv.has_key('BIRT'):
        return False
    elif not indiv.has_key('DEAT'):
        return True

    return date_first(indiv['BIRT'], indiv['DEAT'])
