"""Checks date of birth occurs between marrage of parents"""
import utils

def marr_before_child(ind, family):
    if not family.has_key('MARR'):
        return False
    if not family.has_key('CHIL'):
        return True
    children = family['CHIL']
    return check_children(ind, children, family['MARR'])

"""Extracted method from above into standalone method"""
def check_children(ind, children, date):
    for child in children:
        if (not ind[child].has_key('BIRT')) or utils.date_first(ind[child]['BIRT'], date):
            return False
    return True
