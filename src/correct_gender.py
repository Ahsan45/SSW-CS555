"""Module for checking if spouses are the correct gender for their role"""

def husb_correct_gender(indiv, fam):
    """Checks if husband is correct gender"""
    husb = fam['HUSB']
    return indiv[husb]['SEX'] == 'M'

def wife_correct_gender(indiv, fam):
    """Checks if wife is correct gender"""
    wife = fam['WIFE']
    return indiv[wife]['SEX'] == 'F'
