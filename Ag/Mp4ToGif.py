# -*- coding: UTF-8 -*-
import os
file_path = r'Z:\LiFiles\2022年\11月份\踩踏\交付\mp4gif'
files_names = os.listdir(file_path)
for files_name in files_names:
    # if files_name == "Thumbs.db": continue
    if ".mp4" in files_name: 
    # if ".gif" in files_name: 
        the_file=os.path.join(file_path, files_name)
        name = the_file.split('.')[0]
        # gif转mp4
        # order = "ffmpeg -f gif -i %s.gif %s.mp4"%(name,name)
        
        # mp4转gif
        # order = "ffmpeg -i %s.mp4 -an -y -r 20 -vf scale=-1:720 %s.gif"%(name,name)
        order = "ffmpeg -i %s.mp4 -an -y -r 3 -maxrate 0.1K -vf scale=500:-1 %s.gif"%(name,name)
        # # 压缩视频
        # order = "ffmpeg -i %s.mp4 -vf scale=1280:-1 -c:v libx264 -preset veryslow -crf 24 %s%s.mp4"%(name,name,"low")
        print(order)
        os.system(order)
        print("gif generated OK")

# # 提取图片
# os.system("ffmpeg -i \
#     '/Users/pengyinzhong/科普/李永乐/科普视频-loc/看不懂的数字/交付/mp4togif/mp4/其他例子.mp4'\
#     -r 3 \
#     /Users/pengyinzhong/科普/李永乐/科普视频-loc/看不懂的数字/交付/mp4togif/单张图/image-%3d.jpg"
# )

# #裁切视频并转成gif
# import os
# file_path = 'Z:/LiFiles/2021年/11月份/约瑟夫环/素材/gif'
# files_names = os.listdir(file_path)
# for files_name in files_names:
#     # if files_name == "Thumbs.db": continue
#     if ".mp4" in files_name: 
#         the_file=os.path.join(file_path, files_name)
#         name = the_file.split('.')[0]
#         Resolution = 720
#         Width = 300
#         Height = 300
#         x = (Resolution*1920/1080-Width)/2
#         y = (Resolution-Height)/2
#         order = "ffmpeg -i %s.mp4 -y -r 10 -vf scale=-1:%s,crop=%s:%s:%s:%s %s.gif"%(name,Resolution,Width,Height,x,y,name)
#         print(order)
#         os.system(order)
#         print("gif generated OK")
