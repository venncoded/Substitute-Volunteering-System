from src.database_utils import *
import datetime
from src.sms import *
from src.sms_slots import *
from src.sms_substitutes import *


if __name__ == '__main__':
    while(True):
        selection = input("""Welcome to the command line application for Example Academy! How can we help you today administrator?
              \r1) Substitutes
              \r2) Time Slots
              \r0) Quit
              \r""")
        match selection:
            case '0':
                break
            case '1':
                selectionSUB = input("""What would you like to do?
                    \r1) View Substitutes
                    \r2) Add Substitute
                    \r3) Delete subsitute
                    \r0) Return to main menu
                    \r""")
                match selectionSUB:
                    case '1':
                        for record in get_all_subs():
                            print(record)
                    case '2':
                        sub_username=input("What is the substitute's username? ")
                        sub_email=input("What is the subsitute's email? ")
                        add_sub(sub_username, sub_email)
                    case '3':
                        sub_username=input("What is the username of the sub you wish to delete? ")
                        delete_sub_username(sub_username)
    print("Goodbye!")