import MySQLdb
import temp

__author__ = "VahidMohsseni"

DB = ""


def add_teacher(teacher, school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TABLE_NAME (name, grade, title, course, working_days, working_hours, school_id"
                       "VALUES (?, ?, ?, ?, ?, ?)", (teacher.name, teacher.grade, teacher.title, teacher.course,
                                                     teacher.working_days, teacher.working_hours, school_id))

        return "OK"


def add_school(school):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TABLE_NAME (name, teachers, grades)"
                       "VALUES (?, ?, ?)", (school.name, school.teachers, school.grades))
        return "OK"


def add_course(course, school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TABLE_NAME (name, hour, grade, course_local_id, school_id)"
                       "VALUES (?, ?, ?, ?, ?)", (course.name, course.grade, course.id, school_id))
        return "OK"


def add_grade(grade, school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TABLE_NAME (name, grade_local_id, courses_list, time, school_id)"
                       "VALUES (?, ?, ?, ?, ?)", (grade.name, grade.id, grade.courses_list, grade.time, school_id))
        return "OK"


def get_teachers_by_school_id(school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TABLE_NAME WHERE school_id = ?", (school_id, ))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(temp.Teacher(row[0], row[1], row[2], row[3], row[4], row[5]))
        return result if not result == [] else "no data!"


def get_grades_by_school_id(school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TABLE_NAME WHERE school_id = ?", (school_id, ))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(temp.Grades(row[0], row[1], row[2], row[3]))
        return result if not result == [] else "no data!"


def get_courses_by_school_id(school_id):
    with MySQLdb.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TABLE_NAME WHERE school_id = ?", (school_id, ))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(temp.Course(row[0], row[1], row[2], row[3]))
        return result if not result == [] else "no data!"


