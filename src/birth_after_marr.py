"""Checks date of birth occurs between marrage of parents"""
import utils

def marr_before_child(ind, family):
    """Checks that marriage was before birth of children"""
    if 'MARR' not in family:
        return False
    if 'CHIL' not in family:
        return True
    children = family['CHIL']
    return check_children(ind, children, family['MARR'])

def check_children(ind, children, date):
    """Helper function to check birth of each child"""
    for child in children:
        if (child not in ind or 'BIRT' not in ind[child]) or utils.date_first(ind[child]['BIRT'], date):
            return False
    return True
