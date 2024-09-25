import unittest
from src.sms import *
from tests.setup_public import *

class TestTestData(unittest.TestCase):
    def test_insert_subs(self):
        start_with_test_data()
        result = exec_get_all('SELECT * FROM substitute_roster')
        self.assertEqual(3, len(result), "three subs should be in the database")

    def test_insert_slots(self):
        start_with_test_data()
        result = exec_get_all('SELECT * FROM slots')
        self.assertEqual(4, len(result), "four slots should be in the database")
