"""Module for listing all living married individuals"""

def living_married(indivs):
    for key in sorted(indivs.keys()):
        if not 'DEAT' in indivs[key]:
            if 'FAMS' in indivs[key]:
                print("{}: {}".format(key, indivs[key]['NAME']))