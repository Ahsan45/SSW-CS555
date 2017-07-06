"""Module for checking for bigamy in a family"""
import time
from utils import date_first

def no_bigamy(indiv, fams):
    """Checks that individuals were not spouses in multiple families at the same time"""
    if "FAMS" in indiv and len(indiv["FAMS"]) > 1:
        spouse = "HUSB" if indiv["SEX"] == "F" else "WIFE"
        all_marrs = {}

        for fam in indiv["FAMS"]:
            if not "MARR" in fams[fam]:
                pass
            else:
                if "DIV" in fams[fam]:
                    curr_marr = (fams[fam]["MARR"], fams[fam]["DIV"])
                elif "DEAT" in fams[fam][spouse]:
                    curr_marr = (fams[fam]["MARR"], spouse["DEAT"])
                else:
                    curr_marr = (fams[fam]["MARR"], time.strftime("%d %b %Y"))
                all_marrs[fam] = curr_marr

        for fam in indiv["FAMS"]:
            for marr_fam in all_marrs:
                if ((not fam == marr_fam) and ("MARR" in fams[fam]) and date_first(all_marrs[marr_fam][0], fams[fam]["MARR"])
                   and date_first(fams[fam]["MARR"], all_marrs[marr_fam][1])):
                    return (fam, marr_fam)
        return True
    else:
        return True
