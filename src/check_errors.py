"""Module for checking for logical errors in gedcom files"""
import birth_before_death
import marr_before_div
import lt150
import birth_after_marr
import date_before_now
import birth_before_marr

def check_indiv(indivs):
    """Checks for individual-level logical errors"""
    for key in sorted(indivs.iterkeys()):
        if not date_before_now.birth_before_now(indivs[key]):
            print "Error US01: Birth date of {} ({}) occurs in the future".format(indivs[key]['NAME'], key) 
        if not date_before_now.death_before_now(indivs[key]):
            print "Error US01: Death date of {} ({}) occurs in the future".format(indivs[key]['NAME'], key)
	if not birth_before_death.birth_before_death(indivs[key]):
            if indivs[key]["SEX"] == "M": pronoun = "his"
            else: pronoun = "her"
            print "Error US03: Birth date of {} ({}) occurs after {} death date".format(indivs[key]["NAME"], key, pronoun)
        if "DEAT" in indivs[key]:
            if not lt150.check150(indivs[key]["BIRT"],indivs[key]["DEAT"]):
                print "Error US07: Age of {} greater than 150 years".format(indivs[key]["NAME"])
        if not "DEAT" in indivs[key]:
            if not lt150.check150(indivs[key]["BIRT"], None):
                print "Error US07: Age of {} is greater than 150 years".format(indivs[key]["NAME"])
	#print indivs
def check_fam(fams, indivs):
    """Checks for family-level logical errors"""
    for key in sorted(fams.iterkeys()):
        if not date_before_now.marr_before_now(fams[key]):
            print "Error US01: Marriage date of this family occurs in the future ({})".format(key)
        if not date_before_now.div_before_now(fams[key]):
            print "Error US01: Divorce date of this family occurs in the future ({})".format(key)
        if not birth_before_marr.birth_before_marr_husb(fams[key], indivs):
            print "Error US02: Birth date of husband occurs before marriage in this family ({})".format(key)
        if not birth_before_marr.birth_before_marr_wife(fams[key], indivs):
            print "Error US02: Birth date of wife occurs before marriage in this family ({})".format(key)
	if not marr_before_div.marr_before_div(fams[key]):
            print "Error US04: Divorce occurs before marriage in this family ({})".format(key)
        if not birth_after_marr.marr_before_child(indivs, fams[key]):
            print "Error US08: Birth of child before marriage in this family: ({})".format(key)
