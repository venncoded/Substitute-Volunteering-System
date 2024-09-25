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

    def test_delete_slot_id(self):
        start_with_test_data()
        delete_slot_id(1)
        result = exec_get_all('SELECT * FROM slots')
        self.assertEqual(3, len(result), "3 slots should be in the database")
        self.assertEqual(result[1][1],'C', 'data deletion failed')

    def test_update_sub(self):
        start_with_test_data()
        update_sub_col(1,2)
        result = exec_get_one('SELECT substituteID FROM slots WHERE slotID = 1')
        self.assertEqual(result[0], 2, 'failed to update.')