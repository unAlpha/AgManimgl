# -*- coding: UTF-8 -*-
import os
file_path = "D:\迅雷下载"
files_names = os.listdir(file_path)
for files_name in files_names:
    if ".ts" in files_name: 
        the_file=os.path.join(file_path, files_name) 
        new_file=the_file.replace(" ", "_")
        os.rename(the_file,new_file)
        print(new_file)
        name = new_file.split('.')[0]
        if os.path.exists(name+".mp4"):
            continue
        order = f"ffmpeg -i {name}.ts -c:v libx264 {name}.mp4"
        print(order)
        os.system(order)
        print("gif generated OK")