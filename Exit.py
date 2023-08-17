import os
import sys


def exit():#退出
    os.system("cls") 
    print("结束ADB服务中……")
    os.system("adb.exe kill-server")
    os.system("cls")
    print("已结束ADB程序……")
    sys.exit()