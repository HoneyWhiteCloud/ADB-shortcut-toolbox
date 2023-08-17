import os

from DevicesInfo import deviceid


def 选择设备(chooseandinfo):
    while True:
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
            idc = deviceid()
            if len(idc) == 1:
                os.system("cls")
                print('\033[1;31m'+"您已连接了一个设备，无需再次选择调试设备！\n"+'\033[0m')
                input("回车以返回主界面……")
                return
            elif len(idc) == 0:
                os.system("cls")
                print('\033[1;31m'+"您未连接任何设备！\n"+'\033[0m')
                input("回车以返回主界面……")
                return
            else:
                os.system("cls")
                print("您已连接的设备↓")
                idx = deviceid()
                print('\033[1;32m')
                for index,item in enumerate(idx):
                    print(index+1,item[0])
                print('\033[0m')
                num = int(input("请键入对应数字以选择设备："))
                idc = deviceid()
                用户选择设备 = True
                choose = idc[num-1][0]
                os.system('cls')
                input("您已选择{}作为调试设备，回车以返回主界面：".format('\033[4;33m'+choose+'\033[0m'))
                return choose