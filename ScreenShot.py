import os
from Cmd import all_shell
from Path import get_desktop

def 截屏(choose,chooseandinfo):#截屏&录屏
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
            print("可对您的安卓设备进行截屏＆录屏操作，输入0返回主界面\n")
            
            print("1、截屏")
            print("2、录屏")
            
            print('\033[1;34m')
            xz = input("您的选择：")#命令行光标
            print('\033[0m')
            if xz == '1':
                os.system("cls")
                input("回车以截屏:")
                os.system("cls")
                print("截屏中……")
                all_shell(" shell /system/bin/screencap -p /sdcard/Screenshot.png")
                桌面路径 = ''.join(get_desktop())
                all_shell(" pull /sdcard/Screenshot.png "+桌面路径)
                程序原来执行的路径 = os.getcwd()
                devicename = os.popen("adb.exe "+"-s "+choose+" -d shell getprop ro.product.model").read().replace('\n','')
                os.chdir(桌面路径)#切换至桌面
                num = 0
                if ":" in choose:
                    choose1 = choose.rsplit(":")[1]
                    pass
                else:
                    choose1 = choose
                path = devicename+'-'+choose1+"的截屏.png"
                while True:#检查桌面是否有 choose+"的截屏.png" 的文件
                    if os.path.exists(path):
                        num += 1
                        path = devicename+'-'+choose1+"的截屏("+str(num)+").png"
                        pass
                    else:
                        os.rename("Screenshot.png",path)
                        break
                os.chdir(程序原来执行的路径)#返回初始目录
                all_shell(" shell rm /sdcard/Screenshot.png")#删除安卓设备上的截屏图片
                os.system("cls")
                print("截屏成功！"+'\033[4;33m'+choose+'\033[0m'+"的截屏已保存至桌面！")
                input("\n回车以返回主界面：")
                return
            elif xz == '2':
                os.system("cls")
                input("回车以录屏")
                os.system("cls")
                print("录屏中，按Ctrl+C结束录制")
                桌面路径 = ''.join(get_desktop())
                all_shell(" shell screenrecord /sdcard/ScreenRecord.mp4")
                all_shell(" pull /sdcard/ScreenRecord.mp4 "+桌面路径)
                程序原来执行的路径 = os.getcwd()
                os.chdir(桌面路径)
                num = 0
                if ":" in choose:
                    choose1 = choose.rsplit(":")[1]
                    pass
                else:
                    choose1 = choose
                path = choose1+"的录屏.mp4"
                while True:#检查桌面是否有 choose+"的录屏.mp4" 的文件
                    if os.path.exists(path):
                        num += 1
                        path = devicename+'-'+choose1+"的录屏("+str(num)+").mp4"
                    else:
                        os.rename("ScreenRecord.mp4",path)
                        break
                os.chdir(程序原来执行的路径)#返回初始目录
                all_shell(" rm /sdcard/ScreenRecord.mp4")
                os.system("cls")
                print("录屏成功！"+'\033[4;33m'+choose+'\033[0m'+"的录屏已保存至桌面！")
                input("\n回车以返回主界面：")
                return
            elif xz == '0':
                return
            else:
                pass