# 重复文件删除
from pathlib import Path #用于获取当前目录并遍历路径下所有文件与文件夹
from filecmp import cmp  #cmd（）用于文件比较

folder = Path("/Users/pengyinzhong/Downloads/我创素材") 
result = list(folder.glob('*'))  
#创建result列表，并将每个文件作为元素存放在列表内。
#如只需要删除某种特定文件，比如.xlsx文件，则只需要将glob内的 * 改为 *.xlsx
files = []
for i in result:  #判断是否为文件，如指定了特定文件，这一步可以忽略
    if i.is_file():
        files.append(i)
for m in files:  
    for n in files:
        if m != n and m.exists() and n.exists():  #从列表中遍历数据，判断在不是同一个文件的情况
            if cmp(m, n):  
                n.unlink()  #比较两个文件，如匹配，则使用 unlink() 函数删除
                print("delet",n)
print("delet done!")