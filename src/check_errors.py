"""Module for checking for logical errors in gedcom files"""
import birth_before_death
import marr_before_div

def check_indiv(indivs):
    """Checks for individual-level logical errors"""
    for key in sorted(indivs.iterkeys()):
        if not birth_before_death.birth_before_death(indivs[key]):
            if indivs[key]["SEX"] == "M": pronoun = "his"
            else: pronoun = "her"
            print "Error US01: Birth date of {} ({}) occurs after {} death date".format(indivs[key]["NAME"], key, pronoun)

def check_fam(fams):
    """Checks for family-level logical errors"""
    for key in sorted(fams.iterkeys()):
        if not marr_before_div.marr_before_div(fams[key]):
            print "Error US02: Divorce occurs before marriage in this family ({})".format(key)
