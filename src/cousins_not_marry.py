"""Module for checking that first cousins have not married"""
from utils import *

def cousins_not_marry(key, indivs, fams):
    """Checks that an individual has not married one of their cousins"""
    cousins = get_cousins(key, indivs, fams)
    spouses = get_spouses(key, indivs, fams)
    return set(spouses).isdisjoint(cousins)
