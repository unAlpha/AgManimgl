# <code># -- coding:UTF-8 --<code>
# 把srt字幕处理成无时间的txt
# 单文件处理
# path = "./assets/files/jojo.txt"
# newFile = open("./assets/files/newFile.txt", 'w')

# with open(path,'r',encoding='utf-8') as fc:
#     for line in fc.readlines()[2::4]:
#         newFile.write(line)
# newFile.close()


# 把srt字幕处理成无时间的txt
# 文件夹处理
# <code># -- coding:UTF-8 --<code>
import os
import io

file_path = '/Users/pengyinzhong/Downloads/2月份/GPT/字幕/mp3/'
files_names = os.listdir(file_path)
import sys  
# reload(sys)  
# sys.setdefaultencoding('utf-8')
for files_name in files_names:
    if files_name.endswith(".txt"):
        path = os.path.join(file_path, files_name)
        newpath = os.path.join(
            file_path,
            files_name.split(".")[0]+'_lan.txt')
        newFile = open(newpath, 'w')
        print(path)
        print(newFile)
        with io.open(path,'r',encoding='utf-8') as fc:
            for line in fc.readlines()[2::4]:
                newFile.write(line)
        newFile.close()
        
# # 读取文件名中的信息并重名命
# import os
# import re
# file_path = 'Z:/LiFiles/田老师/铃木大提琴封面素材信息/铃木大提琴音频调整版/1、第一册/'
# files_names = os.listdir(file_path)
# filter_num_function = re.compile(r'[第](.*?)[首]', re.S)
# filter_name_function = re.compile(r'[《](.*?)[》]', re.S)
# num =[re.findall(filter_num_function, files_names[i])[0][3:] for i in range(len(files_names))] 
# name =[re.findall(filter_name_function, files_names[i])[0] for i in range(len(files_names))]
# print(num,name)


# # 读取文件名中的信息并重名命
# import os
# import re
# file_path = 'D:\Program Files\Blackmagic Design\DaVinci Resolve\Fusion\Templates\Edit\Transitions\ViccoVlog_Transitions_Full_Pack_v2.0'
# files_names = os.listdir(file_path)
# filter_name_function = re.compile(r'[_](.*?)[.]', re.S)
# for files_name in files_names:
#     name =re.findall(filter_name_function, files_name)[0]
#     os.rename(os.path.join(file_path, files_name), os.path.join(file_path, name+".setting"))
#     print(name)


# # 文件名替换成(读取)文件夹的名字
# import os
# file_path = 'Z:\LiFiles\教学课程\MATHTSING数学\选修1-1\素材\第1章'
# files_names = os.listdir(file_path)
# for files_name in files_names:
#     old_path_name=os.path.join(file_path, files_name)
#     in_files_names = os.listdir(old_path_name)
#     for in_files_name in in_files_names:
#         print(in_files_name)
#         print(os.path.join(old_path_name, in_files_name))
#         print(os.path.join(old_path_name, files_name+"."+in_files_name.split(".")[-1]))
#         os.rename(os.path.join(old_path_name, in_files_name),os.path.join(old_path_name, files_name+"."+in_files_name.split(".")[-1]))
#         print("Rename OK")


# # 替换setting文件中的'MacroOperator'为'GroupOperator'
# import os
# import io
# # mac need use io
# def findAllFile(base, suffix='.setting'):
#     for root, ds, fs in os.walk(base):
#         for f in fs:
#             if f.endswith(suffix):
#                 fullname = os.path.join(root, f)
#                 yield fullname

# def alter(file,old_str,new_str, n=1):
#     file_data = ""
#     with io.open(file, "r", encoding="utf-8") as f:
#         for line in f:
#             if old_str in line:
#                 line = line.replace(old_str,new_str,n)
#             file_data += line
#     with io.open(file,"w",encoding="utf-8") as f:
#         f.write(file_data)  

# def main():
#     base = 'D:\Program Files\Blackmagic Design\DaVinci Resolve\Fusion\Templates\Edit'
#     base = "/Users/pengyinzhong/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Titles/Vicco"
#     for file in findAllFile(base):
#         alter(file, 'MacroOperator', 'GroupOperator')
#         print(file+" Replace OK")
# if __name__ == '__main__':
#     main()
        
        
# # 文件夹名替换
# import os
# file_path = 'E:\Dropbox\manim\AgManim\media\Physics_HL'
# files_names = os.listdir(file_path)
# for files_name in files_names:
#     old_path_name=os.path.join(file_path, files_name)
#     new_path_name = old_path_name.replace("%", "_")
#     os.rename(old_path_name, new_path_name)
#     print("Rename OK")


# '''
# 注意这里是从1开始报数的，因此需要 index == k, 且相等时，删除
# '''
# def josephus(n,k):
#     #n代表总人数，k代表报数的数字
#     List = list(range(0,n))
#     index = 0
#     while len(List)>1:
#         temp = List.pop(0)
#         index += 1
#         if index == k:
#             index = 0
#             print(temp)
#             continue
#         List.append(temp)
#         # print(List)
#     return List

# print(josephus(8,3))

