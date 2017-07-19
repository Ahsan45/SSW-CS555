"""Module for checking that aunts and uncles have not married their nieces and nephews"""
from utils import *

def aunts_and_uncles(key, indivs, fams):
    """Check that aunts and uncles have not married their nieces and nephews"""
    nieces_nephews = get_nieces_and_nephews(key, indivs, fams)
    spouses = get_spouses(key, indivs, fams)
    return set(spouses).isdisjoint(nieces_nephews)
