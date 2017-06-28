#Erik Lim
#SSW 555 Agile Methods for Software Development

'''Module for checking if marriage came before death'''

from utils import date_first

def marr_before_death_husb(fam, indiv):
    husb = fam['HUSB']
    if not 'DEAT' in indiv[husb]:
        return True

    return date_first(fam['MARR'], indiv[husb]['DEAT'])

def marr_before_death_wife(fam, indiv):
    wife = fam['WIFE']
    if not 'DEAT' in indiv[wife]:
        return True

    return date_first(fam['MARR'], indiv[wife]['DEAT'])
