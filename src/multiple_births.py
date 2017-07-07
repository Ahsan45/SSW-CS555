#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if multple births are less than or equal to 5'''

from utils import date_first

def multiple_births(indiv, fam):
    if not 'CHIL' in fam:
        return True

    children =fam['CHIL']

    for child1 in children:
        i = 0
        for child2 in children:
            if indiv[child1]['BIRT'] == indiv[child2]['BIRT']:
                i+=1
            if i == 6:
                return False
    return True