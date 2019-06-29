from db import model


# 健壮性/鲁棒性/robust
def register_interface(username, pwd):
    obj = model.Admin.read(username)
    if obj:
        return '用户名已被使用'

    model.Admin(username, pwd)

    return '注册成功'

def create_school_interface(username,school_name,school_addr):
    admin_obj = model.Admin.read(username)
    school_obj = model.School.read(school_name)

    if school_obj:
        return f'{school_name}学校已经存在'

    admin_obj.create_school(school_name,school_addr)

    return f'{school_name}创建成功'


def create_teacher_interface(username,teacher_username,teacher_pwd):
    admin_obj = model.Admin.read(username)
    teacher_obj = model.Teacher.read(teacher_username)

    if teacher_obj:
        return f'{teacher_username}老师已经存在'

    admin_obj.create_teacher(teacher_username,teacher_pwd)

    return f'{teacher_username}创建成功'


def create_course_interface(username,course_name,school_name):
    admin_obj = model.Admin.read(username)
    school_obj  = model.School.read(school_name)
    course_obj = model.Course.read(course_name)   # None

    # 课程在学校里,None,   []  --> [None]
    if course_obj in school_obj.course_list:
        return f'{course_name}课程已经存在'

    admin_obj.create_course(course_name)
    course_obj = model.Course.read(course_name)
    school_obj.add_course(course_obj)  # python对象


    return f'{course_name}创建成功'