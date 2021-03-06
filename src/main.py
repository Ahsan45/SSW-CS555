"""Script to parse a GEDCOM file passed as a system argument"""
import sys
from parser import parse
from table import build_table
import check_errors
from print_deceased import print_deceased
from living_married import *
from living_single import *
from list_multiple_births import *

def main(argv):
    """Main function that reads GEDCOM file"""
    gedcom = open(argv[1], 'r')

    data = parse(gedcom)

    inds = build_table(data[0], data[1], "individuals")
    fams = build_table(data[1], data[0], "families")
    deadPeople = print_deceased(data[0])
    dead = build_table(deadPeople, data[1], "deceased")

    print "\nIndividuals\n", inds
    print "\nFamilies\n", fams
    print "\nDeceased\n", dead

    print
    print "Parser Errors:"
    for error in sorted(data[2]): print error
    if data[2] == []: print 'None'
    print
    print "Individual Errors:"
    for error in sorted(check_errors.check_indiv(data[0], data[1])): print error
    if check_errors.check_indiv(data[0], data[1]) == []: print 'None'
    print
    print "Family Errors:"
    for error in sorted(check_errors.check_fam(data[1], data[0])): print error
    if check_errors.check_fam(data[1], data[0]) == []: print 'None'
    print
    print "Living Married Individuals (US30):" 
    living_married(data[0])
    print
    print "Living Single Individuals (US31):" 
    living_single(data[0])
    print
    print "Multiple Births (US32):"
    list_multiple_births(data[0])
    print
    
if __name__ == "__main__":
    main(sys.argv)
