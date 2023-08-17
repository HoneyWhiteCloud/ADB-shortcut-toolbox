try:
    import win32ui
except:
    import os,sys
    print("正在安装程序所需运行库\n")#仅在直接运行源代码时适用，防止不同小伙伴因为缺少第三方库而发生报错的问题
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pypiwin32")
    input("\n如安装完成，可回车退出后重启程序！")
    sys.exit()
    pass
    
from Path import get_desktop

def apk路径():
    desktoppath = get_desktop()
    lpszFilter = "APK安装包 (*.apk)|*.apk|" \
                "所有文件 (*.*)|*.*|| "
    # 这里的构造方法，对应上面展示的构造方法
    dlg = win32ui.CreateFileDialog(True, "apk", None, 0x04 | 0x02, lpszFilter)  # True表示打开文件对话框
    # 设置打开文件对话框中的初始显示目录
    dlg.SetOFNInitialDir(desktoppath)
    dlg.DoModal()
    # 等待获取用户选择的文件
    filename = dlg.GetPathName()  # 获取选择的文件名称
    # 如果用户点击了取消，则返回的filename为""，而不是None
    if filename == "":
        return None
    else:
        return filename