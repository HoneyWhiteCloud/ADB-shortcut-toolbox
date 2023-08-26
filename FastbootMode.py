import os

from Cmd import all_shell


def fastbootbox(choose,chooseandinfo):
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
            os.system('cls')
            print('\033[1;31m'+'#####高级模式#####\n'+'\033[0m')
            print("")
            print('\033[1;31m'+'请知晓您在做什么，如果您并不了解安卓的"fastboot"模式或"recovery"模式,请不要擅用本工具箱的高级功能！\n'+'\033[0m')
            print("输入0即可返回主界面\n")
            print('\033[1;32m')
            print("1、重启设备至recovery")
            print("2、重启设备至fastboot")
            print('\033[0m')

            #####################显示↑光标↓
            print('\033[1;34m')
            com = input("["+'高级模式'+"]:")#命令行光标
            print('\033[0m')
            #####################光标↑判断输入↓
            if com == "1":
                os.system('cls')
                print('命令执行中……')
                all_shell(choose,"reboot recovery")
                os.system('cls')
                print('\033[1;31m'+"已自动进入adb命令行，输入“exit”即可返回工具箱……"+'\033[0m')
                print('\033[1;31m'+"本功能只适用于recovery为完整CWM或TWRP的设备，如您不知道什么是recovery，或您不知道您的设备的recovery是什么，请自行百度您设备的型号"+'\033[0m'+"\n")
                os.system("cmd /k")
                return
            elif com == '2':
                os.system('cls')
                print('命令执行中……')
                all_shell(choose,"reboot bootloader")
                os.system('cls')
                print('\033[1;31m'+"已自动进入fastboot命令行，输入“exit”即可返回工具箱……"+'\033[0m')
                print('\033[1;31m'+"本功能只适用于已解bl锁的设备，如您不知道什么是bl锁，或您想解开bl锁，请自行百度您设备的型号"+'\033[0m'+"\n")
                print('\033[1;31m'+"命令格式：fastboot [命令选项...] 命令..."+'\033[0m'+"\n")
                os.system("cmd /k")
                return
            elif com == '0':
                return
            else:
                pass