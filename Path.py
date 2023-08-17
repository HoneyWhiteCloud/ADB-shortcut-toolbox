import os
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx


def get_desktop():#获取桌面路径
    key = OpenKey(HKEY_CURRENT_USER,r'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
    return QueryValueEx(key, "Desktop")[0]


def MainPath():#切换工作路径
    path = os.path.split(os.path.abspath(__file__))[0]
    return path