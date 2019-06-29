import os
import pickle
from conf import settings


def save_file(obj):
    # 老师可能有nick,学生可能也有nick,如果都保存到db文件,则无法判断这个人为老师还是学生,所以对他们
    # 分文件夹处理

    # 创建文件夹
    classify = obj.__class__.__name__.lower()
    dir = os.path.join(settings.DB_PATH, classify)
    if not os.path.exists(dir):
        os.mkdir(dir)

    # 创建文件
    filename = os.path.join(dir, obj.name)

    with open(filename, 'wb') as fw:
        pickle.dump(obj, fw)


def read_file(classify, name):
    # 创建文件夹
    filename = os.path.join(settings.DB_PATH, classify,name)
    if not os.path.exists(filename):
        return False

    with open(filename, 'rb') as fr:
        obj = pickle.load(fr)

    return obj
