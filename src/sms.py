from src.database_utils import *

def build_tables():
    conn = connect()
    cur = conn.cursor()
    build_substitutes(cur)
    build_slots(cur)
    conn.commit()
    conn.close()

def build_substitutes(cur):
    drop_sql = """
        DROP TABLE IF EXISTS substitute_roster
    """
    create_sql = """
        CREATE TABLE substitute_roster(
            subID SERIAL PRIMARY KEY,
            username VARCHAR(40),
            firstName VARCHAR(40),
            middleName VARCHAR(40),
            lastName VARCHAR(40),
            preferredName VARCHAR(40),
            emailAddress VARCHAR(100)
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

def build_slots(cur):
    drop_sql = """
        DROP TABLE IF EXISTS slots
    """
    create_sql = """
        CREATE TABLE slots(
            slotID SERIAL PRIMARY KEY, 
            periodName VARCHAR(10) NOT NULL,
            startTime TIMESTAMP,
            endTime TIMESTAMP,
            substituteID int,
            course VARCHAR(50),
            ogTeacher VARCHAR(100),
            lessonPlanLink VARCHAR(5000),
            seriesCode VARCHAR(10)
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

if __name__ == '__main__':
    build_tables()