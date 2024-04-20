#-*- coding:utf-8 -*-
#作者：Honey White Cloud(3303599383)

import os
import sys
from traceback import print_exc

from About import 关于
from ADBshell import shell
from APPmanager import APKmanager
from ChangeDPI import 更改DPI
from Check import check
from ChooseDevices import 选择设备
from Cmd import ADB命令行
from DevicesHardwareInfo import 设备信息
from DevicesInfo import deviceid, devicesinfo
from Exit import exit
from FastbootMode import fastbootbox
from FileManager import 文件管理
from MiWatchMode import 停用
from ScreenShot import 截屏
from Title import TitleDanger, TitleERROR, TitleTrue
from wireless import 无线连接, 未连接设备连接

global choose
choose = '0'
version = "v0.77.6"#版本号一键修改

class ASTmain(object):
    def __init__(self):
        while True:
            try:
                os.system("mode con:cols=128 lines=9999")#设置窗口大小
                os.popen("chcp 936")#设置中文代码页
                check()
                self.main()
            except KeyboardInterrupt:
                pass
            except SystemExit:
                sys.exit()
            except:
                os.system('cls')
                os.popen("title 工具箱遇到错误！").read()
                TitleERROR()
                print('\033[1;31m'+"\n工具箱遇到错误！"+'\033[0m')
                print("\n报错如下↓")
                print('\033[1;31m')
                print_exc()
                print('\033[0m\n')
                print("如果您能将此问题截屏发给开发者(QQ：3303599383)，不胜感激！")
                input("\n回车以重启工具箱……")
                os.chdir(os.path.split(os.path.abspath('res'))[0])
                pass

    def main(self):
        global choose
        while True:
            os.system("cls")
            os.system("title AST快捷工具箱 {} 主功能界面".format(version))
            TitleTrue()
            print('\033[1;32m                                 ADB快捷工具箱 版本：{} CTS云顶工作室 出品(1020918195)\033[0m'.format(version))
            print('\033[1;31m######主界面######(可按F11进入全屏模式)\n\033[0m')
            print('\033[1;31m请确保您的设备已开启开发者模式——ADB（或USB）（华为设备可能为HDC调试）调试！\nTips:在主界面直接输入ADB指令可以快速单次执行!\033[0m')
            print('\033[1;32m')
            print("输入各选项前的数字以选择↓直接回车即可刷新已连接的设备列表")
            print("\n[1]、 无线连接调试相关功能")
            print("[2]、 应用管理")
            print("[3]、 改变DPI大小")
            print("[4]、 ADB SHELL")
            print("[5]、 ADB 命令行")
            print("[6]、 截屏&录屏")
            print("[7]、 文件管理(预览版)")
            print("[8]、 所选设备的信息")
            print("[9]、 选择您要调试的设备（当您连接了多个设备时使用）")
            print("[10]、 增强米表性能&恢复（仅供小米手表使用）")
            print("[11]、 高级选项")
            print("[12]、 关于本工具箱(第一次使用必看)")
            print("[13]、 结束ADB进程、清理临时文件并退出")
            print('\033[0m')

            print('\033[4;33m'+"您已连接的设备列表↓回车以刷新已连接的设备列表！"+'\033[0m')
            for index,i in enumerate(devicesinfo()):
                if i == 0:
                    print('\033[1;31m'+"您未连接设备，请连接您要调试的设备！"+'\033[0m')
                    pass
                else:
                    print(index+1,i)
            print('\033[4;33m'+"已选择的调试设备(默认选择第一个允许调试的设备)：\n"+'\033[0m',end = '')
            chooseandinfo = deviceid()
            if  chooseandinfo== []:
                choose = '0'
                print('\033[1;31m'+"您未连接设备，请连接您要调试的设备！"+'\033[0m')
                pass
            else:
                for index,i in enumerate(chooseandinfo):
                    if len(chooseandinfo) > 1 and choose == '0' and chooseandinfo[index][-1] == 'device':
                        choose = str(chooseandinfo[0][0])
                        print('['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose)
                        break
                    elif len(chooseandinfo) == 1 and chooseandinfo[index][-1] == 'device':
                        choose = str(chooseandinfo[0][0])
                        print('['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose)
                        break
                    elif len(chooseandinfo) > 1 and choose == '0':
                        choose = str(chooseandinfo[0][0])
                        print(choose)
                        break
                    elif len(chooseandinfo) == 1:
                        choose = str(chooseandinfo[0][0])
                        print(choose)
                        break
                    else:
                        print('['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose)
                        break
            
            #####################显示↑光标↓
            com = input('\n\033[1;34m'+"[ADB Tool Box]:"+'\033[0m')#命令行光标

            if com == "":
                continue
            elif com == '13':
                exit()
            elif com == '5':
                ADB命令行()
                continue
            elif com == '1':
                未连接设备连接()
                continue
            elif com == "12":
                关于(version)
                continue
            elif choose == '0':
                os.system("cls")
                print('\033[1;31m'+"您未连接您的设备，亦或者是您的设备未打开ADB（或USB）调试（华为设备为HDC调试），请确保您已连接好您的设备，并在您的设备上允许调试后再试！\n"+'\033[0m')
                input("回车以返回主界面……")
                continue
            elif not chooseandinfo[index][-1] == 'device':
                os.system("cls")
                print('\033[1;31m'+"您的设备没有授权调试！亦或者您的设备连接出现问题，请查看您的设备是否允许调试后再试！\n"+'\033[0m')
                input("回车以返回主界面……")
                continue
            if com == '1':
                无线连接(choose,chooseandinfo)
                pass
            elif com == '2':
                APKmanager(choose)
                pass
            elif com == '3':
                更改DPI(choose,chooseandinfo)
                pass
            elif com == '4':
                shell(choose,chooseandinfo)
                pass
            elif com == '5':
                ADB命令行()
                pass
            elif com == '6':
                截屏(choose,chooseandinfo)
                pass
            elif com == '7':
                文件管理(choose)
                pass
            elif com == '8':
                设备信息(choose,chooseandinfo)
                pass
            elif com == '9':
                dev = 选择设备(chooseandinfo)
                if dev == "":
                    pass
                else:
                    choose = dev
                pass
            elif com == '10':
                停用(choose,chooseandinfo)
            elif com == '11':
                fastbootbox(choose,chooseandinfo)
                pass
            elif com == '12':
                关于(version)
                pass
            elif com == '13':
                exit()
            elif com == '':
                pass
            else:
                os.system("cls")
                print('\033[1;31m'+"执行指令中……"+'\033[0m'+"\n")
                try:
                    os.system(com)
                    input("\n回车以返回主界面……")
                    pass
                except Exception:
                    print("未知错误")
                    pass
                    
if __name__ == '__main__':
    ASTmain()
    pass
