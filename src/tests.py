"""Module for running tests"""
import time
import unittest
import parser
import utils
import birth_before_death
import marr_before_div
import lt150
import birth_after_marr
import date_before_now
import birth_before_marr
import parents_not_too_old

class TestUtils(unittest.TestCase):
    """Class for testing utility functions"""
    def test_date_comparer_true(self):
        """Test date comparer when result should be true"""
        test = utils.date_first('19 DEC 1999', '21 AUG 2004')
        self.assertTrue(test)

    def test_date_comparer_false(self):
        """Test date comparer when result should be false"""
        test = utils.date_first('04 JUN 2013', '26 MAR 2002')
        self.assertFalse(test)

class TestBirthBeforeDeath(unittest.TestCase):
    """Class for testing birth before death feature"""
    def setUp(self):
        gedcom = open('inputs/birth_before_death.txt', 'r')
        self.individuals = parser.parse(gedcom)[0]

    def tearDown(self):
        self.individuals = None

    def test_no_death(self):
        """Tests birth_before_death when no death date exists"""
        test = birth_before_death.birth_before_death(self.individuals['I01'])
        self.assertTrue(test)

    def test_death_at_birth(self):
        """Tests bith_before_death when individual dies at birth"""
        test = birth_before_death.birth_before_death(self.individuals['I02'])
        self.assertTrue(test)

    def test_no_birth(self):
        """Tests birth_before_death when no birth date exists"""
        test = birth_before_death.birth_before_death(self.individuals['I03'])
        self.assertTrue(test)

    def test_no_birth_with_death(self):
        """Tests birth_before_death when no birth date exists but a death date does exist"""
        test = birth_before_death.birth_before_death(self.individuals['I04'])
        self.assertFalse(test)

    def test_death_before_birth(self):
        """Tests bith_before_death when individual's death is before birth"""
        test = birth_before_death.birth_before_death(self.individuals['I05'])
        self.assertFalse(test)


    def test_death_after_birth(self):
        """Tests bith_before_death when individual's death is after birth"""
        test = birth_before_death.birth_before_death(self.individuals['I06'])
        self.assertTrue(test)

class TestMarrBeforeDiv(unittest.TestCase):
    """Class for testing marriage before divorce feature"""
    def setUp(self):
        gedcom = open('inputs/marr_before_div.txt', 'r')
        self.families = parser.parse(gedcom)[1]

    def tearDown(self):
        self.families = None

    def test_no_div(self):
        """Tests marr_before_div when no divorce date exists"""
        test = marr_before_div.marr_before_div(self.families['F01'])
        self.assertTrue(test)

    def test_div_at_marr(self):
        """Tests marr_before_div when divorce and marriage happen on same day"""
        test = marr_before_div.marr_before_div(self.families['F02'])
        self.assertTrue(test)

    def test_no_marr(self):
        """Tests marr_before_div when no marriage date exists"""
        test = marr_before_div.marr_before_div(self.families['F03'])
        self.assertTrue(test)

    def test_no_marr_with_div(self):
        """Tests marr_before_div when no marriage date exists but a divorce date does exist"""
        test = marr_before_div.marr_before_div(self.families['F04'])
        self.assertFalse(test)

    def test_div_before_marr(self):
        """Tests marr_before_div when family's divorce is before marriage"""
        test = marr_before_div.marr_before_div(self.families['F05'])
        self.assertFalse(test)


    def test_div_after_marr(self):
        """Tests marr_before_div when family's divorce is after marriage"""
        test = marr_before_div.marr_before_div(self.families['F06'])
        self.assertTrue(test)

class TestLTOneFifty(unittest.TestCase):
    """Class for testing age less than 150 feature"""
    def setUp(self):
        gedcom = open('inputs/input.txt', 'r')
        self.individuals = parser.parse(gedcom)[0]

    def tearDown(self):
        self.individuals = None

    def test_age_less_than_150(self):
        """Tests when age less than 150"""
        age = lt150.check150('09-04-1996', '06-09-2017')
        self.assertTrue(age)

    def test_age_greater_than_150(self):
        """Tests when age greater than 150"""
        age = lt150.check150('09-17-1860', '09-17-2017')
        self.assertFalse(age)

    def test_indiv_age_dead(self):
        """Tests when individual has died"""
        age = utils.find_age(self.individuals['I07']['BIRT'], self.individuals['I07']['DEAT'])
        self.assertTrue(age <= 150)

    def test_indiv_age_alive(self):
        """Tests when individual has not died"""
        age = utils.find_age(self.individuals['I01']['BIRT'], time.strftime('%d %b %Y'))
        self.assertTrue(age <= 150)

    def test_no_birth(self):
        """Tests when there is no birth"""
        age = lt150.check150(None, '5 May 1999')
        self.assertFalse(age)

class TestBirthAfterMarriage(unittest.TestCase):
    """Class for testing birth after marriage feature"""
    def setUp(self):
        gedcom = open('inputs/birth_after_marriage.txt', 'r')
        self.families = parser.parse(gedcom)

    def tearDown(self):
        self.families = None

    def test_birth_after_marriage(self):
        """test that birth after marriage of family returns true"""
        result = birth_after_marr.marr_before_child(self.families[0], self.families[1]['F01'])
        self.assertTrue(result)

    def test_birth_before_marriage(self):
        """test that birth before marriage of family returns false"""
        result = birth_after_marr.marr_before_child(self.families[0], self.families[1]['F02'])
        self.assertFalse(result)

    def test_no_birth(self):
        """test that individual with no birthday will return false"""
        result = birth_after_marr.marr_before_child(self.families[0], self.families[1]['F03'])
        self.assertFalse(result)

    def test_no_marr(self):
        """test what happens when no marriage tag in family"""
        result = birth_after_marr.marr_before_child(self.families[0], self.families[1]['F04'])
        self.assertFalse(result)

class TestDateBeforeNow(unittest.TestCase):
    """Class for testing date before now feature"""
    def setUp(self):
        gedcom = open('inputs/date_before_now.txt', 'r')
        self.indiv = parser.parse(gedcom)[0]

    def tearDown(self):
        self.indiv = None

    def test_date_true(self):
        """Tests date comparer to be true"""
        test = date_before_now.date_past('24 APR 2004')
        self.assertTrue(test)

    def test_date_false(self):
        """Tests date comparer to be false"""
        test = date_before_now.date_past('30 MAY 2022')
        self.assertFalse(test)

    def test_birth_true(self):
        """Tests if birth is before today"""
        test = date_before_now.birth_before_now(self.indiv['I01'])
        self.assertTrue(test)

    def test_birth_false(self):
        """Tests if birth is before today"""
        test = date_before_now.birth_before_now(self.indiv['I02'])
        self.assertFalse(test)

    def test_no_death(self):
        """Tests if death date doesn't exist"""
        test = date_before_now.death_before_now(self.indiv['I03'])
        self.assertTrue(test)

    def test_death_true(self):
        """Tests if death is before today"""
        test = date_before_now.death_before_now(self.indiv['I04'])
        self.assertTrue(test)

    def test_death_false(self):
        """Tests if death date is before today"""
        test = date_before_now.death_before_now(self.indiv['I07'])
        self.assertFalse(test)

class TestBirthBeforeMarr(unittest.TestCase):
    """Class for testing birth before marriage feature"""
    def setUp(self):
        gedcom = open('inputs/birth_before_marr.txt', 'r')
        self.fam = parser.parse(gedcom)

    def tearDown(self):
        self.fam = None

    def test_husb_birth_true(self):
        """Tests if husband's birth happens before marriage"""
        test = birth_before_marr.birth_before_marr_husb(self.fam[1]['F01'], self.fam[0])
        self.assertTrue(test)

    def test_husb_birth_false(self):
        """Tests if husband's birth happens before marriage"""
        test = birth_before_marr.birth_before_marr_husb(self.fam[1]['F02'], self.fam[0])
        self.assertFalse(test)

    def test_wife_birth_true(self):
        """Tests if wife's birth happens before marriage"""
        test = birth_before_marr.birth_before_marr_wife(self.fam[1]['F03'], self.fam[0])
        self.assertTrue(test)

    def test_wife_birth_false(self):
        """Tests if wife's birth happens before marriage"""
        test = birth_before_marr.birth_before_marr_wife(self.fam[1]['F02'], self.fam[0])
        self.assertFalse(test)

class TestParentsNotTooOld(unittest.TestCase):
    """Class for testing the parents not too old feature"""
    def setUp(self):
        gedcom = open('inputs/parents_too_old.txt')
        self.fam = parser.parse(gedcom)

    def tearDown(self):
        self.fam = None

    def test_husb_too_old(self):
        """Tests when father is too old"""
        test = parents_not_too_old.husb_not_too_old(self.fam[1]['F01'], self.fam[0])
        self.assertFalse(test)

    def test_wife_too_old(self):
        """Tests when mother is too old"""
        test = parents_not_too_old.wife_not_too_old(self.fam[1]['F01'], self.fam[0])
        self.assertFalse(test)

    def test_husb_not_too_old(self):
        """Tests when father is not too old"""
        test = parents_not_too_old.husb_not_too_old(self.fam[1]['F02'], self.fam[0])
        self.assertTrue(test)

    def test_wife_not_too_old(self):
        """Tests when mother is not too old"""
        test = parents_not_too_old.wife_not_too_old(self.fam[1]['F02'], self.fam[0])
        self.assertTrue(test)

    def test_no_children(self):
        """Tests when their are no children in family"""
        test1 = parents_not_too_old.husb_not_too_old(self.fam[1]['F04'], self.fam[0])
        test2 = parents_not_too_old.wife_not_too_old(self.fam[1]['F04'], self.fam[0])
        self.assertTrue(test1 and test2)

if __name__ == '__main__':
    unittest.main()
