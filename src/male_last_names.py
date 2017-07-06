"""Checks Male Last Names"""

def male_last_names(inds, males):
    """Checks male last names, returns appropriate Boolean for if all male last names consistent"""
    lastNames = []
    for male in males:
        lastNames.append(get_last_name(inds, male)) 
    return len(set(lastNames))==1

def get_last_name(people, individual):
    """Finds last name from Individual dictionary"""
    surname = people[individual]['NAME'].split()
    return surname[1]

def get_males(families, people):
    """Finds all males in family: Husband and any children who have 'SEX' of 'M'"""
        
    familyMen = []
    familyMen.append(families['HUSB'])
    children = []
    children = families['CHIL']
    for kid in children:
        if people[kid]['SEX'] == 'M':
            familyMen.append(kid) 
    return familyMen
