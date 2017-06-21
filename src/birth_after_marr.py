"""Checks date of birth occurs between marrage of parents"""
from dateutil.relativedelta import *
from dateutil import parser 
import utils

def marr_before_child(ind, family):
    if not family.has_key('MARR'):
        return False
    if not family.has_key('CHIL'):
        return True
    marrDate = family['MARR']
    children = family['CHIL']
    for child in children:
        if (not ind[child].has_key('BIRT')) or utils.date_first(ind[child]['BIRT'],marrDate):
            return False
    return True
