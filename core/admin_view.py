from interface import common_interface, admin_interface
from lib import common

user_info = {'username': None}


def login():
    print('欢迎来到登录功能')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的密码>>>')

    flag, msg = common_interface.login_interface(username, pwd, 'admin')
    print(msg)

    if flag:
        user_info['username'] = username
        return True


def register():
    print('欢迎来到注册功能')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的的密码>>>')

    msg = admin_interface.register_interface(username, pwd)
    print(msg)


@common.login_auth('admin')
def create_school():
    print('欢迎来到创建学校功能')
    username = user_info['username']
    school_name = input('请选择你需要创建的学校名>>>')
    school_addr = input('请选择你需要创建的学校地址>>>')

    msg = admin_interface.create_school_interface(username, school_name, school_addr)
    print(msg)


@common.login_auth('admin')
def create_teacher():
    print('欢迎来到创建老师功能')
    username = user_info['username']
    teacher_username = input('请选择你需要创建老师的名字>>>')
    teacher_pwd = input('请选择你需要创建老师的密码>>>')

    msg = admin_interface.create_teacher_interface(username, teacher_username, teacher_pwd)
    print(msg)


@common.login_auth('admin')
def create_course():
    print('欢迎来到创建课程功能')
    username = user_info['username']
    school_list = common.get_obj_list('school')
    print(school_list)
    school_name = input('请选择你需要选择的学校')

    course_name = input('请输入你需要创建课程的名字>>>')

    msg = admin_interface.create_course_interface(username, course_name, school_name)
    print(msg)


def run():
    print('欢迎来到管理员视图界面')

    msg = '''
    1. 注册
    2. 登录
    3. 创建学校
    4. 创建老师
    5. 创建课程
    q. 退出
    '''

    func_dict = {
        '1': register,
        '2': login,
        '3': create_school,
        '4': create_teacher,
        '5': create_course,
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
