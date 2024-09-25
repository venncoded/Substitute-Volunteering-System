import datetime
import unittest
from src.sms_slots import *
from tests.setup_public import *

class TestSlots(unittest.TestCase):
    def test_add_slot(self):
        start_with_test_data()
        add_slot('E',datetime.datetime.now()+ datetime.timedelta(minutes=90), datetime.datetime.now()+ datetime.timedelta(minutes=135), "English","Mr. F")
        result = exec_get_all('SELECT * FROM slots')
        self.assertEqual(5, len(result), "five subs should be in the database")