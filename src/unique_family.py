#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if all the families are unique by spouses'''

from collections import Counter

def unique_family(family, fams):
    for key in sorted(fams.keys()):
        if family != key:
            if fams[family]['HUSB'] == fams[key]['HUSB'] and fams[family]['WIFE'] == fams[key]['WIFE'] and fams[family]['MARR'] == fams[key]['MARR']:
                return False

    return True
