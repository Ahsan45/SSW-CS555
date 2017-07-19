#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if all the families are unique by spouses'''

from collections import Counter

def unique_family(key, fams):
    for family in fams:
        if key['HUSB'] == family['HUSB'] and key['WIFE'] == family['WIFE'] and key['MARR'] == family['MARR']
            return False

    return True
