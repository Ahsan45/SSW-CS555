'''module for finding individuals who are deceased'''
def print_deceased(people):
    deadPeople = {}

    for key in sorted(people.iterkeys()):
        if 'DEAT' in people[key]:
            deadPeople[key] = people[key]['DEAT']
    print deadPeople
    return deadPeople
