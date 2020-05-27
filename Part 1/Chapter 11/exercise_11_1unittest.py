import unittest
from exercise_11_1 import *

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_formatter('vancouver', 'canada')
        self.assertEqual(formatted, "Vancouver, Canada")

if __name__ == '__main__':
    unittest.main()


