"""Module for checking for corresponding entries"""

def corresponding_indiv(key, indiv, fams):
    """Check for corresponding entries to indiv entries"""
    if 'FAMC' in indiv:
        if not key in fams[indiv['FAMC']]['CHIL']: return False
    if 'FAMS' in indiv:
        for fam in indiv['FAMS']:
            if indiv['SEX'] == 'M':
                if not key == fams[fam]['HUSB']: return False
            else:
                if not key == fams[fam]['WIFE']: return False
    return True


def corresponding_fam(key, fam, indivs):
    """Check for corresponding entries to fam entries"""
    if 'HUSB' in fam:
        if not fam['HUSB'] in indivs or not indivs[fam['HUSB']]['FAMS'] == key: return False
    if 'WIFE' in fam:
        if not fam['WIFE'] in indivs or not indivs[fam['WIFE']]['FAMS'] == key: return False
    if 'CHIL' in fam:
        for child in fam['CHIL']:
            if not child in indivs or not indivs[child]['FAMC'] == key: return False
    return True
