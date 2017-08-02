"""Module for listing all living single individuals above 30"""
import utils
import time

def living_single(indivs):
    for key in sorted(indivs.keys()):
        if not 'DEAT' in indivs[key]:
            if not 'FAMS' in indivs[key]:
                if utils.find_age(indivs[key]['BIRT'], time.strftime("%m %d %Y")) >= 30:
                    print("{}: {}".format(key, indivs[key]['NAME']))