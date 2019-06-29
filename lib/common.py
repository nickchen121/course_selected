import os
from conf import settings

def login_auth(classify):
    from core import admin_view, student_view, teacher_view
    def outer(func):
        def wrapper(*args, **kwargs):

            flag = False

            if classify == 'admin':
                if admin_view.user_info['username']:
                    res = func(*args, **kwargs)
                    return res
                flag = admin_view.login()

            elif classify == 'teacher':
                if teacher_view.user_info['username']:
                    res = func(*args, **kwargs)
                    return res
                flag = teacher_view.login()

            elif classify == 'student':
                if student_view.user_info['username']:
                    res = func(*args, **kwargs)
                    return res
                flag = student_view.login()

            # 登录成功后运行函数func
            if flag:
                res = func(*args, **kwargs)
                return res
            else:
                print('登录失败')

        return wrapper

    return outer

def get_obj_list(name):
    obj_list = os.listdir(os.path.join(settings.DB_PATH, name))
    return obj_list