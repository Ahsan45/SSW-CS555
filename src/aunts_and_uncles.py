"""Module for checking that aunts and uncles have not married their nieces and nephews"""

def get_children(key, indivs, fams):
    """Get children of an individual"""
    if 'FAMS' in indivs[key]:
        return reduce(lambda x, y: x + fams[y]['CHIL'] if 'CHIL' in fams[y] else [], indivs[key]['FAMS'], [])
    else:
        return []

def get_nieces_and_nephews(key, indivs, fams):
    """Get nieces and nephews of an individual"""
    if 'FAMC' in indivs[key]:
        siblings = [x for x in fams[indivs[key]['FAMC']]['CHIL'] if not x == key]
        return reduce(lambda x, y: x + get_children(y, indivs, fams), siblings, [])
    else:
        return []

def get_spouses(key, indivs, fams):
    """Get spouses of an individual"""
    if 'FAMS' in indivs[key]:
        return reduce(lambda x, y: x + [fams[y]['HUSB'] if indivs[key]['SEX'] == 'F' else fams[y]['WIFE']], indivs[key]['FAMS'], [])
    else:
        return []

def aunts_and_uncles(key, indivs, fams):
    """Check that aunts and uncles have not married their nieces and nephews"""
    nieces_nephews = get_nieces_and_nephews(key, indivs, fams)
    spouses = get_spouses(key, indivs, fams)
    return set(spouses).isdisjoint(nieces_nephews)
