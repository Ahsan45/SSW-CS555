"""Module for checking if parents are too old"""
from utils import date_first
from utils import find_age

def parents_not_too_old(fam, indivs):
    """Checks if mothers and fathers are 60 and 80 years older than their children respectively"""
    husb = fam["HUSB"]
    wife = fam["WIFE"]

    if "CHIL" in fam:
        children = fam["CHIL"]
        oldest_child_birth = indivs[children[0]]["BIRT"]
        for child in children:
            if date_first(indivs[child]["BIRT"], oldest_child_birth):
                oldest_child_birth = indivs[child]["BIRT"]
    else:
        return True

    return (find_age(indivs[husb]["BIRT"], oldest_child_birth) < 60 and
            find_age(indivs[wife]["BIRT"], oldest_child_birth) < 80)
