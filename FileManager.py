import os


def 文件管理(choose):
    文件路径 = ['/sdcard'] #默认从sdcard开始读取
    本目录下的文件名列表 = []
    while True:
        os.system("cls")
        print('\033[1;31m######文件管理######(预览版)\n\033[0m')
        fp =  os.popen("adb.exe -s {} shell ls {} -1".format(choose,'/'.join(文件路径)))
        返回的ADB文件名 = fp.buffer.read().decode('utf-8').replace("\r","").rsplit("\n")[0:-1]
        fp1 =  os.popen("adb.exe -s {} shell ls {} -g".format(choose,'/'.join(文件路径)))
        返回的ADB文件信息 = fp1.buffer.read().decode('utf-8').replace("\r","").rsplit("\n")[1:-1]
        sdcard文件列表 = []
        if 返回的ADB文件信息 == []:
            os.system("cls")
            print("当前路径：{}\n".format('/'.join(文件路径)))
            print('\033[1;31m'+"该文件夹内没有文件！"+'\033[0m')
            i = input("\n回车以返回上一级，输入0返回根目录！:")
            if i == '0':
                文件路径 = ['/sdcard']
                continue
            else:
                del 文件路径[-1]
                continue
        for index,i in enumerate(返回的ADB文件信息):
            文件信息 = []
            i = i.rsplit(" ")
            for a in i:
                if a == " ":
                    pass
                else:
                    文件信息.append(a)
            if 文件信息[0] == "-rw-rw----":
                文件属性 = '文件  '
                pass
            else:
                文件属性 = '文件夹'
                pass
            文件名 = 返回的ADB文件名[index]
            a = [文件属性,文件名]
            sdcard文件列表.append(a)


        if len(sdcard文件列表) == 0 and 文件路径 == ['/sdcard']:#未接入设备
            os.system("cls")
            print("当前路径：{}\n".format('/'.join(文件路径)))
            print('\033[1;31m'+"您的设备连接发生错误，请检查您设备的连接情况！"+'\033[0m')
            input("\n回车以返回主界面:")
            return
        else:                                                                                                 #文件夹内有文件
            本目录下的文件名列表.clear()                                                                        #清空列表
            print("当前路径：{}\n".format('/'.join(文件路径)))
            print("输入数字以进入对应的下一级,输入b返回上一级,输入e返回根目录,输入0返回主界面\n")

            print('\033[1;32m')
            for index,i in enumerate(sdcard文件列表):
                lon = len(list(str(len(sdcard文件列表)))) - len(list(str(index+1)))
                print("["+str(index+1)+"] {}".format(" "*lon)+" {}：{}".format(i[0],i[-1]),flush=True)
                pass
            print('\033[0m')
            用户输入 = input("光标:")

            if 用户输入 == 'b' or 用户输入 == 'B':
                if 文件路径 == ['/sdcard']:
                    os.system("cls")
                    print('\033[1;31m'+"已返回至根目录！无需再返回！\n"+'\033[0m')
                    input("回车以继续……")
                    pass
                else:
                    del 文件路径[-1]
                    pass

            elif os.path.isfile(用户输入):
                os.system("cls")
                print("正在将{}传输到{}文件夹下……".format(用户输入,'/'.join(文件路径)))

                pass

            elif 用户输入 == 'e' or 用户输入 == 'E':
                if 文件路径 == ['/sdcard']:
                    os.system("cls")
                    print('\033[1;31m'+"已返回至根目录！无需再返回！\n"+'\033[0m')
                    input("回车以继续……")
                    pass
                else:
                    文件路径 = ['/sdcard']
                    pass
                pass

            elif 用户输入 == '0':
                return
            else:
                try:
                    用户输入 = int(用户输入)
                    sdcard文件列表[用户输入-1][0]
                    if sdcard文件列表[用户输入-1][0] == "文件  ":
                        os.system("cls")
                        print('\033[1;31m'+"文件不可进入！\n"+'\033[0m')
                        input("回车以返回上一级……")
                        pass
                    else:
                        文件路径.append(sdcard文件列表[用户输入-1][-1])
                        pass
                except BaseException as e:
                    os.system("cls")
                    print(e)
                    print('\033[1;31m'+"输入有误，请重试！\n"+'\033[0m')
                    input("回车以继续……")
                pass


"""def apk路径():
    desktoppath = get_desktop()
    lpszFilter = "所有文件 (*.*)|*.*|| "
    # 这里的构造方法，对应上面展示的构造方法
    dlg = win32ui.CreateFileDialog(True, "*", None, 0x04 | 0x02, lpszFilter)  # True表示打开文件对话框
    # 设置打开文件对话框中的初始显示目录
    dlg.SetOFNInitialDir(desktoppath)
    dlg.DoModal()
    # 等待获取用户选择的文件
    filename = dlg.GetPathName()  # 获取选择的文件名称
    # 如果用户点击了取消，则返回的filename为""，而不是None
    if filename == "":
        return None
    else:
        return filename"""