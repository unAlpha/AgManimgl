import os
import time
import shutil
import platform

def main():
    # 创建一个临时文件夹来存储可能的 DaVinci Resolve 文件，并在其中添加一个基于时间戳的子文件夹
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    temp_folder = os.path.expanduser(f'~{os.path.sep}Desktop{os.path.sep}DaVinci_Cleanup_{timestamp}')
    os.makedirs(temp_folder, exist_ok=True)

    # 关键字，用于识别与 DaVinci Resolve 相关的文件或文件夹
    keywords = ['DaVinci', 'Resolve', 'Blackmagic Design']

    # 确定要搜索的路径
    if platform.system() == 'Darwin':
        paths_to_search = [
            os.path.expanduser('~/Library/Application Support/'),
            os.path.expanduser('~/Library/Caches/'),
            os.path.expanduser('~/Library/Preferences/'),
            '/Library/Application Support/Blackmagic Design/DaVinci Resolve/',
            '/Library/Application Support/Blackmagic Design/',
            os.path.expanduser('~/Library/Application Support/Blackmagic Design/'),
            os.path.expanduser('~/Library/Preferences/com.blackmagic-design.DaVinciResolve.plist'),
            os.path.expanduser('~/Library/Saved Application State/com.blackmagic-design.DaVinciResolve.savedState/')
        ]
    elif platform.system() == 'Windows':
        paths_to_search = [
            os.path.expanduser(r'~\AppData\Local'),
            os.path.expanduser(r'~\AppData\Roaming'),
            r'C:\Program Files\Blackmagic Design\DaVinci Resolve',
            r'C:\ProgramData\Blackmagic Design\DaVinci Resolve'
        ]
    else:
        print("不支持的操作系统")
        return

    # 在每个路径中搜索与 DaVinci Resolve 相关的文件
    for path in paths_to_search:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in dirs + files:
                    if any(keyword in name for keyword in keywords):
                        source = os.path.join(root, name)
                        # 保持源文件的原始目录结构
                        relative_path = os.path.relpath(root, start=path)
                        destination_dir = os.path.join(temp_folder, relative_path)
                        os.makedirs(destination_dir, exist_ok=True)
                        destination = os.path.join(destination_dir, name)
                        print(f"移动 {source} 到 {destination}")
                        shutil.move(source, destination)
                        print(f"{source} 已移动")
        else:
            print(f"{path} 不存在")

    print("清理完成，请在桌面的 DaVinci_Cleanup 文件夹中检查文件。")

if __name__ == "__main__":
    if platform.system() == 'Darwin':
        if os.geteuid() != 0: # 检查当前是否为root用户
            os.system("sudo python3 {}".format(__file__))
        else:
            # 调用主要逻辑
            main()
            print("执行脚本完成...")
    elif platform.system() == 'Windows':
        import ctypes
        import sys
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            # 以管理员身份重新运行脚本
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            # 现在，你以管理员身份运行脚本，可以调用你的主函数
            main()
            print("执行脚本完成...")
    else:
        print("不支持的操作系统")
