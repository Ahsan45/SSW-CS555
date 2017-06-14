"""Module for running tests"""
import unittest
import main
import birth_before_death

class TestBirthBeforeDeath(unittest.TestCase):
    """Class for testing birth before death feature"""
    def setUp(self):
        gedcom = open('inputs/birth_before_death.txt', 'r')
        self.individuals = main.parse(gedcom)[0]

    def tearDown(self):
        self.individuals = None

    def test_date_comparer_true(self):
        """Test date comparer when result should be true"""
        test = birth_before_death.date_first('19 DEC 1999', '21 AUG 2004')
        self.assertTrue(test)

    def test_date_comparer_false(self):
        """Test date comparer when result should be false"""
        test = birth_before_death.date_first('04 JUN 2013', '26 MAR 2002')
        self.assertFalse(test)

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


if __name__ == '__main__':
    unittest.main()
