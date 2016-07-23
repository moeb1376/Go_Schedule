__author__ = "moeb1376"
__editor__ = "VahidMohsseni"


class School:
    def __init__(self, teachers_list, grades_list):
        self.teachers = teachers_list
        self.grades = grades_list


class Grades:
    def __init__(self, name, grade_id):
        self.name = name
        self.id = grade_id
        self.courses_list = None


class Course:
    def __init__(self, name, hour, grade, course_counter):
        self.name = name
        self.hour = hour
        self.grade = grade
        self.id = course_counter


class Teacher:
    def __init__(self, name, title, course_list, working_days, working_hours):
        self.name = name
        self.title = title  # Mr. or Mrs.
        self.course = course_list
        self.working_days = working_days
        self.working_hours = working_hours
