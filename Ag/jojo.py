# <code># -- coding:UTF-8 --<code>
# 把srt字幕处理成无时间的txt
# path = "/Users/pengyinzhong/Downloads/诺贝尔经济_yt.txt"
# newFile = open("/Users/pengyinzhong/Downloads/诺贝尔经济文本.txt", 'w')

# with open(path,'r',encoding='utf-8') as fc:
#     for line in fc.readlines()[2::4]:
#         newFile.write(line)
# newFile.close()

name = "对话栏目"
path = f"/Users/pengyinzhong/Downloads/公益课表格/{name}.txt"
path_ = f"/Users/pengyinzhong/Downloads/公益课表格/{name}_.txt"
newFile = open(path_, 'w')
with open(path,'r',encoding='utf-8') as fc:
    # for line in reversed(fc.readlines()[4::7]):
    for line in fc.readlines()[4::7]:
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
# file_path = '/Volumes/files/LiFiles/教学课程/MATHTSING数学/必修4/必修四素材/第3章'
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

# import os
# import hashlib
# from os.path import getsize
 
# class ClearRepeat(object):
#     def __init__(self):
#         self.file_path = None
#         self.file_collection = None
#         self.file_origin = {}
#         self.file_repeat = {}
 
#     def getSource(self,file_path):
#         try:
#             if os.path.exists(file_path):
#                 self.file_path = file_path
#                 self.file_collection = []
#                 for dirpath,dirnames,filenames in os.walk(self.file_path):
#                     for file in filenames:
#                         fullpath = os.path.join(dirpath,file)
#                         self.file_collection.append(fullpath)
#                     print('File Collection Success.Total File:%d\r'%len(self.file_collection),end='')
#             print('\n')
#         except Exception as error:
#             self.file_path = None
#             print(error)
 
#     def findRepeat(self):
#         if self.file_path != None and self.file_collection != []:
#             file_count=0
#             for file in self.file_collection:
#                 try:
#                     compound_key = (getsize(file),self.createChecksum(file))
#                     if compound_key in self.file_origin:
#                         print("\nDelete Repete File %s"%file)
#                         os.remove(file)
#                     else:
#                         self.file_origin[compound_key] = file
#                 except Exception as error:
#                     print(error)
#                 file_count+=1
#                 print("Check File Count:%d\r"%file_count,end='')
 
#             print("\nDelete Repeat File Success!")
#         else:
#             print("\nPlease Check File Path Is Correctly!")
 
#     def createChecksum(self,path):
#         fp = open(path,encoding='gb18030', errors='ignore')
#         checksum = hashlib.md5()
#         while True:
#             buffer = fp.read(8192)
#             if not buffer: break
#             checksum.update(buffer.encode('utf-16'))
#         fp.close()
#         checksum = checksum.digest()
#         return checksum

# def CEF(dir):
#     dir_list = []
#     for root,dirs,files in os.walk(dir):
#         dir_list.append(root)
#     for root in dir_list[::-1]:
#         if not os.listdir(root):
#             os.rmdir(root)
#     print("Rmdir OK")
 

# if __name__ == '__main__':
#     file_path = "Z:\\Drive\\彭导Video\\创意点"
#     obj_clear = ClearRepeat()
#     obj_clear.getSource(file_path)
#     obj_clear.findRepeat()
#     CEF(file_path)


