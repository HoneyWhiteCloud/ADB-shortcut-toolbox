import os

from Cmd import all_shell


def 停用(choose,chooseandinfo):
    os.system("cls")
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
        设备类型 = str(all_shell(choose," -d shell getprop ro.product.model")).strip()
        if 设备类型 != "Mi Watch":
            os.system("cls")
            print('\033[1;31m'+"您所选择调试的的设备不是小米手表，无法使用该功能！"+'\033[0m')
            input("\n回车以返回主界面……")
            return
        else:
            while True:
                冻结应用列表 = ['com.xiaomi.wear.hotwordle','com.android.cts.priv.ctsshim','com.qualcomm.qti.sidekickmetrics','com.qualcomm.qcrilmsgtunnel','com.qualcomm.timeservice','com.google.android.ext.services','com.qualcomm.qti.operationmeasurement','com.xiaomi.wear.fitness','com.iflytek.inputmethod.wear.xiaomi','com.android.providers.calendar','com.android.providers.media','com.xiaomi.wear.watchface.function','com.xiaomi.wear.watchface.art','com.xiaomi.account','com.xiaomi.wear.recorder','com.xiaomi.wear.watchface.animation','com.android.providers.downloads','com.onetrack.watch','com.android.vending','com.google.android.wearable.batteryservices','com.xiaomi.wear.watchface.album','com.xiaomi.wear.watchface.decomposite','com.google.android.marvin.talkback','com.xiaomi.wear.watchface.classic','com.google.android.clockwork.lesetup','com.xiaomi.wear.tutorial','com.xiaomi.wear.deskclock','com.android.statementservice','com.xiaomi.wear.sportlogger','com.xiaomi.wear.compass','com.google.android.clockwork.gestures.tutorial','com.google.android.wearable.overlay.common.baiji','com.xiaomi.wear.weather','com.xiaomi.wear.sound.meter','com.google.android.gsf','com.google.android.theme.baiji.default','com.xiaomi.wear.charging','com.xiaomi.mihome','com.xiaomi.wear.anonymous.xiaoai','com.xiaomi.wear.lpa','com.xiaomi.wear.mqs','com.google.android.wearable.overlay.helium.baiji','com.google.android.inputmethod.pinyin','com.android.cts.ctsshim','com.xiaomi.wear.calculator','com.xiaomi.wear.camera','com.google.android.apps.handwriting.ime','com.android.providers.blockednumber','com.android.providers.userdictionary','com.xiaomi.wear.market','com.google.android.wearable.overlay.home.baiji.tiles','com.xiaomi.wear.setupprovider','com.google.android.wearable.overlay.home.baiji','com.xiaomi.wear.xiaoai','com.android.providers.contacts','com.google.android.wearable.frameworkpackagestubs','com.xiaomi.wear.pressure','com.xiaomi.wear.card']
                保留部分功能 = ['com.xiaomi.wear.hotwordle','com.android.cts.priv.ctsshim','com.qualcomm.qti.sidekickmetrics','com.qualcomm.qcrilmsgtunnel','com.qualcomm.timeservice','com.google.android.ext.services','com.qualcomm.qti.operationmeasurement','com.google.android.ext.services','com.xiaomi.wear.setupprovider','com.onetrack.watch','com.android.vending','com.google.android.wearable.batteryservices','com.google.android.marvin.talkback','com.android.statementservice','com.google.android.clockwork.gestures.tutorial','com.google.android.wearable.overlay.common.baiji','com.google.android.theme.baiji.default','com.xiaomi.mihome','com.xiaomi.wear.mqs','com.google.android.wearable.overlay.helium.baiji','com.google.android.inputmethod.pinyin','com.android.cts.ctsshim','com.xiaomi.wear.camera','com.google.android.apps.handwriting.ime','com.android.providers.userdictionary','com.google.android.wearable.overlay.home.baiji.tiles','com.google.android.wearable.overlay.home.baiji','com.google.android.wearable.frameworkpackagestubs']
                os.system("cls")
                print("小米手表性能增强&恢复模式\n")
                print('\033[1;31m')
                print("请确保您的米表已开启开发者模式——ADB调试,并允许调试！\n")
                print("注意！！！本工具仅限高级玩表人士使用，普通玩家不要轻易尝试！")
                print('本工具会导致手表系统自带表盘全部无法显示（腕间图库等第三方表盘不受影响）\n\n"停用部分功能换取性能"功能会导致任何关于小米的应用全部无法使用（包括但不限于：米家、小米账号、手表应用商店、表盘商店、小爱同学）\n以及所有工具类应用（包括但不限于：海拔气压、天气、计算器、卡与支付、运动模式）\n以及部分系统功能（包括但不限于：谷歌输入法（系统自带）、讯飞输入法（系统自带）、Talkback、充电显示、省电模式')
                print('\n"保留部分常用功能增加性能"保留了日常可能会使用的功能，仅停用部分系统应用！^_^')
                print("\n如果您因使用本工具导致的任何财产损失，请自行承担！本开发者不负任何责任！")
                print('\033[1;32m')
                print("1、停用所有非必须应用换取性能")
                print("2、保留部分常用应用增加性能")
                print("3、恢复原来所有的系统应用"+'\033[0m')
                选择 = input("\n您的选择，输入0以返回主界面：")
                if 选择 == '1':
                    os.system("cls")
                    while True:
                        print("您确定停用您米表上所有非必须应用以增强性能吗？(Y/N)?")
                        选择1 = input("您的选择：")
                        if 选择1 == 'y'or'Y':
                            os.system("cls")
                            print("执行指令中……，请确保您的设备连接良好，不要在命令执行期间断开设备的连接！")
                            for packname in 冻结应用列表:
                                os.popen("adb.exe -s {} shell pm disable-user {}".format(choose,packname)).read()
                                pass
                            for packname1 in 冻结应用列表:
                                os.popen("adb.exe -s {} shell am force-stop {}".format(choose,packname1)).read()
                                pass
                            os.system("cls")
                            print("命令执行完成！")
                            input("\n回车以退出……")
                            return
                        elif 选择1 == 'n'or'N':
                            return
                        else:
                            pass
                elif 选择 == '2':
                    os.system("cls")
                    while True:
                        print("您确定保留您米表上的部分常用功能增强性能吗？(Y/N)?")
                        选择1 = input("您的选择：")
                        if 选择1 == 'y'or'Y':
                            os.system("cls")
                            print("执行指令中……，请确保您的设备连接良好，不要在命令执行期间断开设备的连接！")
                            for packname in 保留部分功能:
                                os.popen("adb.exe -s {} shell pm disable-user {}".format(choose,packname)).read()
                                pass
                            for packname1 in 保留部分功能:
                                os.popen("adb.exe -s {} shell am force-stop {}".format(choose,packname1)).read()
                                pass
                            os.system("cls")
                            print("命令执行完成！")
                            input("\n回车以退出……")
                            return
                        elif 选择1 == 'n'or'N':
                            return
                        else:
                            pass
                elif 选择 == '3':
                    while True:
                        os.system("cls")
                        print("您确定放弃米表性能换取系统的部分功能吗？(Y/N)?")
                        选择1 = input("您的选择：")
                        if 选择1 == 'y'or'Y':
                            os.system("cls")
                            print("执行指令中……，请确保您的设备连接良好，不要在命令执行期间断开设备的连接！")
                            for packname in 冻结应用列表:
                                os.popen("adb.exe -s {} shell pm enable {}".format(choose,packname)).read()
                                pass
                            os.system("cls")
                            print("命令执行完成！")
                            是否重启 = input("\n回车以重启手表（请注意保存您未完成的工作资料！），输入0以返回主界面……")
                            if 是否重启 == '0':
                                return
                            else:
                                os.system("cls")
                                print("执行指令中……，请确保您的设备连接良好，不要在命令执行期间断开设备的连接！")
                                os.popen("adb.exe -s {} reboot".format(choose)).read()#重启手表
                                print("命令执行完成！")
                                input("\n回车以退出……")
                            return
                        elif 选择1 == 'n'or'N':
                            return
                        else:
                            pass
                elif 选择 == '0':
                    return
                else:
                    pass