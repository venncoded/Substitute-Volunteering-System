from src.sms import *

def start_with_test_data():
    build_tables()
    conn = connect()
    cur = conn.cursor()
    insert_subs(cur)
    insert_slots(cur)
    conn.commit()
    conn.close()

def insert_subs(cur):
    insert_sql="""
        INSERT INTO substitute_roster(username, emailAddress)
        VALUES ('user1', 'user1@gmail.com'), ('user2', 'user2@gmail.com'),('user3', 'user3@gmail.com')
    """
    cur.execute(insert_sql)

def insert_slots(cur):
    insert_sql="""
        INSERT INTO slots(periodName, startTime, endTime, course, ogTeacher)
        VALUES ('A', CURRENT_TIMESTAMP+INTERVAL '1 week', CURRENT_TIMESTAMP+INTERVAL '45 minutes'+INTERVAL '1 week', 'Comp Sci','Mr. S'), 
        ('B', CURRENT_TIMESTAMP+INTERVAL '2 week', CURRENT_TIMESTAMP+INTERVAL '45 minutes'+INTERVAL '1 week', 'Comp Eng','Mr. A'),
        ('C', CURRENT_TIMESTAMP+INTERVAL '3 week', CURRENT_TIMESTAMP+INTERVAL '45 minutes'+INTERVAL '1 week', 'Math','Mrs. D'),
        ('D', CURRENT_TIMESTAMP+INTERVAL '5 week', CURRENT_TIMESTAMP+INTERVAL '65 minutes'+INTERVAL '5 week', 'Math','Mrs. D')
    """
    cur.execute(insert_sql)