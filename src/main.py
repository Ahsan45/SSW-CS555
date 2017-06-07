"""Script to parse a GEDCOM file passed as a system argument"""

import sys
import time
from dateutil import parser
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

def parse(gedcom):
    """Parse each line of the GEDCOM file"""
    valid_tags = [["INDI", "FAM", "HEAD", "TRLR", "NOTE"],
                  ["NAME", "SEX", "BIRT", "DEAT", "FAMC","FAMS",
                   "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
                  ["DATE"]]

    def get_tag(parts):
        """Get tag from list of line parts"""
        if parts[0] == "0" and (parts[2] == "INDI" or parts[2] == "FAM"):
            return parts[2]
        return parts[1]

    def is_valid(level, tag):
        """Determine whether tag in line is valid"""
        if tag in valid_tags[int(level)]:
            return "Y"
        return "N"

    def get_args(level, tag, parts):
        """Get rest of arguments from line"""
        parts.remove(level)
        parts.remove(tag)
        return " ".join(parts)

    def add_to_dict(cur_key, tag, args):
        """Add current line to appropiate dictionary"""
        if cur_key[0] == "I":
            individuals[cur_key][tag] = args
        else:
            if tag == "CHIL":
                if not families[cur_key].has_key(tag):
                    families[cur_key][tag] = [args]
                else:
                    families[cur_key][tag].append(args)
            else:
                families[cur_key][tag] = args

    individuals = {}
    families = {}
    cur_key = ""
    second_key = ""

    for line in gedcom:
        line_parts = line.rstrip().split(" ")

        level = line_parts[0]
        tag = get_tag(line_parts)
        valid = is_valid(level, tag)
        args = get_args(level, tag, line_parts)

        if valid:
            if level == "0":
                if tag == "INDI":
                    cur_key = args
                    individuals[args] = {}
                if tag == "FAM":
                    cur_key = args
                    families[args] = {}
            elif level == "1":
                if tag == "BIRT" or tag == "DEAT" or tag == "MARR" or tag == "DIV":
                    add_to_dict(cur_key, tag, "")
                    second_key = tag
                else:
                    add_to_dict(cur_key, tag, args)
            else:
                if second_key == "":
                    add_to_dict(cur_key, tag, args)
                else:
                    add_to_dict(cur_key, second_key, args)
                    second_key = ""

    return (individuals, families)

def buildTable(cur_data, ref_data, data_type):
    """Build a table for the given data"""
    table = PrettyTable()

    def find_age(start, end):
        """Parse strings as date objects and compare them to get age"""
        start = parser.parse(start)
        end = parser.parse(end)

        return relativedelta(end, start).years

    def get(key, field):
        """Looks up the requested data in the appropiate dictionary"""
        if field == "AGE":
            if cur_data[key].has_key("DEAT"):
                return find_age(cur_data[key]["BIRT"], cur_data[key]["DEAT"])
            else:
                return find_age(cur_data[key]["BIRT"], time.strftime("%m %d %Y"))
        elif field == "ALIVE":
            return cur_data[key].has_key("DEAT")
        elif field == "HUSB_NAME":
            if cur_data[key].has_key("HUSB"):
                return ref_data[cur_data[key]["HUSB"]]["NAME"]
            else: return "NA"
        elif field == "WIFE_NAME":
            if cur_data[key].has_key("WIFE"):
                return ref_data[cur_data[key]["WIFE"]]["NAME"]
            else: return "NA"

        return cur_data[key][field] if cur_data[key].has_key(field) else "NA"

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
                           get(key, "WIFE"), get(key, "WIFE_NAME"), get(key, "CHIL")])

    return table

def main(argv):
    """Main function that reads GEDCOM file"""
    gedcom = open(argv[1], 'r')

    data = parse(gedcom)
    inds = buildTable(data[0], data[1], "individuals")
    fams = buildTable(data[1], data[0], "families")

    print "\nIndividuals\n", inds
    print "\nFamilies\n", fams

if __name__ == "__main__":
    main(sys.argv)
