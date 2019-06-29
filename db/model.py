from db import db_handler


class BaseClass():

    def save(self):
        db_handler.save_file(self)

    @classmethod
    def read(cls, name):
        obj = db_handler.read_file(cls.__name__.lower(), name)
        return obj


class Teacher(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.course_list = []
        self.save()

    def add_course(self, course):
        self.course_list.append(course)
        self.save()

    def modify_score(self, student, course, score):
        student.course_score[course.name] = score
        student.save()


class Student(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = ''
        self.course_list = []
        self.course_score = dict()
        self.save()

    def get_school(self):
        if self.school:
            return self.school

    def choose_school(self, school):
        self.school = school
        self.save()

    def add_course(self, course):
        self.course_list.append(course)
        self.save()


class Course(BaseClass):
    def __init__(self, name):
        self.name = name
        self.student_list = []
        self.save()

    def add_student(self, student):  # course
        self.student_list.append(student)
        self.save()


# 2. 刚开始学校绑定的课程一定是空的，然后学生添加到课程列表里，但是没有被修改

class School(BaseClass):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_list = []
        self.save()

    def add_course(self, course):
        self.course_list.append(course)
        self.save()


class Admin(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def create_school(self, name, addr):
        School(name, addr)

    def create_course(self, name):
        Course(name)

    def create_teacher(self, name, pwd):
        Teacher(name, pwd)


if __name__ == '__main__':
    admin = Admin('nick', 123)
    admin.create_course('python')
    admin.create_teacher('nick', 123)

    # classmethod只是让下面的代码变成下下面的代码
    # nick = db_handler.read_file('teacher', 'nick')  # type:Teacher
    # python = db_handler.read_file('course', 'python')

    nick = Teacher.read('nick')
    python = Course.read('python')

    print(nick)
    print(nick.name)
    nick.add_course(python)
    print(nick.__dict__)
