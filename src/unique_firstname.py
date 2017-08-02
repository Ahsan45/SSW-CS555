#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if all first names are unique'''

def unique_firstname(indiv, fam):
    if not 'CHIL' in fam:
        return True

    children = fam['CHIL']

    for child1 in children:
        i = 0
        for child2 in children:
            if child1 in indiv and child2 in indiv and indiv[child1]['NAME'] == indiv[child2]['NAME'] and indiv[child1]['BIRT'] == indiv[child2]['BIRT']:
                i+=1
            if i == 2:
                return False
    return True