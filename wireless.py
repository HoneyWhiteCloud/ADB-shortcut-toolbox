import os

def 无线连接(choose,chooseandinfo):#无线连接
    while True:
        os.system("cls")
        print("{}#####无线调试界面#####{}\n\n请打开您设备上的“WLAN调试”或者“通过无线调试”选项，且您的设备需和您的电脑在同一区域网内，且路由器的“AP隔离”为关闭状态".format('\033[1;31m','\033[0m'))
        
        print('\033[1;32m')
        print("1、USB转wlan调试")
        print("2、输入IP和端口进行wlan调试（无需选择要调试的设备）")
        print("3、断开所有已无线连接的设备")
        print('\033[0m')

        afd = input("\n请选择您的调试方法，输入0以返回主界面：")
        if afd == '1':
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
                while True:
                    os.system("cls")
                    if '.' in choose:
                        input("您的设备已为wifi连接设备，无需再转为wlan调试，回车以返回主界面：")
                        return
                    else:
                        pass
                    try:
                        IP = os.popen("adb.exe -s {} shell ip addr show wlan0 | findstr inet".format(choose)).readlines()[0]
                        pass
                    except Exception:
                        os.system("cls")
                        print('\033[1;31m'+"您的设备可能没有连接网络，亦或者您调试的设备是虚拟机（不支持无线调试），请检查您设备的网络连接后再试！\n"+'\033[0m')
                        if input("回车以重试，输入0以返回主界面：") == '0':
                            return
                        else:
                            continue
                    IP = list(IP)
                    del IP[0:8]
                    IP = ''.join(IP).rsplit("/")[0]
                    IP3 = IP+":5555"
                    os.popen("adb.exe -s "+choose+" tcpip 5555").read()
                    print("连接中……设备调试端口为5555……")
                    out = os.popen("adb.exe -s "+choose+" connect "+IP3).read()
                    if 'connected' in out:
                        os.system("cls")
                        print("设备'\033[4;33m{}\033[0m'连接成功！\n".format(IP3.strip()))
                    input("回车以继续……")
                    return
        elif afd == '2':
            os.system("cls")
            os.system("cls")
            print("点击您设备连接的网络即可查看设备的IP地址")
            ip = str(input("\n请输入您的设备的IP地址,如(192.168.1.1):"))
            port = str(input("\n请输入您的设备的端口号，如(5555):"))
            os.system("cls")
            print("连接设备中……如长时间未连接成功请检查IP地址或端口后重试！")
            cP = os.popen("adb.exe connect {}:{}".format(ip,port)).read()
            if 'connected to ' in cP:
                os.system("cls")
                input('\033[1;32m'+"设备已连接！回车以返回主界面"+'\033[0m')
                return
            elif'unable to connect' in cP:
                os.system("cls")
                input('\033[1;31m'+"设备未能连接，请检查您是否输入了正确的IP地址和端口号，或检查您的路由器是否开启了AP隔离（需关闭），检查设备是否开启“WLAN调试”！回车以返回选择界面"+'\033[0m')
            elif afd == '0':
                return
        elif afd == '3':
            os.system("cls")
            af = input('\033[1;31m'+"确定断开所有已连接的无线连接？输入0返回上一级："+'\033[0m')
            if af == '0':
                pass
            else:
                os.system("cls")
                os.popen("adb.exe disconnect").read()
                input("已断开，回车以返回主界面")
                return
            
        elif afd == '0':
            return
        else:
            pass

def 未连接设备连接():
    os.system("cls")
    print("{}#####无线连接设备界面#####{}\n\n请打开您设备上的“WLAN调试”或者“通过无线调试”选项，且您的设备需和您的电脑在同一区域网内，且路由器的“AP隔离”为关闭状态".format('\033[1;31m','\033[0m'))
    print("点击您设备连接的网络即可查看设备的IP地址")
    ip = str(input("\n请输入您的设备的IP地址,如(192.168.1.1):"))
    port = str(input("\n请输入您的设备的端口号，如(5555):"))
    os.system("cls")
    print("连接设备中……如长时间未连接成功请检查IP地址或端口后重试！")
    cP = os.popen("adb.exe connect {}:{}".format(ip,port)).read()
    if 'connected to ' in cP:
        os.system("cls")
        input('\033[1;32m设备已连接！回车以返回主界面\033[0m')
        return
    elif'unable to connect' in cP:
        os.system("cls")
        input('\033[1;31m'+"设备未能连接，请检查您是否输入了正确的IP地址和端口号，或检查您的路由器是否开启了AP隔离（需关闭），检查设备是否开启“WLAN调试”！回车以返回选择界面"+'\033[0m')
