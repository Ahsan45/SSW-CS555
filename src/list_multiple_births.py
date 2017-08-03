#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for listing multiple births'''

def list_multiple_births(indiv):
    list_birth = {}
    for key1 in sorted(indiv.keys()):
        i = 0
        for key2 in sorted(indiv.keys()):
            if indiv[key1]['BIRT'] == indiv[key2]['BIRT']:
                i+=1
            if i == 2:
                if key1 not in list_birth:
                    list_birth[key1] = {}

    print("\n".join(list_birth))