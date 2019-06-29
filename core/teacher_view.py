from lib import common
from interface import common_interface, teacher_interface

user_info = {'username': None}


def login():
    print('欢迎来到登录功能')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的密码>>>')

    flag, msg = common_interface.login_interface(username, pwd, 'teacher')
    print(msg)

    if flag:
        user_info['username'] = username
        return True

@common.login_auth('teacher')
def choose_course():
    print('欢迎来到选择课程功能')

    username = user_info['username']

    school_list = common.get_obj_list('school')
    for ind, school in enumerate(school_list):
        print(ind, school)

    school_choice = input('请选择你需要获取的学校的序号>>>')
    school_name = school_list[int(school_choice)]

    course_list = teacher_interface.get_school_course_interface(school_name)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

    course_choice = input('请选择你需要获取课程的序号>>>')
    course = course_list[int(course_choice)]

    msg = teacher_interface.choose_course_interface(username, course)
    print(msg)

@common.login_auth('teacher')
def check_course():
    print('欢迎来到查看课程功能')

    username = user_info['username']

    course_list = teacher_interface.get_teacher_course_interface(username)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

@common.login_auth('teacher')
def check_student():
    print('欢迎来到查看学生功能')

    username = user_info['username']

    course_list = teacher_interface.get_teacher_course_interface(username)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

    course_choice = input('请输入你需要选择的课程>>>')
    course = course_list[int(course_choice)]

    course = teacher_interface.get_course(course)

    for student in course.student_list:
        print(student.name)


@common.login_auth('teacher')
def modify_score():
    print('欢迎来到修改成绩功能')

    username = user_info['username']

    course_list = teacher_interface.get_teacher_course_interface(username)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

    course_choice = input('请输入你需要选择的课程>>>')
    course = course_list[int(course_choice)]

    course = teacher_interface.get_course(course)
    student_list = course.student_list

    for ind, student in enumerate(student_list):
        print(ind, student.name)

    student_choice = input('请输入你需要打分的学生>>>')
    student = student_list[int(student_choice)]

    score = input('请输入你需要打的分数>>>')

    msg = teacher_interface.modify_score_interface(username, course, student, score)
    print(msg)


def run():
    print('欢迎来到老师视图界面')

    msg = '''
        1. 登录
        2. 选择课程
        3. 查看课程
        4. 查看学生
        5. 修改学生成绩
        q. 退出
        '''

    func_dict = {
        '1': login,
        '2': choose_course,
        '3': check_course,
        '4': check_student,
        '5': modify_score,
    }

    while True:
        print(msg)
        func_choice = input('请选择你需要的功能>>>')

        if func_choice == 'q':
            break

        if func_choice not in func_dict:
            print('傻逼,功能不存在')
            continue

        func_dict[func_choice]()
