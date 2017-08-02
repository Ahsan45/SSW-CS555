"""Checks no marriages to descendants"""

def no_marr_to_desc(individuals, family, families):
    """Main function to check children/descendents against Husband/Wife of family"""
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
    """Function finds children within family, calls get_lower_desc if grandchildren found"""
    if 'CHIL' in family:    
        children = family['CHIL']
    else:
        children = [] 

    if children == []:
        return children
    else:
        families = []
        for kid in children:
            if kid in individuals and 'FAMS' in individuals[kid]:
                families.extend(individuals[kid]['FAMS'])
        if families == []:
            return children
        for fam in map(str, families):

            return children + get_lower_desc(fam, allFam)

def get_lower_desc(family, families):
    """Function finds children, called by get_desc when looking for grandchildren/great-grandchildren"""
    desc = []
    if 'CHIL 'in family:
        desc.extend(families[family]['CHIL'])
    return desc
