"""Checks no marriages to descendants"""
def no_marr_to_desc(individuals, family, families):
    husband = family['HUSB']
    wife = family['WIFE']
    descendents = get_desc(individuals, family, families)

    if husband in descendents:
        return False
    elif wife in descendents:
        return False
    else:   
        return True 

def get_desc(individuals, family, allFam):

    children = family['CHIL']


    if children == []:

        return children
    else:
        families = []
        for kid in children:
            if 'FAMS' in individuals[kid]:
                families.append(individuals[kid]['FAMS'])
        if families == []:
            return children
        for fam in families:

            return children + get_lower_desc(fam, allFam)

def get_lower_desc(family, families):

    desc = families[family]['CHIL']
    return desc
