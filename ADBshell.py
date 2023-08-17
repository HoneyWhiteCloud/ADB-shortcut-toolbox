import os


def shell(choose,chooseandinfo):#ADB shell
    for index, sublist in enumerate(chooseandinfo):
        if sublist[0] == choose:
            break
        else:
            pass
        pass
    if choose == '0':
        os.system("cls")
        print('\033[1;31m'+"您未连接您的设备，请确保您已连接好您的设备，并在您的设备上允许调试后再试！\n"+'\033[0m')
        input("回车以返回主界面……")
        return
    elif not chooseandinfo[index][-1] == 'device':
        os.system("cls")
        print('\033[1;31m'+"您的设备没有授权调试！亦或者您的设备连接出现问题，请查看您的设备是否运行调试后再试！\n"+'\033[0m')
        input("回车以返回主界面……")
        return
    else:
        os.system("cls")
        print('\033[1;31m')
        print("按Enter键进入所选设备的shell界面")
        input("按回车以继续:")
        print('\033[0m')
        #运行SHELL
        os.system("cls")
        print('\033[1;31m')
        print("输入exit即可返回主界面")
        print('\033[0m')
        os.system("adb.exe "+"-s "+choose+" shell")
        input("回车以返回主界面……")
        os.system("cls")
        return