# 重复文件删除
import os
import hashlib
from moviepy.editor import VideoFileClip
from pathlib import Path #用于获取当前目录并遍历路径下所有文件与文件夹
from filecmp import cmp  #cmd（）用于文件比较
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

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

def video_duration(filename):
    clip = VideoFileClip(filename)
    t = float(clip.duration)
    clip.close()
    return t

folder = Path(r"C:\Users\ag_zh\Downloads\我创素材") 
# result = sorted(folder.iterdir())
result = list(folder.glob('*'))

#创建result列表，并将每个文件作为元素存放在列表内。
#如只需要删除某种特定文件，比如.xlsx文件，则只需要将glob内的 * 改为 *.xlsx
files = []
for i in result:  #判断是否为文件，如指定了特定文件，这一步可以忽略
    if i.is_file():
        files.append(i)
for count,file_x in enumerate(files): 
    if not file_x.exists():
        continue
    for file_y in files[count+1:]:
        if not file_y.exists():
            continue 
        if similarity(str(file_x),str(file_y))>0.92:
            xt=video_duration(str(file_x))
            yt=video_duration(str(file_y))
            print(f"{count}\n{file_x} {xt}\n{file_y} {yt}")
            if abs(xt-yt)<0.1 and str(file_x.name)[0:3]!="IMG":
            #     # if os.path.getsize(m) == os.path.getsize(n):
            #     # if cmp(m,n):
            #         # if createChecksum(m)==createChecksum(n):
                os.remove(file_y)
                print(f"remove {file_y}, reserve {file_x}")
        else:
            break;
        
print("delet done!")