import os
import shutil
from re import M, compile
from pathlib import Path
from subprocess import Popen,PIPE

from Path import MainPath, get_desktop
from PathChooser import apk路径
from Title import TitleTrue


def APKmanager(choose):#安装APK文件
    while True:
            os.system("cls")
            print('\033[1;31m'+'#####应用管理界面#####\n'+'\033[0m')
            print('\033[1;32m')
            print("1、安装应用")
            print("2、卸载应用")
            print("3、提取应用")
            print("4、强行停止应用")
            print('\033[0m\n')
            i = input("输入选项前数字以继续，输入0即可返回主界面：")










            if i == '1':
                while True:
                    os.system("cls")
                    TitleTrue()
                    print('\033[1;31m')
                    print("#####APK安装界面#####\n\n将APK文件拖入进窗口后回车即可安装，输入1可打开文件选择对话框，输入0即可返回主界面！")
                    print('\033[0m'+'\n')
                    ###################### 
                    APK文件路径 = input('\033[1;34m'+"路径："+'\033[0m').strip()#命令行光标
                    ###################### 
                    if APK文件路径 == '0':
                        return
                    elif APK文件路径 == '':
                        pass
                    elif APK文件路径 == '1':
                        APK文件路径 = '"{}"'.format(apk路径())#获取文件选择界面返回的apk文件路径
                        
                        if APK文件路径 == None:#判断路径是否为空
                            continue
                        pass
                        os.system("cls")
                        cmd = Popen('aapt.exe dump badging {} | findstr application-label-zh-CN:'.format(APK文件路径),
                                    shell=True,stdout=PIPE,stderr=PIPE).communicate()[0].decode('utf-8')
                        try:
                            out = cmd.strip().replace("'",'').rsplit(":",2)[1]
                            pass
                        except Exception:
                            cmd = Popen('aapt.exe dump badging {} | findstr application-label:'.format(APK文件路径),
                                        shell=True,stdout=PIPE,stderr=PIPE).communicate()[0].decode('utf-8')
                            try:
                                out = cmd.strip().replace("'",'').rsplit(":",2)[1]
                                pass
                            except Exception:
                                out = ""
                        if out == "":
                            print("应用：{} 安装中，请耐心等待……".format('\033[4;33m'+APK文件路径+'\033[0m'))
                            pass
                        else:
                            print('应用：\033[4;33m[{}]\033[0m{} 安装中，请耐心等待……'.format(out,APK文件路径))
                            pass
                        
                        result = "\n".join([i.decode("utf-8") 
                                            for i in Popen("adb.exe -s {0} install -r {1}".format(choose,APK文件路径),
                                                                             shell=True,stdout=PIPE,stderr=PIPE).communicate()])
                        break
                    else:
                        
                        try:
                            filevalue = os.path.splitext(APK文件路径)[-1]
                        except:
                            pass
                        if ".apk" in filevalue.lower():
                            os.system("cls")
                            pass
                        elif ".1" in filevalue.lower():
                            os.system("cls")
                            print('\033[1;31m'+"您输入的文件是以.1结尾的，如果是从QQ下载的文件可直接回车继续(文件名将会被改为以.apk结尾的文件)，若不是请输入0重试！"+'\033[0m')
                            _inp = input("\n你的选择：")
                            if _inp == "0":
                                continue
                            else:
                                程序原来执行的路径 = os.getcwd()
                                try:
                                    if list(APK文件路径)[0] == '"':
                                        i=list(APK文件路径)
                                        del i[0]
                                        address =os.path.dirname("".join(i))
                                        pass
                                    else:
                                        address = os.path.dirname(APK文件路径)
                                        pass
                                    os.chdir(address)
                                    try:
                                        os.remove("ASTtemp.apk")
                                        pass
                                    except Exception:
                                        pass
                                    os.rename(os.path.splitext('{}.1'.format(os.path.basename(APK文件路径))[0]),
                                              "{}.apk".format(Path(APK文件路径).stem))#虽然这边会把文件命名为xxx.apk.apk但是为了出现一些意外情况就先这样了
                                except Exception as e:
                                    raise e
                                os.chdir(程序原来执行的路径)
                                APK文件路径=os.path.join(address,"ASTtemp.apk")
                            pass
                        else:
                            os.system("cls")
                            print('\033[1;31m'+"您输入的文件不是以.apk为后缀的安卓软件安装包文件，请重试！"+'\033[0m')
                            input("\n回车以重试")
                            continue
                        
                        if " " in APK文件路径:#判断路径中是否有空格，然后判断是否被双引号括起来，如果没有则添加双引号
                            if APK文件路径[0] != '"':
                                APK文件路径 = '"'+APK文件路径
                                pass
                            if APK文件路径[-1] != '"':
                                APK文件路径 = APK文件路径+'"'
                                pass

                        os.system("cls")
                        cmd = Popen('aapt.exe dump badging {} | findstr application-label-zh-CN:'.format(APK文件路径),
                                    shell=True,stdout=PIPE,stderr=PIPE).communicate()[0].decode('utf-8')
                        try:
                            out = cmd.strip().replace("'",'').rsplit(":",2)[1]
                            pass
                        except Exception:
                            cmd = Popen('aapt.exe dump badging {} | findstr application-label:'.format(APK文件路径),
                                        shell=True,stdout=PIPE,stderr=PIPE).communicate()[0].decode('utf-8')
                            try:
                                out = cmd.strip().replace("'",'').rsplit(":",2)[1]
                                pass
                            except Exception:
                                out = ""
                        if out == "":
                            print("应用：{} 安装中，请耐心等待……".format('\033[4;33m'+APK文件路径+'\033[0m'))
                            pass
                        else:
                            print('应用：\033[4;33m[{}]\033[0m{} 安装中，请耐心等待……'.format(out,APK文件路径))
                            pass
                        result = "\n".join([i.decode("utf-8") for i in Popen("adb.exe -s {0} install -r {1}".format(choose,APK文件路径),
                                                                             shell=False,stdout=PIPE,stderr=PIPE).communicate()])
                        break
                    
                while True:
                    if 'SHARED_USER_INCOMPATIBLE' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK文件签名有问题，请换用其他APK文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'OLDER_SDK' in result :
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您系统版本过旧，低于APK兼容最低版本，请换用其他APK文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'NEWER_SDK' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK版本过新，请换用其他APK文件再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INTERNAL_ERROR' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+'安装系统出现故障！'+'\033[0m')
                        print('错误信息：\n'+result)
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'NO_CERTIFICATES' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK没有签名证书，需要对APK签名！或换用其他APK文件后再试!\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'DEFAULT' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+'未知错误！'+'\033[0m')
                        print('错误信息：\n'+result)
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INVALID_APK' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK为无效的安装包,或安装包已损坏！换用其他APK文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INSUFFICIENT_STORAGE' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您的设备没有剩余的储存空间，请先对您的设备进行清理，或删除部分软件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INVALID_INSTALL_LOCATION' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('错误信息：\n'+result)
                        print('\033[1;31m'+"无效的安装位置！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INSTALL_CANCELED_BY_USER' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您的设备系统禁止安装未知来源的应用！"+'\033[0m')
                        print("请在手机上操作，勾选\"系统设置->安全->未知来源\"选项后重试，这个错误常见于小米手机\n")
                        print("如果您是华为手表3（Watch 3）请先将“应用安装器”（包名：com.android.packageinstaller）停用（冻结），停用（冻结）后即可安装APK\n")
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INCONSISTENT_CERTIFICATES' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"安装包签名不一致！换用其他APK文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'MISSING_SHARED_LIBRARY' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您的设备上缺少您欲安装的APK文件的共享库，请换用其他APK文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'CPU_AEI_INCOMPATIBLE' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"用到ShardUserId，但是没有系统签名，或者签名有问题，请更换其他APK安装"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'Success' in result:#安装成功！
                        os.system("cls")
                        print('\033[1;32m'+"APK安装成功！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        if i == '0':
                            return
                        else:
                            pass
                    elif 'Missing APK file' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"工具箱无法在您的设备上找到您要安装的APK文件，请检查您的APK文件路径是否输入正确！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'NO_MATCHING_ABIS' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK它没有您的设备的CPU架构的本地库！请更换其他APK后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'INSTALL_FAILED_UPDATE_INCOMPATIBLE' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK文件与之前设备上的APK签名不一致，请更换其他APK后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'No such file or directory' in result:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print('\033[1;31m'+"您欲安装的APK文件不存在，请检查apk文件后再试！\n"+'\033[0m')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass
                    elif 'Performing Streamed Install' in result and 'Success'  not in result:
                        os.system("cls")
                        print(result)
                        print("\nAPK安装中止！\n")
                        print('\033[1;31m'+"请检查您的设备数据线是否松动！以及您是否已在设备上允许ADB安装应用！或检查您设备是否有足够的存储空间来安装此应用！亦或者是您设备不支持降级安装！\n"+'\033[0m')
                        i1 = input("回车即可重新安装APK文件，拖入其他APK可快速安装，输入1可打开文件选择对话框，输入0返回主界面:")
                        if i1 == "":
                            pass
                        if i1 == '0':
                            return
                        elif '\\' in i1:
                            i = i1
                            pass
                        else:
                            i = APK文件路径
                            pass
                        pass
                    else:
                        os.system("cls")
                        print("APK安装失败！\n")
                        print("未收录的错误：\n")
                        print('\033[1;31m'+result+'\n'+'\033[0m')
                        print('如果您知道这个错误代表着什么，或了解如何解决这个错误，欢迎QQ联系开发者！\n')
                        i= input("输入APK路径并回车即可继续安装APK文件，输入1可打开文件选择对话框，输入0返回主界面:")
                        pass

                    if i == '0':
                        return
                    elif i == '':
                        pass
                    elif i == '1':
                        APK文件路径 = apk路径()

                        os.system("cls")
                        cmd = os.popen('aapt.exe dump badging {} | findstr application-label-zh-CN:'.format(i))
                        try:
                            out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                            pass
                        except Exception:
                            cmd = os.popen('aapt.exe dump badging {} | findstr application-label:'.format(i))
                            try:
                                out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                                pass
                            except Exception:
                                out = ""
                        if out == "":
                            print("应用：{} 安装中，请耐心等待……".format('\033[4;33m'+i+'\033[0m'))
                            pass
                        else:
                            print('应用：\033[4;33m[{}]\033[0m{} 安装中，请耐心等待……'.format(out,APK文件路径))
                            pass
                        result = os.popen("adb.exe -s {} install -r {}".format(choose,i)).read()

                    elif '\\' in i:
                        try:
                            filevalue = os.path.splitext(APK文件路径)[-1]
                        except:
                            pass
                        if ".apk" == filevalue:

                            if " " in APK文件路径:#判断路径中是否有空格，然后判断是否被双引号括起来，如果没有则添加双引号
                                if APK文件路径[0] != '"':
                                    APK文件路径 = '"'+APK文件路径
                                    pass
                                if APK文件路径[-1] != '"':
                                    APK文件路径 = APK文件路径+'"'
                                    pass

                            os.system("cls")
                            cmd = os.popen('aapt.exe dump badging {} | findstr application-label-zh-CN:'.format(i))
                            try:
                                out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                                pass
                            except Exception:
                                cmd = os.popen('aapt.exe dump badging {} | findstr application-label:'.format(i))
                                try:
                                    out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                                    pass
                                except Exception:
                                    out = ""
                            if out == "":
                                print("应用：{} 安装中，请耐心等待……".format('\033[4;33m'+i+'\033[0m'))
                                pass
                            else:
                                print('应用：\033[4;33m[{}]\033[0m{} 安装中，请耐心等待……'.format(out,APK文件路径))
                                pass
                            result = os.popen("adb.exe -s {} install -r {}".format(choose,i)).read()
                        else:
                            os.system("cls")
                            print('\033[1;31m'+"您输入的文件不是APK文件，请重试！"+'\033[0m')
                            input("\n回车以重试")
                            pass
                    else:
                        pass












            #卸载应用
            elif i == '2':
                sucuninstallAPKnumlist = []
                failuninstallAPKnumlist = []
                killpackname = []
                info = []
                suc = 0
                while True:
                    os.system("cls")
                    TitleTrue()
                    print('\033[1;31m'+"本功能可卸载您所调试的设备上所选的第三方软件！\n"+'\033[0m')
                    print("您设备上的所有的第三方软件↓")
                    print('\033[1;32m')
                    if len(info) != 0:
                        for index,i in enumerate(info):
                            lon = len(list(str(len(info)))) - len(list(str(index+1)))
                            print("[{0}] {1}".format(str(index+1)," "*lon)+i)
                            pass
                        pass
                    else:
                        os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                        os.popen("adb.exe -s {} push aapt /data/local/tmp".format(choose)).read()#将aapt传入/data/local/tmp下
                        os.popen("adb.exe -s {} shell chmod 0755 /data/local/tmp/aapt".format(choose)).read()#将aapt提权
                        cmd = 'adb.exe -s {} shell pm list package -3 -f'.format(choose)
                        res = os.popen(cmd).read()
                        info_list = compile(r'(/.*/base\.apk)=(.*)').findall(res, M)

                        for index,item in enumerate(info_list):
                            out = "\n".join([i.decode("utf-8") 
                                             for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label-zh-CN:'.format(choose,item[0]),
                                                                              shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                            if out[-1] == "":
                                out = "\n".join([i.decode("utf-8") 
                                                 for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label:'.format(choose,item[0]),
                                                                                  shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                if out[-1] == "":
                                    out = "空应用名"
                                    pass
                                elif "ERROR" in out[0]:
                                    out = "空应用名"
                                    pass
                                else:
                                    out = out[-1]
                            elif "ERROR" in out[0]:
                                out = "空应用名"
                                pass
                            else:
                                out = out[-1]
                            lon = len(list(str(len(info_list)))) - len(list(str(index+1)))
                            print("[{0}] {1}".format(str(index+1)," "*lon)+"[{0}]：{1}".format(out,item[1]))
                            info.append("[{0}]：{1}".format(out,item[1]))
                            killpackname.append(item[1])
                            pass
                        os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件

                    print('\033[0m')
                    print("输入对应应用前的序号回车即可卸载，数字之间可空格以选择多个应用，输入0以返回主界面")
                    print('\033[0m')
                    put = input("您的选择:")


                    if ' ' in put:
                        os.system("cls")
                        print("命令执行中……请不要断开您的设备！")
                        trueAPKlist = put.split()
                        for i in trueAPKlist:
                            try:
                                i = int(i)
                                pass
                            except Exception:
                                failuninstallAPKnumlist.append(i)
                                continue
                            try:
                                cmd = "adb.exe -s {} uninstall ".format(choose)+killpackname[i-1]
                                os.popen(cmd).read()
                                sucuninstallAPKnumlist.append(i)
                                suc += 1
                            except Exception:
                                failuninstallAPKnumlist.append(i)
                                pass

                        os.system("cls")
                        print("命令执行成功！成功卸载了{}个，共{}个\n".format(suc,len(trueAPKlist)))
                        print("\n成功卸载的应用：")
                        for i in sucuninstallAPKnumlist:
                            print('\033[1;32m'+info[i-1]+'\033[0m')
                            pass
                        print("\n未能成功卸载的：")
                        if len(failuninstallAPKnumlist) != 0:
                            for i in failuninstallAPKnumlist:
                                print('\033[1;31m'+info[i-1]+'\033[0m')
                                pass
                            pass
                        else:
                            print('\033[1;32m'+"都成功卸载了哦！"+'\033[0m')
                        input("\n回车返回主界面……")
                        return
                    if put == '0':
                        return
                    if put == ' ' or put == '':
                        pass
                    else:
                        try:
                            i = int(put)
                            i -= 1
                            pass
                        except Exception:
                            os.system("cls")
                            print("输入有误！\n")
                            input("回车以重试")
                            continue
                        os.system("cls")
                        print("命令执行中……请不要断开您的设备！")
                        try:
                            cmd = "adb.exe -s {} uninstall ".format(choose)+killpackname[i]
                            sucuninstallAPKnumlist.append(i)
                            pass
                        except Exception:
                            os.system("cls")
                            print("输入有误！\n")
                            input("回车以重试")
                            continue
                        os.popen(cmd).read()
                        os.system("cls")
                        print("命令执行成功！\n")
                        print("应用：{}卸载成功！".format('\033[4;33m'+info[int(" ".join('%s' %id for id in sucuninstallAPKnumlist))]+'\033[0m'))
                        input("\n回车返回主界面……")
                        return















            #提取应用
            elif i == "3":
                sucuninstallAPKnumlist = []
                failuninstallAPKnumlist = []
                info = []
                apknamelist = []
                suc = 0
                desktop = ''.join(get_desktop())
                while True:
                    os.system("cls")
                    TitleTrue()
                    print('\033[1;31m'+"本功能提取您设备上所选的软件的APK！\n"+'\033[0m')
                    print("您设备上的所有的第三方软件↓")
                    print('\033[1;32m')
                    if len(info) != 0:
                        for index,i in enumerate(info):
                            lon = len(list(str(len(info)))) - len(list(str(index+1)))
                            print("[{0}] {1}".format(str(index+1)," "*lon)+i)
                            pass
                        pass
                    else:
                        os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                        os.popen("adb.exe -s {} push aapt /data/local/tmp".format(choose)).read()#将aapt传入/data/local/tmp下
                        os.popen("adb.exe -s {} shell chmod 0755 /data/local/tmp/aapt".format(choose)).read()#将aapt提权
                        cmd = 'adb.exe -s {} shell pm list package -3 -f'.format(choose)
                        res = os.popen(cmd).read()
                        info_list = compile(r'(/.*/base\.apk)=(.*)').findall(res, M)
                        for i in info_list:#所有apk路径列表
                            apknamelist.append(i[0])
                            pass
                        
                        for index,item in enumerate(info_list):
                            out = "\n".join([i.decode("utf-8") 
                                             for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label-zh-CN:'.format(choose,item[0]),
                                                                              shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                            if out[-1] == "":
                                out = "\n".join([i.decode("utf-8") 
                                                 for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label:'.format(choose,item[0]),
                                                                                  shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                if out[-1] == "":
                                    out = "空应用名"
                                    pass
                                elif "ERROR" in out[0]:
                                    out = "空应用名"
                                    pass
                                else:
                                    out = out[-1]
                            elif "ERROR" in out[0]:
                                out = "空应用名"
                                pass
                            else:
                                out = out[-1]
                            lon = len(list(str(len(info_list)))) - len(list(str(index+1)))
                            print("[{0}] {1}".format(str(index+1)," "*lon)+"[{0}]：{1}".format(out,item[1]))
                            info.append("[{0}]：{1}".format(out,item[1]))
                            pass
                        os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件


                    print('\033[0m')
                    print("输入对应应用前的序号回车即可提取APK，数字之间可空格以选择多个应用，输入0以返回主界面")
                    print('\033[0m')
                    put = input("您的选择:")
                    if ' ' in put:
                        os.system("cls")
                        print("命令执行中……请不要断开您的设备！")
                        trueAPKlist = put.split()
                        for i in trueAPKlist:
                            try:
                                i = int(i)
                                pass
                            except Exception:
                                failuninstallAPKnumlist.append(i)
                                continue
                            try:
                                cmd = "adb.exe -s {} pull {} {}".format(choose,apknamelist[i-1],MainPath()+"\\res\\base.apk")
                                os.popen(cmd).read()
                                sucuninstallAPKnumlist.append(i)
                                suc += 1
                            except Exception:
                                failuninstallAPKnumlist.append(i)
                                pass

                            path = info[i-1]+".apk"
                            num = 0
                            while True:
                                if os.path.exists(path):
                                    num += 1
                                    path = info[i-1]+"({})".format(str(num+1))+".apk"
                                    pass
                                else:
                                    os.rename("base.apk",path)
                                    try:
                                        os.remove(os.path.join(desktop,path))
                                        pass
                                    except Exception:
                                        pass
                                    shutil.move(path,desktop)
                                    try:
                                        os.remove("base.apk")
                                    except:
                                        pass
                                    break
                                pass

                        os.system("cls")
                        print("命令执行成功！成功提取了{}个，共{}个 (应用APK已保存至桌面)\n".format(suc,len(trueAPKlist)))
                        print("\n成功提取的应用：")
                        for i in sucuninstallAPKnumlist:
                            print('\033[1;32m'+info[i-1]+'\033[0m')
                            pass
                        print("\n未能成功提取的：")
                        if len(failuninstallAPKnumlist) != 0:
                            for i in failuninstallAPKnumlist:
                                print('\033[1;31m'+info[i-1]+'\033[0m')
                                pass
                            pass
                        else:
                            print('\033[1;32m'+"都成功提取了哦！"+'\033[0m')
                        input("\n回车返回主界面……")
                        return
                    if put == '0':
                        return
                    if put == ' ' or put == '':
                        pass
                    else:
                        try:
                            i = int(put)-1
                            pass
                        except Exception:
                            os.system("cls")
                            print("输入有误！\n")
                            input("回车以重试")
                            continue
                        os.system("cls")
                        print("命令执行中……请不要断开您的设备！")
                        try:
                            os.popen("adb.exe -s {0} pull {1} {2}".format(choose,apknamelist[i],desktop+"\\base.apk")).read()
                            sucuninstallAPKnumlist.append(i)
                            pass
                        except Exception:
                            os.system("cls")
                            print("输入有误！\n")
                            input("回车以重试")
                            continue

                        程序原来执行的路径 = os.getcwd()
                        os.chdir(desktop)#切换至桌面
                        path = info[i]+".apk"
                        num = 0
                        while True:
                            if os.path.exists(path):
                                num += 1
                                path = info[i]+"({})".format(str(num+1))+".apk"
                                pass
                            else:
                                os.rename("base.apk",path)
                                try:
                                    os.remove("base.apk")
                                    pass
                                except Exception:
                                    pass
                                break
                            pass
                        os.chdir(程序原来执行的路径)#返回初始目录

                        os.popen(cmd).read()
                        os.system("cls")
                        print("命令执行成功！\n")
                        print("应用：{}提取成功！(应用APK已保存至桌面)".format('\033[4;33m'+info[int(" ".join('%s' %id for id in sucuninstallAPKnumlist))]+'\033[0m'))
                        input("\n回车返回主界面……")
                        return











            elif i == '4':
                os.system("cls")

                print('\033[1;31m'+'#####应用强行停止界面#####\n'+'\033[0m')
                print('\033[1;31m'+'本功能可强行停止您所选设备上的应用，请注意保存您的工作资料！\n'+'\033[0m')
                print('\033[1;32m')
                print("1、手动选择要强行停止的第三方应用")
                print("2、自动强行停止所有第三方应用")
                print("3、自动强行停止正在显示的应用")
                print('\033[0m\n')
                i = input("输入选项前数字以继续，输入0即可返回主界面：")
                if i == '0':
                    return
                elif i == '1':
                    sucuninstallAPKnumlist = []
                    failuninstallAPKnumlist = []
                    killpackname = []
                    info = []
                    suc = 0
                    while True:
                        os.system("cls")
                        print('\033[1;31m'+"本功能可自行强行停止您所调试的设备上所选的第三方软件！\n")
                        print("请注意保存您的工作资料！\n"+'\033[0m')
                        print("您设备上的所有的第三方软件↓")
                        print('\033[1;32m')
                        if len(info) != 0:
                            for index,i in enumerate(info):
                                lon = len(list(str(len(info)))) - len(list(str(index+1)))
                                print("[{0}] {1}".format(str(index+1)," "*lon)+i)
                                pass
                            pass
                        else:
                            os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                            os.popen("adb.exe -s {} push aapt /data/local/tmp".format(choose)).read()#将aapt传入/data/local/tmp下
                            os.popen("adb.exe -s {} shell chmod 0755 /data/local/tmp/aapt".format(choose)).read()#将aapt提权
                            cmd = 'adb.exe -s {} shell pm list package -3 -f'.format(choose)
                            res = os.popen(cmd).read()
                            info_list = compile(r'(/.*/base\.apk)=(.*)').findall(res, M)

                            for index,item in enumerate(info_list):
                                out = "\n".join([i.decode("utf-8") for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label-zh-CN:'.format(choose,item[0]),
                                                                                  shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                if out[-1] == "":
                                    out = "\n".join([i.decode("utf-8") for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label:'.format(choose,item[0]),
                                                                                      shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                    if out[-1] == "":
                                        out = "空应用名"
                                        pass
                                    elif "ERROR" in out[0]:
                                        out = "空应用名"
                                        pass
                                    else:
                                        out = out[-1]
                                elif "ERROR" in out[0]:
                                    out = "空应用名"
                                    pass
                                else:
                                    out = out[-1]
                                lon = len(list(str(len(info_list)))) - len(list(str(index+1)))
                                print("[{0}] {1}".format(str(index+1)," "*lon)+"[{0}]：{1}".format(out,item[1]))
                                info.append("[{0}]：{1}".format(out,item[1]))
                                killpackname.append(item[1])
                                pass
                            os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件

                        print('\033[0m')
                        print("输入对应应用前的序号回车即可强行停止，数字之间可空格以选择多个应用，输入0以返回主界面")
                        print('\033[0m')
                        put = input("您的选择:")
                        if ' ' in put:
                            put1 = put.split()
                            os.system("cls")
                            print("命令执行中……请不要断开您的设备！")
                            for i1 in put1:
                                try:
                                    i = int(i1)-1
                                    pass
                                except Exception:
                                    pass
                                try:
                                    cmd = "adb.exe -s {} shell am force-stop ".format(choose)+killpackname[i]
                                    os.popen(cmd).read()
                                    sucuninstallAPKnumlist.append(i)
                                    suc += 1
                                    pass
                                except Exception:
                                    failuninstallAPKnumlist.append(i)
                                    pass
                            os.system("cls")
                            print("命令执行成功！成功停用了{}个，共{}个\n".format(suc,len(put1)))
                            print("\n成功停用的应用：")
                            for i in sucuninstallAPKnumlist:
                                print('\033[1;32m'+info[i]+'\033[0m')
                                pass
                            print("\n未能成功停用的应用：")
                            if len(failuninstallAPKnumlist) != 0:
                                for i in failuninstallAPKnumlist:
                                    print('\033[1;31m'+info[i]+'\033[0m')
                                    pass
                                pass
                            else:
                                print('\033[1;32m'+"都成功停用了哦！"+'\033[0m')
                            input("\n回车返回主界面……")
                            return
                        if put == '0':
                            return
                        if put == ' ' or put == '':
                            pass
                        else:
                            try:
                                i = int(put)
                                i -= 1
                                pass
                            except Exception:
                                os.system("cls")
                                print('\033[1;31m'+"输入有误！\n"+'\033[0m')
                                input("回车以重试")
                                continue
                            os.system("cls")
                            print("命令执行中……请不要断开您的设备！")
                            try:
                                cmd = "adb.exe -s {} shell am force-stop ".format(choose)+killpackname[i]
                                os.popen(cmd).read()
                                sucuninstallAPKnumlist.append(i)
                                pass
                            except Exception:
                                os.system("cls")
                                print("输入有误！\n")
                                input("回车以重试")
                                continue
                            os.popen(cmd).read()
                            os.system("cls")
                            print("命令执行成功！\n")
                            print("应用：{}停用成功！".format('\033[4;33m'+info[int(" ".join('%s' %id for id in sucuninstallAPKnumlist))]+'\033[0m'))
                            input("\n回车返回主界面……")
                            return

                elif i == '2':
                    info = []
                    killpackname = []
                    while True:
                        os.system("cls")
                        print('\033[1;31m'+"本功能会强行停止您所选的设备上的所有第三方应用程序！\n")
                        print("请注意保存您的工作资料！\n"+'\033[0m')
                        print("如有无关内容出现请回车刷新！")
                        print("您设备上的所有第三方应用程序↓")
                        print('\033[1;32m')
                        if len(info) != 0:
                            for i in info:
                                print(i)
                                pass
                            pass
                        else:
                            os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                            os.popen("adb.exe -s {} push aapt /data/local/tmp".format(choose)).read()#将aapt传入/data/local/tmp下
                            os.popen("adb.exe -s {} shell chmod 0755 /data/local/tmp/aapt".format(choose)).read()#将aapt提权
                            cmd = 'adb.exe -s {} shell pm list package -3 -f'.format(choose)
                            res = os.popen(cmd).read()
                            info_list = compile(r'(/.*/base\.apk)=(.*)').findall(res, M)

                            for index,item in enumerate(info_list):
                                out = "\n".join([i.decode("utf-8") for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label-zh-CN:'.format(choose,item[0]),
                                                                                  shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                if out[-1] == "":
                                    out = "\n".join([i.decode("utf-8") for i in Popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label:'.format(choose,item[0]),
                                                                                      shell=True,stdout=PIPE,stderr=PIPE).communicate()]).strip().replace("'","").rsplit(":",2)
                                    if out[-1] == "":
                                        out = "空应用名"
                                        pass
                                    elif "ERROR" in out[0]:
                                        out = "空应用名"
                                        pass
                                    else:
                                        out = out[-1]
                                elif "ERROR" in out[0]:
                                    out = "空应用名"
                                    pass
                                else:
                                    out = out[-1]
                                lon = len(list(str(len(info_list)))) - len(list(str(index+1)))
                                print("[{0}] {1}".format(str(index+1)," "*lon)+"[{0}]：{1}".format(out,item[1]))
                                info.append("[{0}]：{1}".format(out,item[1]))
                                killpackname.append(item[1])
                                pass
                            os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                            
                        print("回车以全部强行停止，输入0以返回主界面")
                        print('\033[0m')
                        put = input("您的选择:")
                        if put == '0':
                            return
                        else:
                            os.system("cls")
                            print("命令执行中……请不要断开您的设备！")
                            for i in killpackname:
                                os.popen("adb.exe -s {} shell am force-stop {}".format(choose,i)).read()
                                pass
                            os.system("cls")
                            print("命令执行成功！\n")
                            input("回车返回主界面……")
                            return

                elif i == '3':
                    info = []
                    while True:
                        os.system("cls")
                        out = os.popen("adb.exe -s {} shell dumpsys window | findstr mCurrentFocus".format(choose)).read()
                        actlist = list(out.replace(' ','').replace('{','').replace('}','').rsplit("/",2)[0])
                        del actlist[0:29]
                        act = ''.join(actlist)
                        cmd = 'adb.exe -s {} shell pm list package -3 -f'.format(choose)
                        res = os.popen(cmd).read()
                        info_list = compile(r'(/.*/base\.apk)=(.*)').findall(res, M)
                        for i in info_list:
                            if act in i[1]:
                                apkpath = i[0]
                                os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                                os.popen("adb.exe -s {} push aapt /data/local/tmp".format(choose)).read()#将aapt传入/data/local/tmp下
                                os.popen("adb.exe -s {} shell chmod 0755 /data/local/tmp/aapt".format(choose)).read()#将aapt提权
                                cmd = os.popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label-zh-CN:'.format(choose,apkpath))
                                try:
                                    out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                                    pass
                                except Exception:
                                    cmd = os.popen('adb.exe -s {} shell /data/local/tmp/aapt d badging {} | findstr application-label:'.format(choose,apkpath))
                                    try:
                                        out = cmd.buffer.read().decode('utf-8').strip().replace("'","").rsplit(":",2)[1]
                                        pass
                                    except Exception:
                                        out = "空应用名"
                                        pass
                                    pass     
                                os.popen("adb.exe -s {} shell rm /data/local/tmp/aapt -f".format(choose)).read()#删除临时文件
                                pass
                            else:
                                out = "空应用名"
                                pass
                        info.append("[{}]:{}".format(out,act))
                        print('\033[1;31m'+"本功能可强行停止您所选的设备上的顶部Activity（正在前台显示的应用）\n"+'\033[0m')
                        print("您设备的顶部Activity为：{}".format(info[0]))
                        inp = input('\033[1;31m'+"回车以强行停止您设备的顶部Activity，输入0以返回主界面："+'\033[0m')
                        if inp == '0':
                            return
                        elif inp == '':
                            os.system("cls")
                            print("命令执行中……请不要断开您的设备！")
                            os.popen("adb.exe -s {} shell am force-stop {}".format(choose,act))
                            os.system("cls")
                            print("命令执行成功！\n")
                            input("回车以返回主界面……")
                            return
                        else:
                            pass
                        pass
                else:
                    pass

            
            elif i == "0":
                return
            else:
                pass
