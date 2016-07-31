__author__ = "moeb1376"
__editor__ = "VahidMohsseni"


# {sat:0,sun:2,...}
class School:
    def __init__(self, name, teachers_list, grades_list):
        self.name = name
        self.teachers = teachers_list
        self.grades = grades_list


class Grades:
    def __init__(self, name, grade_id, courses_list, class_counter, time):
        self.name = name
        self.id = grade_id
        self.courses_list = courses_list
        self.time = time


class Course:
    def __init__(self, name, hour, grade, course_counter):
        self.name = name
        self.hour = hour
        self.grade = grade
        self.id = course_counter


class Teacher:
    def __init__(self, name, grade, title, course_list, working_days, working_hours):
        self.name = name
        self.title = title  # Mr. or Mrs.
        self.grade = grade
        self.course = course_list
        self.working_days = working_days  # exp:[1,3,4]
        self.working_hours = working_hours
