from src.database_utils import *

def add_slot(periodName, startTime, endtime, course=None, ogTeacher=None, substituteID=None, lessonPlanLink=None, seriesCode=None ):
    insert_sql="""
         INSERT INTO slots(periodName, startTime, endtime, course, ogTeacher, substituteID, lessonPlanLink, seriesCode )
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    exec_commit(insert_sql, [periodName, startTime, endtime, course, ogTeacher, substituteID, lessonPlanLink, seriesCode])

def delete_slot_id(id):
    delete_sql="""
        DELETE FROM slots WHERE slotID = %s
    """
    exec_commit(delete_sql, [id])

def update_sub_col_id(slotID, subID):
    update_sql="""
        UPDATE slots
        SET substituteID = %s
        WHERE slotID = %s
    """
    exec_commit(update_sql, [subID, slotID])

def update_sub_col_username(slotID, sub_username):
    update_sql="""
        UPDATE slots
        SET substituteID = (SELECT subID FROM substitute_roster WHERE username = %s)
        WHERE slotID = %s
    """
    exec_commit(update_sql, [sub_username, slotID])

def get_all_slots():
    select_sql="""
        SELECT * FROM slots
    """
    return exec_get_all(select_sql)