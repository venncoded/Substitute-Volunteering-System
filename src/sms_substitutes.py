from src.database_utils import *

def add_sub(username, emailAddress, firstName=None, middleName=None, lastName=None, preferredName=None ):
    insert_sql="""
         INSERT INTO substitute_roster(username, emailAddress, firstName, middleName, lastName, preferredName)
         VALUES (%s,%s,%s,%s,%s,%s)
    """
    exec_commit(insert_sql, [username, emailAddress, firstName, middleName, lastName, preferredName])

def delete_sub_id(id):
    delete_sql="""
        DELETE FROM substitute_roster WHERE subID = %s
    """
    exec_commit(delete_sql, [id])