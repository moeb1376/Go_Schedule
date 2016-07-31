import temp

__author__ = "VahidMohsseni"

grade_counter = 1
grade_dic = {}


def make_grade(grade_name, courses_list, class_counter):
    global grade_counter
    grade_dic[grade_name] = temp.Grades(grade_name, grade_counter, courses_list, class_counter)
    grade_counter += 1


course_counter = 1
course_name_id_dic = {}
course_dic = {}


def make_course(course_name, hour, grade_name):
    global course_counter
    course_name_id_dic[course_counter] = temp.Course(course_name, hour, grade_dic[grade_name], course_counter)
    course_counter += 1


teacher_counter = 1
teacher_name_id_dic = {}


def make_teacher(name, title, grade, course_list, days, hours):
    global teacher_counter
    teacher_name_id_dic[teacher_counter] = temp.Teacher(name, title, grade, course_list, days, hours)
    teacher_counter += 1
