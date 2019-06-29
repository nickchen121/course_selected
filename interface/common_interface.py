from db import db_handler


def login_interface(username, pwd, classify='admin'):
    obj = db_handler.read_file(classify, username)

    if not obj:
        return False, '用户不存在'

    if obj.pwd == pwd:
        return True, '登录成功'
    return False, '登录失败'
