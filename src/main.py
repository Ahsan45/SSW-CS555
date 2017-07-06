"""Script to parse a GEDCOM file passed as a system argument"""
import sys
from parser import parse
from table import build_table
import check_errors

def main(argv):
    """Main function that reads GEDCOM file"""
    gedcom = open(argv[1], 'r')

    data = parse(gedcom)

    inds = build_table(data[0], data[1], "individuals")
    fams = build_table(data[1], data[0], "families")

    print "\nIndividuals\n", inds
    print "\nFamilies\n", fams

    print
    check_errors.check_indiv(data[0])
    check_errors.check_fam(data[1], data[0])
    print

if __name__ == "__main__":
    main(sys.argv)
