class school:
    def __init__(self, courses, schedule_hours):
        self.courses = courses #list of course
        self.schedule_hours = schedule_hours #example [[2,2,2],[2,2,2],[2,2,2],[2,2,2],[2,2,2]]

class teacher:
    def __init__(self,course,working_days,working_hours,grade):
        self.course = course
        self.working_days = working_days
        self.working_hours = working_hours
        self.grade = grade

class course:
    def __init__(self,name,hour,grade):
        pass