import unittest
from src.sms_substitutes import *
from tests.setup_public import *

class TestTestData(unittest.TestCase):
    def test_add_sub(self):
        start_with_test_data()
        add_sub('user4','abra@cadabra.com', 'doug')
        result = exec_get_all('SELECT * FROM substitute_roster')
        self.assertEqual(4, len(result), "four subs should be in the database")
        self.assertEqual(result[3][2],'doug', 'data addition failed')

    def test_delete_sub_id(self):
        start_with_test_data()
        delete_sub_id(1)
        result = exec_get_all('SELECT * FROM substitute_roster')
        self.assertEqual(2, len(result), "2 subs should be in the database")
        self.assertEqual(result[1][1],'user3', 'data deletion failed')