"""Checks date of birth occurs between marrage of parents"""
import utils

def marr_before_child(ind, family):
    if 'MARR' not in family:
        return False
    if 'CHIL' not in family:
        return True
    children = family['CHIL']
    return check_children(ind, children, family['MARR'])

"""Extracted method from above into standalone method"""
def check_children(ind, children, date):
    for child in children:
        if ('BIRT' not in ind[child]) or utils.date_first(ind[child]['BIRT'], date):
            return False
    return True
