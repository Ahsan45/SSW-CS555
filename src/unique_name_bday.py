"""Module to check if name and birthdays unique in GEDCOM"""
def unique_name_bday(individual, individuals):
    return check_bday(individual, individuals)
    
def check_bday(individual, people):
    bdays = []
    for key in sorted(people.iterkeys()):
        bdays.append(people[key]['BIRT'])
    
    if bdays.count(individual['BIRT']) > 1:
        check_names(individual,people)
        print individual
    else:
        return True

def check_names(person, people):
    names = []    
    for person in people:
        names.append(people[person]['NAME'])
    print people[person]['NAME']
    print names.count(people[person]['NAME'])
    if names.count(people[person]['NAME']) > 1:
        return False
    else:
        return True

        
