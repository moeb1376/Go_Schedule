import temp.py


def teacher_data(my_teacher):
    available_hours = 0
    for i in my_teacher.grade:
        for j in my_teacher.working_days:
            available_hours += sum(i.time[j])
    if available_hours < my_teacher.working_hours:
        print my_teacher.name + 'roozhaye kari kam ast'


def grade_data(my_grade, teacher_list):
    available_hours = 0
    for i in teacher_list:
        if my_grade in i.grade:
            available_hours += i.working_hours
    if available_hours < sum(sum([i for i in my_grade.time])):
        print my_grade.name, 'moallemash kame'


def course_data(my_course, teacher_list):
    available_hours = 0
    for i in teacher_list:
        if my_course in i.course:
            available_hours += i.working_hours
    if available_hours < my_course.hour:
        print my_course.name, 'moallem kam dare'
    elif available_hours > my_course.hour:
        print my_course.name, 'moallem ziyad dare'
