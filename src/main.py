"""Script to parse a GEDCOM file passed as a system argument"""

import sys

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

def main(argv):
    """Main function that reads GEDCOM file"""
    gedcom = open(argv[1], 'r')

    data = parse(gedcom)
    print data

if __name__ == "__main__":
    main(sys.argv)
