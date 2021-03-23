path = "./assets/files/jojo.txt"
newFile = open("/assets/files/newFile.txt", 'w')

with open(path,'r',encoding='utf-8') as fc:
    for line in fc.readlines()[2::4]:
        newFile.write(line)
newFile.close()