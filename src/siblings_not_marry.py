"""Module for checking if both spouses are not siblings"""
from utils import *

def siblings_not_marry(key, indivs, fams):
    """Check that an individual has not married their sibling"""
    siblings = get_siblings(key, indivs, fams)
    spouses = get_spouses(key, indivs, fams)
    return set(spouses).isdisjoint(siblings)