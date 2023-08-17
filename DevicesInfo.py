import os


def devicesinfo():#设备信息
    while True:
        try:
            name = []
            device = os.popen('adb.exe devices').readlines()
            del device[0]
            del device[-1]
            if len(device) == 0:
                name.append(0)
                pass
            else:
                for item in device:
                    lists = item.rsplit()
                    if 'device' in lists[-1]:
                        name.append('['+os.popen("adb.exe -s {} -d shell getprop ro.product.model".format(lists[0])).read().strip()+']'+lists[0]+ '\033[1;32m'+'     设备正常连接且已授权调试'+'\033[0m')
                        pass
                    elif 'unauthorized' in lists[-1]:
                        name.append(lists[0] + '\033[1;31m'+'     设备正常连接但并未授权调试'+'\033[0m')
                        pass
                    elif 'offline' in lists[-1]:
                        name.append(lists[0] + '\033[1;31m'+'     设备连接出现异常，设备无响应'+'\033[0m')
                        pass
                    elif 'unknown' in lists[-1]:
                        name.append(lists[0] + '\033[1;31m'+'     未知的设备连接状态'+'\033[0m')
                        pass
                    else:
                        name.append(item)
                        pass
                    pass
            return name
        except:
            input()
            os.system("cls")
            print("您电脑上有程序占用ADB端口，正在尝试杀掉ADB……（如长时间卡在此界面请重启本程序或电脑）")
            os.system("taskkill /im adb.exe /f")
            pass

def deviceid():#设备ID以及状态获取
    chooseandinfo = []
    all_info = os.popen('adb.exe devices').readlines()
    del all_info[0]
    del all_info[-1]
    for i in all_info:
        i = i.strip().rsplit('\t')
        del i[1:-1]
        chooseandinfo.append(i)
        pass
    return chooseandinfo

