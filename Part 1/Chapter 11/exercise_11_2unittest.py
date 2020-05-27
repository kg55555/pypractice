import unittest
from exercise_11_2 import *


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_formatter('vancouver', 'canada')
        self.assertEqual(formatted, "Vancouver, Canada")

    def test_city_country_population(self):
        formatted = city_formatter('santiago', 'chile', 328989489)
        self.assertEqual(formatted, "Santiago, Chile - Population: 328989489")


if __name__ == '__main__':
    unittest.main()
