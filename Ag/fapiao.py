import os
import fitz

root_dir = r'E:\Dropbox\发票\12月份\12月份电子发票'
repeat_dir = r'E:\Dropbox\发票\11月份\11月份电子发票'
 
def fapiao_read(text):
    money = 0
    dollar = ""
    if "￥" in text:
        dollar = "￥"
    elif "¥" in text:
        dollar = "¥"
    for tex in text.split(dollar):
        if '.' in tex.split("\n")[0]:
            money_tmp = tex.split("\n")[0].strip()
            if float(money_tmp)>float(money):
                money = money_tmp
    return money
 
def xingchengdan_read(text):
    money = text.split("合计")[1].split("元")[0].split()[0].strip()
    return money

Repeat_name_list = []
Money_sum = 0
for file in os.listdir(root_dir):
    if file.endswith(".pdf") or file.endswith(".PDF"):
        src = os.path.join(root_dir, file)
        doc = fitz.open(src)  # or fitz.Document(filename)
        page = doc.load_page(0)
        text = page.get_text("text")
        if "￥" in text or "¥" in text:
            money = fapiao_read(text)
            Money_sum+=float(money)
            out_file_name = "电子发票" + money + "元"
        else:
            money = xingchengdan_read(text)
            Money_sum+=float(money)
            out_file_name = "电子发票" + money + "元行程单"
        Repeat_name_list.append(out_file_name)
        if out_file_name in Repeat_name_list:
            repeat_num = Repeat_name_list.count(out_file_name)
            if repeat_num == 1:
                out_file_name = out_file_name
            else:
                out_file_name = out_file_name + "(" + str(repeat_num-1) + ")"
                print(f"有重复命名：{out_file_name}")
        for rpfile in os.listdir(repeat_dir):
            if rpfile == out_file_name+".pdf":
                print(rpfile,"重复")
        dst = os.path.join(root_dir, out_file_name+".pdf")
        doc.close()
        os.rename(src, dst)
        
print(round(Money_sum,2))
