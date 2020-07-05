import sqlite3

db = sqlite3.connect('assignment2.db')
cursor = db.cursor()
cursor.execute('drop table STUDENT')
cursor.execute('drop table INSTRUCTOR')
cursor.execute('drop table ADMIN')
cursor.execute('drop table COURSE')

# Create student table
command = """CREATE TABLE STUDENT(
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
PASS        TEXT    NOT NULL,
SURNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL, 
COURSES     TEXT);
"""
cursor.execute(command) # Add student table

# Student values
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'PhysicsFounder', 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'marcur', 'Marie', 'Curie', 1903, 'BSAS', 'curiem', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'DontStealMyWorkEdison', 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Lightbulb', 'Thomas', 'Edison', 1879, 'BSEE', 'notcool', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'Newman', 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'AmazingGrace', 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'MayFlowers', 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'MarkMyWords', 'Mark', 'Dean', 1979, 'BSCO', 'deanm', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'FaraDayandNight', 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym', NULL);""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'LacedwithLove', 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea', NULL);""") 
cursor.execute("""insert into STUDENT values(00010020, 'peterk', "Peter", "Klembczyk", 2021, 'BSCO', 'klembczykp', NULL);""")
cursor.execute("""insert into STUDENT values(00010021, 'yankees99', "Aaron", "Judge", 2013, 'BALL', 'judgea', NULL);""")

# Create instructor table
command = """CREATE TABLE INSTRUCTOR (  
ID 		    INT 	PRIMARY KEY 	NOT NULL,
PASS        TEXT    NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL,
COURSES     TEXT)
;"""
cursor.execute(command) # Add instructor table

# Instructor values
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020001, 'hummus', 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj', NULL);""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020002, 'Peace', 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan', NULL);""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020003, 'ToTheStars', 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig', NULL);""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020004, 'BigAl', 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga', NULL);""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020005, 'wentworth123', 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank', NULL);""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020006, 'italian17', 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid', NULL);""")


# Create admin table
command =  """CREATE TABLE ADMIN (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
PASS        TEXT    NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL)
;"""
cursor.execute(command) # Add admin table

# Admin values
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'fourtyFourth', 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""") 
cursor.execute("""INSERT INTO ADMIN VALUES(00030002, 'Registration', 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""") 


# Create course table
command = """create table COURSE(
                    TITLE           varchar (30)    not null,
                    CRN             char(10)        not null    primary key,
                    DEPARTMENT      varchar(20)     not null,
                    INSTRUCTOR      varchar(30)     not null,
                    START_TIME      int(4)         not null,
                    END_TIME        int(4)         not null,
                    DAYS_OF_WEEK    varchar(5)      not null,
                    SEMESTER        char(3)         not null,
                    YEAR            int(4)          not null,
                    CREDITS         int(1)          not null,
                    STUDENT_LIST    TEXT 
                ); """
    
cursor.execute(command) # Add course table

# Add courses
cursor.execute("""insert into COURSE values("Computer Architecture", "ELEC-3725-02", "ELEC", "Marisha Rawlins", 1000, 1120, 'TR', 'SUM', 2020, 4, NULL)""")
cursor.execute("""insert into COURSE values("Advanced Digital Circuit Design", "ELEC-3200-01", "ELEC", "Pilin Junsangsri", 0800, 0920, 'WF', 'SUM', 2020, 4, NULL)""")
cursor.execute("""insert into COURSE values("Advanced Digital Circuit Design", "ELEC-3200-02", "ELEC", "Pilin Junsangsri", 1000, 1150, 'F', 'SUM', 2020, 4, NULL)""")
cursor.execute("""insert into COURSE values("Applied Programming Concepts", "ELEC-3225-01", "ELEC", "Aaron Carpenter", 1200, 1250, 'M', 'SUM', 2020, 4, NULL)""")
cursor.execute("""insert into COURSE values("Applied Programming Concepts Lab", "ELEC-3225-02", "ELEC", "Aaron Carpenter", 1300, 1450, 'TR', 'SUM', 2020, 4, NULL)""")

db.commit()
db.close()