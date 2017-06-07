"""Script to parse a GEDCOM file passed as a system argument"""

import sys

def parse(line):
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


    line_parts = line.split(" ")

    level = line_parts[0]
    tag = get_tag(line_parts)
    valid = is_valid(level, tag)
    args = get_args(level, tag, line_parts)

    input_line = "--> %s" % line
    parsed = "<-- " + level + "|" + tag + "|" + valid + "|" + args

    return "%s\n%s" % (input_line, parsed)

def main(argv):
    """Main function that reads GEDCOM file"""
    gedcom = open(argv[1], 'r')

    for line in gedcom:
        print parse(line.rstrip())

if __name__ == "__main__":
    main(sys.argv)
