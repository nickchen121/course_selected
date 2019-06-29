from core import admin_view,student_view,teacher_view





def run():
    print('欢迎来到主视图界面')
    func_dict = {
        '1': admin_view.run,
        '2': teacher_view.run,
        '3': student_view.run,
    }

    msg = '''
    1. 管理员视图
    2. 老师视图
    3. 学生视图
    q. 退出
    '''

    
    while True:
        print(msg)
        func_choice = input('请选择你需要的功能>>>')

        if func_choice == 'q':
            break
            
        if func_choice not in func_dict:
            print('傻逼,功能不存在')
            continue
        
        func_dict[func_choice]()