"""Module for storing misc. utility functions"""
from dateutil import parser
from dateutil.relativedelta import relativedelta

def date_first(date1, date2):
    """Checks if date1 comes before date2"""
    date1 = parser.parse(date1)
    date2 = parser.parse(date2)

    return relativedelta(date2, date1).days >= 0

def find_age(start, end):
    """Parse strings as date objects and compare them to get age"""
    start = parser.parse(start)
    end = parser.parse(end)

    return relativedelta(end, start).years

def get_parents(key, indivs, fams):
    """Get parents of an individual"""
    if 'FAMC' in indivs[key]:
        return [fams[indivs[key]['FAMC']]['HUSB'], fams[indivs[key]['FAMC']]['WIFE']]
    else:
        return []

def get_siblings(key, indivs, fams):
    """Get siblings of an individual"""
    if 'FAMC' in indivs[key]:
        return [x for x in fams[indivs[key]['FAMC']]['CHIL'] if not x == key]
    else:
        return []

def get_spouses(key, indivs, fams):
    """Get spouses of an individual"""
    if 'FAMS' in indivs[key]:
        return reduce(lambda x, y: x + [fams[y]['HUSB'] if indivs[key]['SEX'] == 'F' else fams[y]['WIFE']], indivs[key]['FAMS'], [])
    else:
        return []

def get_children(key, indivs, fams):
    """Get children of an individual"""
    if 'FAMS' in indivs[key]:
        return reduce(lambda x, y: x + fams[y]['CHIL'] if 'CHIL' in fams[y] else [], indivs[key]['FAMS'], [])
    else:
        return []

def get_nieces_and_nephews(key, indivs, fams):
    """Get nieces and nephews of an individual"""
    siblings = get_siblings(key, indivs, fams)
    if len(siblings) > 0:
        return reduce(lambda x, y: x + get_children(y, indivs, fams), siblings, [])
    else:
        return []

def get_cousins(key, indivs, fams):
    """Get first cousins of an individual"""
    parents = get_parents(key, indivs, fams)
    if len(parents) > 0:
        aunts_uncles = reduce(lambda x, y: x + get_siblings(y, indivs, fams), parents, [])
        if len(aunts_uncles) > 0:
            return reduce(lambda x, y: x + get_children(y, indivs, fams), aunts_uncles, [])
        else:
            return []
    else:
        return []
