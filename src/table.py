"""Module for generating a table based on gedcom data"""
from sort_siblings import sort_siblings
import time
from prettytable import PrettyTable
import utils

def build_table(cur_data, ref_data, data_type):
    """Build a table for the given data"""
    table = PrettyTable()

    def get(key, field):
        """Looks up the requested data in the appropiate dictionary"""
        if field == "AGE":
            if "DEAT" in cur_data[key]:
                return utils.find_age(cur_data[key]["BIRT"], cur_data[key]["DEAT"])
            else:
                return utils.find_age(cur_data[key]["BIRT"], time.strftime("%m %d %Y"))
        elif field == "ALIVE":
            return "DEAT" not in cur_data[key]
        elif field == "HUSB_NAME":
            if "HUSB" in cur_data[key]:
                return ref_data[cur_data[key]["HUSB"]]["NAME"]
            else: return "NA"
        elif field == "WIFE_NAME":
            if "WIFE" in cur_data[key]:
                return ref_data[cur_data[key]["WIFE"]]["NAME"]
            else: return "NA"

        return cur_data[key][field] if field in cur_data[key] else "NA"
    
    if data_type == "individuals":
        table.field_names = ["ID", "Name", "Gender", "Birthday","Age",
                             "Alive", "Death", "Child", "Spouse"]

        for key in sorted(cur_data.iterkeys()):
            table.add_row([key, get(key, "NAME"), get(key, "SEX"), get(key, "BIRT"), get(key, "AGE"),
                           get(key, "ALIVE"), get(key, "DEAT"), get(key, "FAMC"), get(key, "FAMS")])
    else:
        table.field_names = ["ID", "Married", "Divorced", "Husband ID",
                             "Husband Name", "Wife ID", "Wife Name", "Children"]

        for key in sorted(cur_data.iterkeys()):
            table.add_row([key, get(key, "MARR"), get(key, "DIV"), get(key, "HUSB"), get(key, "HUSB_NAME"),
                           get(key, "WIFE"), get(key, "WIFE_NAME"), sort_siblings(get(key, "CHIL"),ref_data)])

    return table

