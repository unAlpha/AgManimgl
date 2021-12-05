import os
import shutil
import hashlib
import filecmp

def findAllFile(base,flag=0):
    '''
    base 查找的路径
    flag 查找是的文件还是文件夹
    '''
    for root, ds, fs in os.walk(base):
        if flag==0:
            for d in ds:
                fullname = os.path.join(root, d)
                yield fullname 
        if flag==1:
            for f in fs:
                fullname = os.path.join(root, f)
                yield fullname
                
def Merge_dirs(root_src_dir, root_dst_dir):
    '''
    root_src_dir 要合并的文件夹
    root_dst_dir 目标文件夹
    '''
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
    print("Merge",root_src_dir,root_dst_dir)
    
def CEF(dir):
    dir_list = []
    for root,dirs,files in os.walk(dir):
        dir_list.append(root)
    for root in dir_list[::-1]:
        if not os.listdir(root):
            os.rmdir(root)
    print("Rmdir OK")    
                
def main_merge_dirs(file_path):
    files_name = findAllFile(file_path)
    for file_name in files_name:
        if file_name.endswith("_",-2,-1):
            path_file_x = os.path.join(file_path, file_name)
            print("Find",path_file_x)
            path_file = os.path.join(file_path, file_name[:-2])
            if os.path.exists(path_file):
                print("Exist",path_file)
                Merge_dirs(path_file_x, path_file)
    print("merge dirs Done!")
   
def createChecksum(path):
    fp = open(path,encoding='gb18030', errors='ignore')
    checksum = hashlib.md5()
    while True:
        buffer = fp.read(8192)
        if not buffer: break
        checksum.update(buffer.encode('utf-16'))
    fp.close()
    checksum = checksum.digest()
    return checksum
 
def main_merge_fils(file_path):
    files_name = findAllFile(file_path, flag=1)
    for file_name in files_name:
        # print(file_name)
        (filename, extension) = os.path.splitext(file_name)
        # print(filename, extension)
        if filename.endswith("_",-2,-1):
            path_file_x = filename+extension
            path_file = filename[:-2]+extension
            print("Find",path_file_x)
            if os.path.exists(path_file):
                print("Exists!",path_file)
                if os.path.getsize(path_file_x) == os.path.getsize(path_file):
                    # if createChecksum(path_file_x)==createChecksum(path_file):
                    if filecmp.cmp(path_file_x,path_file):
                        os.remove(path_file_x)
                        print("Remove:", path_file_x)
    print("merge fils Done!")

if __name__ == '__main__':
    # file_path = 'Z:\\AliYunSyncFiles'
    # main_merge_dirs(file_path)
    CEF("Z:\\AliYunSyncFiles\\2019年\\12月份\\资料\\莱顿弗罗斯特效应")
    # main_merge_fils(file_path)

