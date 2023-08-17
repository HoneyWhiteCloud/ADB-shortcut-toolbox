import os

from Title import TitleTrue


def 关于(version):
    os.system('cls')
    TitleTrue()
    print('\033[5;32;40m' + "AST adb快捷工具箱 版本："+version+" CTS云顶工作室 出品(1020918195)" + '\033[0m')
    print('\033[1;32m')
    print('开发语言：Python')
    print('GUI：无（控制台）')
    print("本工具箱永久免费，不存在任何收费功能，如任何人倒卖本软件，请给予差评并举报！")
    print("本工具箱只为快速调试设备，仅提供基本ADB功能，不支持高级功能（如文件管理等），后续可能会改善，请多多包涵~")
    print('本工具箱遵循GPL-3.0 License开源协议，项目地址："https://github.com/HoneyWhiteCloud/ADB-Tool-Box"')
    print('开发者QQ：3303599383\n欢迎向我吐槽和反馈问题,也可进群(1020918195)交流讨论!')
    print()
    print('本工具箱初衷意在为各位adb爱好者提供快捷、方便的调试功能，工具箱并不完美，存在着许多隐藏的bugs，如果您在使用过程中遇到了报错(首行为："Traceback (most recent call last)")，还希望您能截屏报错信息，并反馈给我，我会非常感激您贡献的bug!')
    print('\033[0m')
    input('\n回车以返回主界面：')