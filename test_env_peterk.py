from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

if __name__ == '__main__':

    student1 = Student(10001)
    student1.print_schedule()

    ins1 = Instructor(20007)
    ins1.print_schedule()
