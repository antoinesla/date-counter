from os import kill
import unittest
import datetime
import date_calculator

class TestDateCalculator(unittest.TestCase):
    '''class that runs tests for date calculator'''

    def test_correct_date_2_args(self):
        '''
        passes correctly formatted date with two arguments and see if it 
        returns the correct datetime object
        '''
        date_string = '12/05'
        correct_date_object = datetime.datetime(2021,5,12)

        test_date_object = date_calculator.get_date_from_string(date_string)
        self.assertEqual(test_date_object, correct_date_object)

    def test_correct_date_3_args(self):
        '''
        passes correctly formatted date with three arguments and see if it 
        returns the correct datetime object
        '''
        date_string = '12/05/2021'
        correct_date_object = datetime.datetime(2021,5,12)

        test_date_object = date_calculator.get_date_from_string(date_string)
        self.assertEqual(test_date_object, correct_date_object)

    def test_incorrect_date(self):
        '''passes a date that should return False'''
        date_string = '12/13/2021'
        test_date_object = date_calculator.get_date_from_string(date_string)
        self.assertFalse(test_date_object)

    def test_string_that_is_not_date(self):
        '''passes a string that is not a date'''
        not_date_string = '654 enft 54'
        test_date_object = date_calculator.get_date_from_string(not_date_string)
        self.assertFalse(test_date_object)


if __name__ == '__main__':
    unittest.main()