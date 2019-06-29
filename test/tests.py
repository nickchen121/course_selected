from conf import settings
from core import admin_view,student_view,teacher_view
from db import db_handler,model
from interface import admin_interface,common_interface,student_interface,teacher_interface
from lib import common

python = db_handler.read_file('course','shpython')
print(python.__dict__)