"""Module for checking for logical errors in gedcom files"""
from birth_before_death import *
from marr_before_div import *
from lt150 import *
from birth_after_marr import *
from date_before_now import *
from birth_before_marr import *
from marr_before_death import *
from divorce_before_death import *
from parents_not_too_old import *
from no_bigamy import *
from birth_before_parents_death import *
from marr_after_14 import *
from male_last_names import * 
from no_marr_to_desc import *
from fewer_than_15_siblings import *
from multiple_births import *
from unique_name_bday import *
from aunts_and_uncles import *
from cousins_not_marry import *
from siblings_not_marry import *
from correct_gender import *
from unique_family import *
from unique_firstname import *
from corresponding_entries import *

def check_indiv(indivs, fams):
    """Checks for individual-level logical errors"""
    errors = []

    for key in sorted(indivs.iterkeys()):
        if not birth_before_now(indivs[key]):
            errors.append("Error US01: Birth date of {} ({}) occurs in the future".format(indivs[key]['NAME'], key))
        if not death_before_now(indivs[key]):
            errors.append("Error US01: Death date of {} ({}) occurs in the future".format(indivs[key]['NAME'], key))
        if not birth_before_death(indivs[key]):
            if indivs[key]["SEX"] == "M": pronoun = "his"
            else: pronoun = "her"
            errors.append("Error US03: Birth date of {} ({}) occurs after {} death date".format(indivs[key]["NAME"], key, pronoun))
        if "DEAT" in indivs[key]:
            if not check150(indivs[key]["BIRT"],indivs[key]["DEAT"]):
                errors.append("Error US07: Age of {} greater than 150 years".format(indivs[key]["NAME"]))
        if not "DEAT" in indivs[key]:
            if not check150(indivs[key]["BIRT"], None):
                errors.append("Error US07: Age of {} is greater than 150 years".format(indivs[key]["NAME"]))
        if no_bigamy(indivs[key], fams) != True:
            errors.append(("Anomaly US11: Individual ({})'s marriage in {} overlaps with their marriage in {}"
                   .format(key, no_bigamy(indivs[key], fams)[0], no_bigamy(indivs[key], fams)[1])))
        if not unique_name_bday(indivs[key],indivs):
            errors.append("Anomaly US23: Multiple Individuals with same name and birthday: {}".format(indivs[key]['NAME']))
        if not aunts_and_uncles(key, indivs, fams):
            errors.append("Anomaly US20: Inidivdual ({}) has married their niece/nephew".format(key))
        if not cousins_not_marry(key, indivs, fams):
            errors.append("Anomaly US19: Individual ({}) has married their first cousin".format(key))
        if not siblings_not_marry(key, indivs, fams):
            errors.append("Anomaly US18: Individual ({}) has married their sibling".format(key))
        if not corresponding_indiv(key, indivs[key], fams):
            errors.append("Error US26: Corresponding entries are missing for the following individual: {}".format(key))
    return errors

def check_fam(fams, indivs):
    """Checks for family-level logical errors"""
    errors = []

    for key in sorted(fams.iterkeys()):
        if not marr_before_now(fams[key]):
            errors.append("Error US01: Marriage date of this family occurs in the future ({})".format(key))
        if not div_before_now(fams[key]):
            errors.append("Error US01: Divorce date of this family occurs in the future ({})".format(key))
        if not birth_before_marr_husb(fams[key], indivs):
            errors.append("Error US02: Birth date of husband occurs after marriage in this family ({})".format(key))
        if not birth_before_marr_wife(fams[key], indivs):
            errors.append("Error US02: Birth date of wife occurs after marriage in this family ({})".format(key))
        if not marr_before_div(fams[key]):
            errors.append("Error US04: Divorce occurs before marriage in this family ({})".format(key))
        if not marr_before_child(indivs, fams[key]):
            errors.append("Anomaly US08: Birth of child before marriage in this family: ({})".format(key))
        if not marr_before_death_husb(fams[key], indivs):
            errors.append("Error US05: Death date of husband occurs before marriage in this family ({})".format(key))
        if not marr_before_death_wife(fams[key], indivs):
            errors.append("Error US05: Death date of wife occurs before marriage in this family ({})".format(key))
        if not divorce_before_death_husb(fams[key], indivs):
            errors.append("Error US06: Death date of husband occurs before divorce in this family ({})".format(key))
        if not divorce_before_death_wife(fams[key], indivs):
            errors.append("Error US06: Death date of wife occurs before divorce in this family ({})".format(key))
        if not husb_not_too_old(fams[key], indivs):
            errors.append("Error US12: Husband in this family ({}) is too old to be a father.".format(key))
        if not wife_not_too_old(fams[key], indivs):
            errors.append("Error US12: Wife in this family ({}) is too old to be a mother.".format(key))
        if not birth_before_parents_death(indivs, fams[key]):
            errors.append("Error US09: Death of parent occurs before birth of child is possible in this family ({})".format(key))
        if not male_last_names(indivs, get_males(fams[key],indivs)):
            errors.append("Error US16: Male surnames not consistent in this family ({})".format(key))
        if not no_marr_to_desc(indivs, fams[key], fams):
            errors.append("Error US17: Marriage to descendents found: ({})".format(key))
        if not husb_marr_after_14(indivs, fams[key]):
            errors.append("Anomaly US10: Husband in this family ({}) was younger than 14 when married.".format(key))
        if not wife_marr_after_14(indivs, fams[key]):
            errors.append("Anomaly US10: Wife in this family ({}) was younger than 14 when married.".format(key))
        if not fewer_than_15_siblings(fams[key]):
            errors.append("Anomaly US15: There are at least 15 siblings in this family ({}).".format(key))
        if not multiple_births(indivs, fams[key]):
            errors.append("Anomaly US14: There are more than 5 siblings born at the same time in this family ({}).".format(key))
        if not husb_correct_gender(indivs, fams[key]):
            errors.append("Error US21: Husband is not the correct gender in this family ({})".format(key))
        if not wife_correct_gender(indivs, fams[key]):
            errors.append("Error US21: Wife is not the correct gender in this family ({})".format(key))
        if not unique_family(key, fams):
            errors.append("Error US24: Family is not unique ({})".format(key))
        if not unique_firstname(indivs, fams[key]):
            errors.append("Error US25: There are children with the same name and birthdate in this family ({})".format(key))
        if not corresponding_fam(key, fams[key], indivs):
            errors.append("Error US26: Corresponding entries are missing for the following family: {}".format(key))
    return errors
