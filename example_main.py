from src.database_utils import *
import datetime
from src.sms import *
from src.sms_slots import *


if __name__ == '__main__':
    build_tables()
    add_slot('E',datetime.datetime.now()+ datetime.timedelta(minutes=90), datetime.datetime.now()+ datetime.timedelta(minutes=135), "English","Mr. F")