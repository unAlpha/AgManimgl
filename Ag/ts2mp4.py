# -*- coding: UTF-8 -*-
import os

file_path = r"E:\直播录屏\tstomp4"
files_names = os.listdir(file_path)
for files_name in files_names:
    if ".ts" in files_name:
        the_file = os.path.join(file_path, files_name)
        new_file = the_file.replace(" ", "_")
        os.rename(the_file, new_file)
        print(new_file)
        name = new_file.split(".")[0]
        if os.path.exists(name + ".mp4"):
            continue
        order = f"ffmpeg -i {name}.ts -c:v libx264 {name}.mp4"
        print(order)
        os.system(order)
        print("gif generated OK")

# from pydub import AudioSegment
# import os

# AudioSegment.converter = "D:\\ffmpeg\\bin\\ffmpeg.exe"

# file_path = r"E:\tmp\通话录音转为文字"
# files_names = os.listdir(file_path)
# for files_name in files_names:
#     awb_file = os.path.join(file_path, files_name)

#     # 将AWB文件转换为AudioSegment对象
#     print(awb_file)
#     audio = AudioSegment.from_file(awb_file)

#     # 设置输出文件路径
#     mp3_file = awb_file.split('.')[0]+".mp3"
#     if os.path.exists(mp3_file.encode()):
#         continue

#     # 导出为MP3格式
#     audio.export(mp3_file, format="mp3")

#     # 确认输出文件存在
#     if os.path.isfile(mp3_file):
#         print("文件已成功转换为MP3格式！")
#     else:
#         print("无法转换文件为MP3格式。")
