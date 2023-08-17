import os


def all_shell(choose,command):
    cmd = "adb.exe "+"-s "+choose+' '+command
    fp = os.popen(cmd)
    ret = fp.buffer.read().decode('utf-8')
    return ret

def ADB命令行():
    os.system("cls")
    #运行adb
    print('\033[1;31m'+'输入"exit"即可返回工具箱……'+'\033[0m'+"\n")
    os.system("cmd /k & adb.exe")
    return