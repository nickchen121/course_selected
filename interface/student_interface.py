from db import model


def register_interface(username, pwd):
    student_obj = model.Student.read(username)

    if student_obj:
        return f'{username}被注册了'

    model.Student(username, pwd)

    return f'{username}注册成功'


def choose_school_interface(username, school_name):
    student_obj = model.Student.read(username)
    school_obj = model.School.read(school_name)

    if student_obj.school:
        return '已经绑定学校,无法再绑定'
    
    student_obj.choose_school(school_obj)

    return f'{username}绑定学校{school_name}成功'


def get_school_course_list(username):
    student_obj = model.Student.read(username)
    if not student_obj.school:
        return '请先选择学校'

    school_obj = model.School.read(student_obj.school.name)

    return school_obj.course_list


def choose_course_interface(username, course):
    student_obj = model.Student.read(username)

    if course in student_obj.course_list:
        return '课程已经存在'

    course = model.Course.read(course.name)
    # 课程一直是学校的课程
    student_obj.add_course(course)
    course.add_student(student_obj)

    return f'{username}选课{course.name}成功'


def get_student_course_list(username):
    student_obj = model.Student.read(username)

    return student_obj.course_list


def check_score_interface(username, course):
    student_obj = model.Student.read(username)

    score = student_obj.course_score.get(course.name)

    return score
