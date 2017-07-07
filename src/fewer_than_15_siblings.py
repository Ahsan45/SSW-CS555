#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if mthere are fewer than 15 siblings in a family'''

from utils import date_first

def fewer_than_15_siblings(fam):
    if 'CHIL' in fam:
        return len(fam['CHIL']) < 15
    return True