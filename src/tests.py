"""Module for running tests"""
import unittest
import main
import utils
import birth_before_death
import marr_before_div

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
        self.individuals = main.parse(gedcom)[0]

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
    """Class for testing birth before death feature"""
    def setUp(self):
        gedcom = open('inputs/marr_before_div.txt', 'r')
        self.families = main.parse(gedcom)[1]

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


if __name__ == '__main__':
    unittest.main()
