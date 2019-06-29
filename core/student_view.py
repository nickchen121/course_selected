from lib import common
from interface import common_interface, student_interface

user_info = {'username': None}


def login():
    print('欢迎来到登录功能')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的密码>>>')

    flag, msg = common_interface.login_interface(username, pwd, 'student')
    print(msg)

    if flag:
        user_info['username'] = username
        return True


def register():
    print('欢迎来到注册功能')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的密码>>>')

    msg = student_interface.register_interface(username, pwd)
    print(msg)

@common.login_auth('student')
def choose_school():
    print('欢迎来到选择学校功能')
    username = user_info['username']

    school_list = common.get_obj_list('school')
    for ind, school in enumerate(school_list):
        print(ind, school)

    school_choice = input('请输入你需要选择的学校序号>>>')
    school_name = school_list[int(school_choice)]

    msg = student_interface.choose_school_interface(username, school_name)
    print(msg)

@common.login_auth('student')
def choose_course():
    print('欢迎来到选择课程功能')

    username = user_info['username']

    # 1. 获取课程
    course_list = student_interface.get_school_course_list(username)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

    # 2. 选择课程
    course_choice = input('请输入你需要选择课程的序号>>>')
    course = course_list[int(course_choice)]
    msg = student_interface.choose_course_interface(username, course)
    print(msg)

@common.login_auth('student')
def check_score():
    print('欢迎来到查看成绩功能')

    username = user_info['username']

    # 1. 获取课程
    course_list = student_interface.get_student_course_list(username)

    for ind, course in enumerate(course_list):
        print(ind, course.name)

    # 2. 选择课程
    course_choice = input('请输入你需要选择课程的序号>>>')
    course = course_list[int(course_choice)]

    score = student_interface.check_score_interface(username, course)
    if score:
        print(f'{username}学生课程{course.name}的成绩为{score}')
    else:
        print('当前课程没有成绩')


def run():
    print('欢迎来到学生视图界面')

    msg = '''
    1. 注册
	2. 登录
	3. 选择学校
	4. 选择课程
	5. 查看成绩
	q. 退出
    '''

    func_dict = {
        '1': register,
        '2': login,
        '3': choose_school,
        '4': choose_course,
        '5': check_score,
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
