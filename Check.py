import os
import sys

from DevicesInfo import deviceid, devicesinfo
from Path import MainPath
from Title import TitleERROR, TitleTrue

ResCheckList = ['aapt','aapt.exe','adb.exe','AdbWinApi.dll','AdbWinUsbApi.dll','fastboot.exe','findstr.exe']#资源包内部文件


def check():
    os.chdir(MainPath())#切换到AST主文件夹
    TitleTrue()
    print("\033[1;36;40m————By HoneyWhiteCloud".rjust(124, " ")+'\033[0m')
    os.system("title 正在检查ADB文件是否完整……")
    if not os.path.exists('res'):
        os.system('cls')
        os.system("title 工具箱主文件夹丢失！")
        TitleERROR()#抛出错误信息
        print("\n请您在杀毒软件内信任本软件或关闭杀毒软件后运行本程序！，本程序内无任何恶意代码！")
        input("\n回车以退出……")
        sys.exit()
        
    os.chdir(os.path.split(os.path.abspath('res'))[0])
    os.chdir(os.path.abspath('res'))#切换路径到资源文件夹下

    for i in ResCheckList:#检查res文件夹内文件是否齐全
        if not os.path.exists(i):
            os.system('cls')
            os.system("title 工具箱依赖资源丢失！")
            TitleERROR()
            print('\033[1;31m'+"\n{}文件丢失".format(i)+'\033[0m')
            print("\n请您在杀毒软件内信任本软件或关闭杀毒软件！，本程序内无任何恶意代码！")
            input("\n回车以退出……")
            sys.exit()
        else:
            pass
    print("依赖文件齐全，准备启动ADB服务\n")
    print("启动ADB服务中……")
    os.system("adb start-server")
    os.system("cls")
    StartValue = sys.argv[1:]
    if len(StartValue) == 0:
        return
    else:
        outlist=[]
        while True:
            StartValue = sys.argv[1:]
            chooseandinfo = deviceid()
            os.system("cls")
            os.system("title AST工具箱快捷模式")
            TitleTrue()
            print("\n您欲安装的APK↓\n")
            for index,luj in enumerate(StartValue):
                try:
                    filevalue = os.path.splitext(luj)[-1]
                except:
                    pass
                if ".apk" == filevalue.lower():
                    cmd = os.popen('aapt.exe dump badging {} | findstr application-label-zh-CN:'.format(luj))
                    try:
                        out = cmd.buffer.read().decode('utf-8').strip().replace("'",'').rsplit(":",2)[1]
                        pass
                    except Exception:
                        cmd = os.popen('aapt.exe dump badging {} | findstr application-label:'.format(luj))
                        try:
                            out = cmd.buffer.read().decode('utf-8').strip().replace("'",'').rsplit(":",2)[1]
                            pass
                        except Exception:
                            out = "空应用名"
                    print(index+1,'\033[1;32m'+"[{}]{}".format(out,luj)+'\033[0m')
                    outlist.append([out,luj])
                    pass
                else:
                    print(index+1,'\033[1;32m'+luj+'\033[0m'+'\033[1;31m'+" <---不是APK文件！安装时会被忽略！"+'\033[0m')
                    pass

            if len(outlist) == 0:#判断传入文件是否都为非APK文件
                print('\033[1;31m'+"\n您所拖动安装的文件都不为APK文件！"+'\033[0m')
                input("\n回车以退出……")
                os.system("cls") 
                print("结束ADB服务中……")
                os.system("adb.exe kill-server")
                os.system("cls")
                print("已结束ADB程序……")
                sys.exit()
            else:
                if len(chooseandinfo) == 1 and chooseandinfo[0][-1] == 'device':
                    choose = str(chooseandinfo[0][0])
                    input("\n回车确认后将所有APK安装到{}:".format('\033[4;33m'+'['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose+'\033[0m'))
                    num = 0
                    SuccessInstall = []
                    for index,i in enumerate(outlist):
                        os.system('cls')
                        out = i[0]
                        print("应用:{}正在安装到{}中……".format('\033[4;33m'+out+'\033[0m','\033[4;33m'+'['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose+'\033[0m'))
                        command = os.popen("adb.exe -s {} install -r {}".format(choose,i[-1]))
                        result = command.buffer.read().decode('utf-8')
                        if 'Success' in result:
                            num+=1
                            SuccessInstall.append(i)
                            pass
                        else:
                            pass
                        pass
                    os.system("cls")
                    print('\033[1;32m'+"安装完成！"+'\033[0m\n')
                    for index,i in enumerate(outlist):
                        if SuccessInstall.count(i) > 0:
                            print(index+1,"\033[1;32m[{}]{}{}\033[0m".format(i[0],i[-1]," \033[1;32m安装成功！\033[0m"))
                            pass
                        else:
                            print(index+1,"\033[1;32m[{}]{}{}\033[0m".format(i[0],i[-1]," \033[1;31m未安装成功！\033[0m"))

                    print("\n成功安装了{}个，共{}个,到{}".format(num,len(outlist),'\033[4;33m'+'['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose+'\033[0m'))
                    input("\n回车以退出……")
                    os.system("cls") 
                    print("结束ADB服务中……")
                    os.system("adb.exe kill-server")
                    os.system("cls")
                    print("已结束ADB程序……")
                    sys.exit()

                elif len(chooseandinfo) > 1:
                    chooseandinfo = deviceid()
                    print('\n\033[4;33m'+"您已连接的设备列表↓回车以刷新已连接的设备列表！"+'\033[0m')
                    devicelist = devicesinfo()
                    for index,i in enumerate(devicelist):
                        print(index+1,i)

                    inp = input('\n\033[1;34m'+"您有多个设备，请输入您欲为其安装APK的设备数字:"+'\033[0m')
                    try:
                        inp = int(inp)
                        
                        if inp == "":
                            pass
                        elif inp == 0:
                            pass
                        elif inp > len(chooseandinfo) or int(inp) < 0 :
                            pass
                        elif chooseandinfo[inp-1][-1] == 'unauthorized':
                            os.system("cls")
                            print('\033[1;31m'+"您所选设备未授权调试，请检查后回车刷新重试！"+'\033[0m')
                            input()
                        else:
                            choose = str(chooseandinfo[inp-1][0])
                            num = 0
                            SuccessInstall = []
                            for index,luj in enumerate(outlist):
                                os.system('cls')
                                out = outlist[index][0]
                                print("应用:{}正在安装到{}中……".format('\033[4;33m'+out+'\033[0m','\033[4;33m'+'['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose+'\033[0m'))
                                command = os.popen("adb.exe -s {} install -r {}".format(choose,outlist[index][-1]))
                                result = command.buffer.read().decode('utf-8')
                                print(result)
                                if 'Success' in result:
                                    num+=1
                                    SuccessInstall.append(i)
                                    pass
                                else:
                                    pass
                                pass
                            os.system("cls")
                            print('\033[1;32m'+"安装完成！"+'\033[0m\n')
                            for index,i in enumerate(outlist):
                                if SuccessInstall.count(i) > 0:
                                    print(index+1,"\033[1;32m[{}]{}{}\033[0m".format(i[0],i[-1]," \033[1;32m安装成功！\033[0m"))
                                    pass
                                else:
                                    print(index+1,"\033[1;32m[{}]{}{}\033[0m".format(i[0],i[-1]," \033[1;31m未安装成功！\033[0m"))
                            print("\n成功安装了{}个，共{}个,到{}".format(num,len(outlist),'\033[4;33m'+'['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(choose)).read().strip()+']'+choose+'\033[0m'))
                            inp = input("\n回车以继续将APK安装到其他设备，输入0以退出……")
                            if inp == "0":
                                os.system("cls") 
                                print("结束ADB服务中……")
                                os.system("adb.exe kill-server")
                                os.system("cls")
                                print("已结束ADB程序……")
                                sys.exit()
                            else:
                                pass
                    except Exception:
                        os.system("cls")
                        print("输入有误，请重试！")
                        input()

                elif len(chooseandinfo) == 1 and chooseandinfo[0][-1] == 'unauthorized':
                    os.system("cls")
                    print('\033[1;31m'+"您连接的设备{}未授权调试，请在您的设备上允许调试后回车刷新重试！\033[0m".format('\033[0m'+'\033[4;33m'+chooseandinfo[0][0]+'\033[0m'+'\033[1;31m'))
                    input()
                    pass
                else:
                    os.system("cls")
                    print('\033[1;31m'+"您未连接任何设备，亦或者您的设备连接发生问题，请检查后回车刷新重试！"+'\033[0m')
                    input()
                pass
