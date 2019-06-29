from db import model


def get_school_course_interface(school_name):
    school_obj = model.School.read(school_name)

    return school_obj.course_list


def get_teacher_course_interface(username):
    teacher_obj = model.Teacher.read(username)

    return teacher_obj.course_list


def choose_course_interface(username, course):
    teacher_obj = model.Teacher.read(username)

    if course in teacher_obj.course_list:
        return '课程已经存在'

    course = model.Course.read(course.name)
    teacher_obj.add_course(course)
    return f'老师{username}添加课程{course.name}成功'


def modify_score_interface(username, course, student, score):
    teacher_obj = model.Teacher.read(username)

    teacher_obj.modify_score(student, course, score)

    return f'老师{username}给学生{student.name}课程{course.name}打分{score}'

def get_course(course):
    course_obj = model.Course.read(course.name)

    return course_obj