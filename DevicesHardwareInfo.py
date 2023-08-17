import os

from Cmd import all_shell


def 设备信息(choose,chooseandinfo):
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
        print('\033[1;32m')
        print("\n您设备的设备型号:"+all_shell(choose," -d shell getprop ro.product.model"))
        print("\n您设备的厂商名称:"+all_shell(choose," -d shell getprop ro.product.brand"))
        print("\n您设备的系统版本:"+all_shell(choose," shell getprop ro.build.version.release"))
        print("\n您设备的系统ID："+all_shell(choose," shell settings get secure android_id"))
        print("\n您设备的API版本:"+all_shell(choose," shell getprop ro.build.version.sdk"))
        print("\n您设备的IMEI：")
        print(all_shell(choose," shell service call iphonesubinfo 1"))
        print("\n设备是否支持 Treble："+all_shell(choose," shell getprop ro.treble.enabled"))
        print("\n您设备的序列号："+all_shell(choose," shell getprop ro.serialno"))
        print("\n您设备的CPU架构："+all_shell(choose," shell getprop ro.product.cpu.abi"))
        print("\n您设备的内存信息：")
        print(all_shell(choose," shell cat /proc/meminfo"))
        print("\n您设备的储存信息：")
        print(all_shell(choose," shell df"))
        print("\n您设备sdcard存储信息：")
        print(all_shell(choose," shell df /sdcard"))
        print("\n您设备的分辨率："+all_shell(choose," shell wm size").rsplit(":",2)[1])
        DPI = os.popen("adb.exe -s {} shell wm density".format(choose)).readlines()
        if len(DPI) == 2 and 'Override density' in DPI[1]:
            print("您设备现在的DPI大小："+DPI[1].strip().replace('Override density: ', ''))
            print("您设备原来的DPI大小："+DPI[0].strip().replace('Physical density: ', ''))
            pass
        else:
            print("您设备现在的DPI大小（看来您并未修改您设备的DPI）："+DPI[0].strip().replace('Physical density: ', ''))
        print("\n")
        print('\033[0m')
        input("以上为您所连接的设备的信息，回车以退出……")
        return