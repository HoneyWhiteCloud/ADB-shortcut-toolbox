#coding:utf-8
#作者：Honey White Cloud(3303599383)
import os
import sys
import time
import re
import subprocess
import threading
import itertools

global choose
choose = 0

fileadb = 'adb'
adbbody = 'adb/adb.exe'
AdbWinApi = 'adb/AdbWinApi.dll'
AdbWinUsbApi = 'adb/AdbWinUsbApi.dll'
fastboot = 'adb/fastboot.exe'

class Signal:#主函数，用于控制指针旋转的开始停止
    go = True

def 指针(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = msg + ' ' + char
        write(status)
        flush()
        time.sleep(.1)
        write('\x08' * len(status))
        if not signal.go:
              break
    write(' ' * len(status) + '\x08' * len(status))


def IO():
    #这里添加一个会花费长时间的IO
    time.sleep(1.5)#模拟花费时间
    return "Exited"#模拟返回值


def 主体():
    signal = Signal()
    spinner = threading.Thread(target=指针,
                               args=('Exiting', signal))
    spinner.start()
    result = IO()
    signal.go = False
    spinner.join()
    return result

class AdbTools(object):

    def __init__(self,device_id=''):
        self.check()
        self.main()
    
    def deal_result(self):
        device = os.popen('adb devices').readlines()
        del device[0]
        del device[-1]
        
        for index,item in enumerate(device):
            print(index +1,item,end='')
    
    def deviceid(self):#设备ID获取
        str_init=' '
        all_info= os.popen('adb devices').readlines()
        for i in range(len(all_info)):
            str_init+=all_info[i]
        devices_name=re.findall('\n(.+?)\t',str_init,re.S)
        return devices_name

    def check(self):
        print("检查ADB组件中……")
        #检查ADB文件是否完整
        if not os.path.exists(fileadb):
            PATH = "PATH:"+ "{" + fileadb + "}" + " could't found!\n"
            print("\nadb文件夹丢失:\n",PATH,"按回车以退出……")
            input()
            sys.exit()
            
        elif not os.path.exists(adbbody):
            PATH = "PATH:"+ adbbody + " could't found!\n"
            input("\nadb主文件丢失:\n",PATH,"按回车以退出……")
            input()
            sys.exit()
            
        elif not os.path.exists(AdbWinApi) :
            PATH = "PATH:"+ AdbWinApi + " could't found!\n"
            input("\n丢失文件：ADB auxiliary dll:\n",PATH,"按回车以退出……")
            input()
            sys.exit()
        elif not os.path.exists(AdbWinUsbApi):
            PATH = "PATH:"+ AdbWinUsbApi + " could't found!\n"
            input("\n丢失文件：AdbWinUsbApi.dll:\n",PATH,"按回车以退出……")
            input()
            sys.exit()
        elif not os.path.exists(fastboot):
            PATH = "PATH:"+ fastboot + " could't found!\n"
            input("\nfastboot主程序丢失:\n",PATH,"按回车以退出……")
            input()
        ######################
        else:
            os.chdir(fileadb)
            os.popen("adb.exe").readlines()#激活ADB
            print("done!")
            os.system("cls")
        ######################
            
    def main(self):
        while True:#循环体
            #显示
            os.system("cls")
            print('\033[5;32;40m' + "ADB快捷工具箱 版本：0.4 作者：Honey White Cloud（3303599383）" + '\033[0m')
            
            print('\033[1;31m')
            print("######主界面######")
            print('\033[0m')
            print('\033[1;31m'+"\n请先连接您的安卓设备，确保您的设备已开启开发者模式——ADB（或USB）调试！\n本版本为控制台版本（已不打算做UI -_-|||），仅支持一次安装单个APK文件，后续将会改善"+'\033[0m')
            
            print('\033[1;32m')
            print("\n输入各选项前的数字以选择↓输入任何非选项字符可刷新已连接的设备列表")
            print("\n1、 使用无线连接调试您的设备（有选项需选择要调试的设备）")
            print("2、 安装APK文件")
            print("3、 改变DPI大小")
            print("4、 ADB SHELL")
            print("5、 ADB 命令行（无需选择要调试的设备）")
            print("6、 截屏&录屏")
            print("7、 设备信息")
            print("8、 断开所有无线连接（无需选择要调试的设备）")
            print("9、 选择您要调试的设备")
            print("10、 激活您设备上的授权应用")
            print("11、 关于本工具箱（无需选择要调试的设备）")
            print("12、 优雅の退出（无需选择要调试的设备）\n")
            print('\033[0m')
            
            print('\033[4;33m'+"您已连接的设备↓(Tips:设备已连接并授权：device；设备已连接未授权：unauthorized；设备离线：offline"+'\033[0m')
            self.deal_result()
            
            print('\033[4;33m'+"已选择的调试设备：\n"+'\033[0m',end = '')
            if choose == 0:
                print('\033[1;31m'+"您未选择要调试的设备，请先输入“9”选择您要调试的设备！"+'\033[0m')
            else:
                print(choose)
            
            #####################显示↑光标↓
            print('\033[1;34m')
            com = input("["+fileadb+"]:")#命令行光标
            print('\033[0m')
            #####################光标↑判断输入↓
            if com == '1':
                self.无线连接()
            elif com == '2':
                self.安装APK()
            elif com == '3':
                self.更改DPI()
            elif com == '4':
                self.shell()
            elif com == '5':
                self.ADB命令行()
            elif com == '6':
                self.截屏()
            elif com == '7':
                self.设备信息()
            elif com == '8':
                self.断开无线调试()
            elif com == '9':
                self.选择设备()
            elif com == '10':
                self.激活()
            elif com == '11':
                self.关于()
            elif com == '12':
                self.退出()
            #########################判断输入↑def体↓
                
    def 退出(self):#退出
        os.system("cls")
        result = 主体()  # <15>
        print(result)
        time.sleep(1)
        sys.exit()
        
    def 更改DPI(self):#更改DPI
        os.system("cls")
        try:
            while True:
                os.system("cls")
                print('\033[1;31m')
                print('#####DPI修改界面#####\n\n'+'输入数字后回车以选择,输入0返回主界面\n')
                print('\033[0m')
                print('注：Physical density为您所连接的设备的原始DPI大小；Override density为您所连接的设备现在的DPI大小。')
                print('\033[1;32m')
                print('1、修改DPI大小')
                print('2、恢复DPI大小')
                print('\033[0m')
                wmsize = self.all_shell(" shell wm density")
                print(wmsize)
                #########################光标↓DPI显示↑
                print('\033[1;34m')
                cho = input("["+'DPI'+"]:")#命令行光标
                print('\033[0m')
                #########################光标↑判断↓
                if cho == '0':
                    return
                elif cho == '1':
                    os.system("cls")
                    print('在下方键入您所需的DPI大小。注：如果您的设备系统为WearOS，DPI小于200时会导致应用无障碍无法打开、蜂窝移动数据设置界面无法进入等问题！')
                    self.all_shell(" shell wm density " + input("DPI数值："))
                    input("修改完毕，回车以回到主界面，少数设备需重启后才能生效！")
                    return
                elif cho == '2':
                    os.system("cls")
                    self.all_shell(" shell wm density adbet")
                    input("修改完毕，回车以回到主界面，少数设备需重启后才能生效！")
                    return
                else:
                    os.system("cls")
                    print('\033[1;31m')
                    input("请输入正确的阿拉伯数字,回车以继续：")
                    print('\033[0m')
                    pass
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面后键入“9”选择您要调试的设备后再试！"+'\033[0m')
            return
        
    def shell(self):#ADB shell
        try:
            #警示语
            os.system("cls")
            print('\033[1;31m')
            print("按Enter键进入所选设备的shell界面")
            input("按回车以继续:")
            print('\033[0m')
            #运行SHELL
            os.system("cls")
            print('\033[1;31m')
            print("输入exit即可返回主界面")
            print('\033[0m')
            os.system("adb.exe "+"-s "+choose+" "+"  shell")
            input()
            os.system("cls")
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择(连接)您要调试的设备，回车返回主界面后键入“9”选择您要调试的设备后再试！"+'\033[0m')
            return
        
    def 安装APK(self):#安装APK文件
        try:
            while True:
                os.system("cls")
                print('\033[1;31m')
                print("#####APK安装界面#####\n\n将APK文件拖入进窗口后回车即可安装,输入0即可返回主界面\n若显示（No such file or directory），则说明您的设备没有您要安装的APK所需的库，无法安装")
                print('\033[0m')
                ###################### 
                print('\033[1;34m')
                luj = input("路径：")#命令行光标
                print('\033[0m')
                ###################### 
                if luj == '0':
                    return
                elif luj == '':
                    os.system("cls")
                    print('\033[1;31m')
                    input("输入的路径为空，回车以返回安装界面")
                    print('\033[0m')
                    pass
                else:
                    os.system("cls")
                    ins = self.all_shell(" install -r "+luj)
                    print(ins)
                    input("命令执行成功，如有ERROR报错（或Failure安装失败）则为缺库或为非WearOS设备安装了WearOS专用软件，亦或者APK文件不存在，回车可继续安装")
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面键入“9”选择您要调试的设备后再试！"+'\033[0m')
            return

    def 无线连接(self):#无线连接
        while True:
            os.system("cls")
            print("#####无线调试界面#####\n\n请打开您设备上的“WLAN调试”或者“通过无线调试”选项，且您的设备需和您的电脑在同一区域网内，且路由器的“AP隔离”为关闭状态")
            print("1、USB转wlan调试")
            print("2、输入IP和端口进行wlan调试（无需选择要调试的设备）")
            afd = input("\n请选择您的调试方法，键入其他字符以返回主界面：")
            if afd == '1':
                try:
                    os.system("cls")
                    mat = re.compile(str(r"192.168"))
                    resu = mat.findall(str(choose))
                    if resu == ['192.168']:
                        input("您的设备已为wifi连接设备，无需再转为wlan调试，回车以返回主界面：")
                        break
                    else:
                        pass
                    port1 = self.all_shell(" tcpip 5555")
                    IP1 = self.all_shell(" shell netcfg")
                    print(self.all_shell(" connect "+IP1+':'+"5555"))
                    input()
                except Exception:
                    os.system("cls")
                    input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面键入“9”选择您要调试的设备后再试！"+'\033[0m')
                    return
            elif afd == '2':
                os.system("cls")
                print('\033[1;31m')
                print('\033[0m')
                os.system("cls")
                print("点击您设备连接的网络即可查看设备的IP地址")
                port = str(input("\n请输入您的设备的端口号，如（5555）:"))
                IP = str(input("\n请输入您的设备的IP地址,如（192.168.1.1）:"))
                cP = os.popen("adb connect "+IP+':'+port).read()
                match = re.compile(r"connected to ")
                match1 = re.compile(r"unable to connect")
                result = match.findall(cP)
                result1 = match1.findall(cP)
                if result == ['connected to ']:
                    os.system("cls")
                    input("设备已连接！回车以返回主界面")
                    return
                elif result1 == ['unable to connect']:
                    os.system("cls")
                    input("设备未能连接，请检查您是否输入了正确的IP地址和端口号，检查设备是否开启“WLAN调试”！回车以返回选择界面")
                elif afd == '0':
                    return
            else:
                return
        
    def ADB命令行(self):
        os.system("cls")
        #运行adb
        os.system("cmd adb.exe")
        input("回车以返回主界面：")
        return
    
    def 截屏(self):#截屏&录屏
        try:
            while True:
                os.system("cls")
                print("可对您的安卓设备进行截屏＆录屏操作，输入0返回主界面\n")
                
                print("1、截屏")
                print("2、录屏(仅支持分辨率大于720x1280的设备")
                
                print('\033[1;34m')
                xz = input("您的选择：")#命令行光标
                print('\033[0m')
                
                if xz == '1':
                    os.system("cls")
                    input("回车以截屏:")
                    self.all_shell(" shell/system/bin/screencap -p /sdcard/screenshot.png")
                    self.all_shell(" shell/sdcard/screenshot.png %userprofile%\desktop")
                    input("回车以返回主界面：")
                    return
                if xz == '2':
                    os.system("cls")
                    print("默认录制时间为180s。按Ctrl+C结束录制")
                    input("回车以录屏")
                    self.all_shell(" shell screenrecord /sdcard/demo.mp4")
                    self.all_shell(" shell/sdcard./demo.mp4 %userprofile%\desktop")
                    input("回车以返回主界面：")
                    return
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面键入“9”选择您要调试的设备后再试！"+'\033[0m')
            return
        
    def all_shell(self,command):
        ret = os.popen("adb.exe "+"-s "+choose+' '+command).read()
        return ret
    
    def 设备信息(self):
        try:
            os.system("cls")
            print('\033[1;32m')
            print("\n您设备的设备型号:")
            self.all_shell(" -d shell getprop ro.product.model")
            print("\n您设备的厂商名称:")
            self.all_shell(" -d shell getprop ro.product.brand")
            print("\n您设备的系统版本:")
            self.all_shell(" shell getprop ro.build.version.release")
            print("\n您设备的系统ID：")
            self.all_shell(" shell settings get secure android_id")
            print("\n您设备的API版本:")
            self.all_shell(" shell getprop ro.build.version.sdk")
            print("\n您设备的IMEI：")
            self.all_shell(" shell service call iphonesubinfo 1")
            print("\n您设备的序列号：")
            self.all_shell(" shell getprop ro.serialno")
            print("\n您设备的mac地址:")
            self.all_shell(" shell cat /sys/class/net/wlan0/address")
            print("\n您设备的内存信息：")
            self.all_shell(" shell cat /proc/meminfo")
            print("\n您设备的储存信息：")
            self.all_shell(" shell df")
            print("\n您设备的内部存储信息：")
            self.all_shell(" shell df /data")
            print("\n您设备sdcard存储信息：")
            self.all_shell(" shell df /storage/sdcard")
            print("\n您设备的分辨率：")
            self.all_shell(" shell wm size")
            print("\n您设备的DPI数值"+'\n注：Physical density为您所连接的设备的原始DPI大小；Override density为您所连接的设备现在的DPI大小。')
            self.all_shell(" shell wm density")
            print("\n")
            print('\033[0m')
            input("以上为您所连接的设备的信息，回车以退出……")
            return
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面键入“9”选择您要调试的设备后再试！"+'\033[0m')
            return
            
        
    
    def 断开无线调试(self):
        os.system("cls")
        af = input('\033[1;31m'+"确定断开所有已连接的无线连接？输入0返回主界面："+'\033[0m')
        if af == '0':
            return
        else:
            os.system("cls")
            os.system("adb disconnect")
            input("已断开，回车以返回主界面")
            return
    
    def 选择设备(self):
        while True:
            os.system("cls")
            print("您已连接的设备↓")
            idx = self.deviceid()
            for index,item in enumerate(idx):
                print(index+1 ,item)
            num = int(input("请键入对应数字以选择设备："))
            try:
                global choose
                idc = self.deviceid()
                choose = str(idc[num-1])
                os.system('cls')
                ad = input("您已选择"+'\033[4;33m'+choose+'\033[0m'+"作为调试设备"+"，回车以返回主界面：")
                return choose
            except Exception:
                input("请键入正确的数字，回车以返重试：")
                
    
    def 激活(self):
        try:
            while True:
                os.system("cls")
                print("本功能可快速激活您设备上的授权应用（如Shizuku、黑阀等）\n")
                print("1、激活黑阀")
                print("2、激活Shizuku")
                print("3、激活App OpsX")
                print("4、激活炼妖壶(设备管理员)")
                print("5、激活冰箱(设备管理员)")
                print("6、激活gesture的增强模式")
                print("7、激活小黑屋")
                ab = input("键入选项回车以一键激活,输入0以返回主界面:")
                if ab == '0':
                    return
                elif ab == '1':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell sh /storage/emulated/0/Android/data/me.piebridge.brevent/brevent.sh")#V2.4.1
                    self.all_shell(" -d shell sh /storage/emulated/0/Android/data/me.piebridge.brevent/brevent.sh")#V3.6.7.1
                elif ab == '2':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh")
                elif ab == '3':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell sh /storage/emulated/0/Android/data/com.zzzmode.appopsx/opsx.sh")
                elif ab == '4':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell dpm set-device-owner com.oasisfeng.island/.IslandDeviceAdminReceiver")
                elif ab == '5':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell dpm set-device-owner com.catchingnow.icebox/.receiverDPMReceiver")
                elif ab == '6':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell sh /storage/emulated/0/Android/data/com.omarea/cache/up.sh")
                elif ab == '7':
                    os.system('cls')
                    print("命令执行中...")
                    self.all_shell(" shell dpm set-device-owner web1n.stopapp/.receiver.AdminReceiver")
                else:
                    os.system('cls')
                    input("请输入正确的数字，回车以重试：")
                    pass
                os.system('cls')
                input("执行成功，回车以返回激活选择界面：")
        except Exception:
            os.system("cls")
            input('\033[1;31m'+"您貌似未选择您要调试的设备，回车返回主界面键入“9”选择您要调试的设备后再试！"+'\033[0m')
        return
    
    def 关于(self):
        os.system('cls')
        print('\033[5;32;40m' + "ADB快捷工具箱 版本：0.4 作者：Honey White Cloud（3303599383）" + '\033[0m')
        print('开发语言：Python')
        print('GUI：无（控制台）')
        print('本工具箱遵循GPL-3.0 License开源协议，项目地址："https://github.com/HoneyWhiteCloud/ADB-Tool-Box"（如github打开慢可使用："https://hub.fastgit.org/HoneyWhiteCloud/ADB-Tool-Box")')
        print('作者QQ：3303599383\n手表：3259992801\n欢迎向我吐槽和反馈问题')
        print('宗旨：更快、更便捷、更简约')
        input('\n回车以返回主界面：')

if __name__ == '__main__':
    AdbTools()
    pass
        

