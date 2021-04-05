import os
import numpy as np

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

def srt_file_process():
    path = "./assets/files/jojo.txt"
    newFile = open("/assets/files/newFile.txt", 'w')

    with open(path,'r',encoding='utf-8') as fc:
        for line in fc.readlines()[2::4]:
            newFile.write(line)
    newFile.close()

def files_rename():
    data = get_coords_from_csvdata("Ag/data_files/GNI-data")
    dataArray = np.array(data)
    row = dataArray.shape[0]
    titles = dataArray[1:row, 1]
    path = "./Ag/raster_images/GNI_icon/"
    file_names = os.listdir(path)
    for file_name,title in zip(file_names, titles): 
        #设置旧文件名（就是路径+文件名）
        # os.sep添加系统分隔符
        old_name=path+file_name 
        #设置新文件名
        new_name=path+title+'.png'
        if os.path.exists(new_name):
            os.remove(new_name)
        #用os模块中的rename方法对文件改名
        print(old_name, new_name)
        os.rename(old_name, new_name) 

if __name__ == '__main__':
    files_rename()