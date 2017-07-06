"""Module for checking if parents are too old"""
from utils import date_first
from utils import find_age

def husb_not_too_old(fam, indivs):
    """Check if father is too old"""
    if not get_oldest_child_birth(fam, indivs):
        return True
    else:
        husb = fam["HUSB"]
        return find_age(indivs[husb]["BIRT"], get_oldest_child_birth(fam, indivs)) < 80

def wife_not_too_old(fam, indivs):
    """Check if mother is too old"""
    if not get_oldest_child_birth(fam, indivs):
        return True
    else:
        wife = fam["WIFE"]
        return find_age(indivs[wife]["BIRT"], get_oldest_child_birth(fam, indivs)) < 60

def get_oldest_child_birth(fam, indivs):
    """Gets birth date of eldest child or return false"""
    if "CHIL" in fam:
        children = fam["CHIL"]
        oldest_child_birth = indivs[children[0]]["BIRT"]
        for child in children:
            if date_first(indivs[child]["BIRT"], oldest_child_birth):
                oldest_child_birth = indivs[child]["BIRT"]
        return oldest_child_birth
    else:
        return False
