import os

from Cmd import all_shell


def 更改DPI(choose,chooseandinfo):#更改DPI
    os.system("cls")
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
            os.system("cls")
            print('\033[1;31m')
            print('#####DPI修改界面#####\n\n'+'输入数字后回车以选择,输入0返回主界面\n')
            print('\033[0m')
            print('注：Physical density为您所连接的设备的原始DPI大小；Override density为您所连接的设备现在的DPI大小。')
            print('\033[1;32m')
            print('1、修改DPI大小')
            print('2、恢复DPI大小')
            print('\033[0m')
            DPI = os.popen("adb.exe -s {} shell wm density".format(choose)).readlines()
            if len(DPI) == 2 and 'Override density' in DPI[1]:
                print("您设备现在的DPI大小："+DPI[1].strip().replace('Override density: ', ''))
                print("您设备原来的DPI大小："+DPI[0].strip().replace('Physical density: ', ''))
                pass
            else:
                print("您设备现在的DPI大小（看来您并未修改您设备的DPI）："+DPI[0].strip().replace('Physical density: ', ''))
            #########################光标↓DPI显示↑
            print('\033[1;34m')
            cho = input("[DPI]"+'\033[0m')#命令行光标
            #########################光标↑判断↓
            if cho == '0':
                return
            elif cho == '1':
                os.system("cls")
                print('在下方键入您所需的DPI大小。注：如果您的设备系统为WearOS，DPI小于200时会导致应用无障碍无法打开、蜂窝移动数据设置界面无法进入等问题！')
                all_shell(choose," shell wm density " + input('\n\033[1;34m'+"DPI数值："+'\033[0m'))
                os.system('cls')
                print("修改完毕，回车以回到主界面，少数设备需重启后才能生效！\n")
                input('回车以返回主界面……')
                return
            elif cho == '2':
                os.system("cls")
                all_shell(choose," shell wm density reset")
                input("修改完毕，回车以回到主界面，少数设备需重启后才能生效！")
                return
            else:
                os.system("cls")
                print('\033[1;31m')
                input("请输入正确的数字,回车以继续：")
                print('\033[0m')
                pass