import unittest
from exercise_11_3 import *


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('bob', 'jones', 30000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 35000)

    def test_give_custom_raise(self):
        self.employee.give_raise(30000)
        self.assertEqual(self.employee.salary, 60000)


if __name__ == '__main__':
    unittest.main()
