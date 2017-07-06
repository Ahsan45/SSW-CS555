"""Checks Male Last Names"""

def male_last_names(inds, males):
    lastNames = []
    for male in males:
        lastNames.append(get_last_name(inds, male))
    #print lastNames    
    return len(set(lastNames))==1

def get_last_name(people, individual):
    surname = people[individual]['NAME'].split()
    #print surname
    return surname[1]

def get_males(families, people):
    #print families
        
    familyMen = []
    familyMen.append(families['HUSB'])
    children = []
    children = families['CHIL']
    #print children
    for kid in children:
        if people[kid]['SEX'] == 'M':
            familyMen.append(kid)
    #print familyMen  
    return familyMen
