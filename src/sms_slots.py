from src.database_utils import *

def add_slot(periodName, startTime, endtime, course=None, ogTeacher=None, substituteID=None, lessonPlanLink=None, seriesCode=None ):
    insert_sql="""
         INSERT INTO slots(periodName, startTime, endtime, course, ogTeacher, substituteID, lessonPlanLink, seriesCode )
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    exec_commit(insert_sql, [periodName, startTime, endtime, course, ogTeacher, substituteID, lessonPlanLink, seriesCode])