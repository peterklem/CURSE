import sqlite3

db = sqlite3.connect('assignment2.db')
cursor = db.cursor()

cursor.execute('''ALTER TABLE INSTRUCTOR ADD COURSE1_ID CHAR(10); ''')
cursor.execute('''ALTER TABLE INSTRUCTOR ADD COURSE2_ID CHAR(10); ''')
cursor.execute('''ALTER TABLE INSTRUCTOR ADD COURSE3_ID CHAR(10); ''')
cursor.execute('''ALTER TABLE INSTRUCTOR ADD COURSE4_ID CHAR(10); ''')
cursor.execute('''ALTER TABLE INSTRUCTOR ADD COURSE5_ID CHAR(10); ''')

db.commit()
db.close()