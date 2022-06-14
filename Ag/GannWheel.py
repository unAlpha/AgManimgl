from manimlib import *
 
class helixMatrix():
    def __init__(self, BeginValu=1, Step=1):
        self.BeginValu=BeginValu
        self.Step = Step

    # 把数字转成坐标
    def Num2XY(self, Nums):
        NumInCycle = 0
        Num = (Nums-self.BeginValu+self.Step)/self.Step
        print(Num)
        if Num == 1:
            raise Exception("Num2XY目标循环已经到了矩阵基数值……")
        if Num <= 0:
            raise Exception("矩阵基数或步长设置错误……")
        i=1
        while not NumInCycle:
            if Num>(2*i-1)**2 and Num<=(2*i+1)**2:
                NumInCycle = i
                break
            i+=1

        NsqareNum = 2*NumInCycle+1

        if Num > (2*NumInCycle-1)**2 + NsqareNum*0 and Num < (2*NumInCycle-1)**2+NsqareNum*1-0:
            x = -NumInCycle
            y = Num - (2*NumInCycle-1)**2 - NsqareNum*0 -NumInCycle + 0
        
        if Num >= (2*NumInCycle-1)**2 + NsqareNum*1  and Num < (2*NumInCycle-1)**2+NsqareNum*2-1:
            x = Num - (2*NumInCycle-1)**2 - NsqareNum*1 -NumInCycle + 1
            y = NumInCycle

        if Num >= (2*NumInCycle-1)**2 + NsqareNum*2-1 and Num < (2*NumInCycle-1)**2+NsqareNum*3-2:
            x = NumInCycle
            y = - Num + (2*NumInCycle-1)**2 + NsqareNum*2 + NumInCycle - 2

        if Num >= (2*NumInCycle-1)**2 + NsqareNum*3-2  and Num < (2*NumInCycle-1)**2+NsqareNum*4-3:
            x = - Num + (2*NumInCycle-1)**2 + NsqareNum*3 + NumInCycle - 3
            y = - NumInCycle
        return (x,y)

    # 把坐标转成数字    
    def XY2Num(self, x, y):
        if abs(y)>=abs(x):
            NumInCycle = abs(y)
            NsqareNum = (2*NumInCycle+1)
            if y < 0:
                Num = -x + (2*NumInCycle-1)**2 + NsqareNum*3 + NumInCycle - 3
            else:
                Num = x + (2*NumInCycle-1)**2 + NsqareNum*1 + NumInCycle - 1
        else:
            NumInCycle = abs(x)
            NsqareNum = 2*NumInCycle+1
            if x < 0:
                Num = y + (2*NumInCycle-1)**2 + NsqareNum*0 + NumInCycle + 0
            else:
                Num = -y + (2*NumInCycle-1)**2 + NsqareNum*2 + NumInCycle -2
        if Num == 1:
            raise Exception("XY2Num目标循环已经到了矩阵基数值……")
        return Num*self.Step-self.Step+self.BeginValu

    # 90度转角数
    def Num90(self, Num, CW):
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        if abs(x) == abs(y):
            raise Exception("值位于角线上，无90角转值 ……")
        if CW == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(y,x)
            if abs(y)>abs(x):
                return self.XY2Num(-y,-x)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(y-1,x+1)
        if CW == 1:
            if abs(x)>abs(y):
                return self.XY2Num(-y,-x)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(y,x)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(y-1,x+1)

    # 180度转角数
    def Num180(self, Num, CW):
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)

        if abs(x) == abs(y):
            raise Exception("值位于角线上，无180角转值 ……")

        if CW == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
        if CW == 1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1) 

    # 风车位的角线数
    def JiaoXian(self, Num, CW):
        # 仅配合风车位使用
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        # print((x,y))
        if CW == -1:
            if x>=0 and y>=0:
                if x==y:
                    return self.XY2Num(-x+1,-y+1)
                return self.XY2Num(-y,-x)
            if x<=0 and y>=0:
                return self.XY2Num(y-1,x+1)
            if x<=0 and y<=0:
                if abs(x)>abs(y):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x>=0 and y<=0:
                return self.XY2Num(y,x)
            
        if CW == 1:
            if x>=0 and y>=0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x<=0 and y>=0:
                return self.XY2Num(y,x)
            if x<=0 and y<=0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y+1,-x+1)            
                else:  
                    return self.XY2Num(-y,-x)
            if x>=0 and y<=0:
                return self.XY2Num(y-1,x+1)

    # 过滤相连的目标数
    def FilterNumbers(self, num, CW, dnum=2):
        if not isinstance(num,list):
            return Exception("需要给个list……")
        if CW == 1:
            verse = False
        else:
            verse = True
        numSort = sorted(num, reverse = verse)
        delnumSort = []
        for i in range(len(numSort)):
            if i>0:
                if abs(numSort[i-1]-numSort[i]) <= dnum:
                    delnumSort.append(numSort[i])
        for delnum in delnumSort:
            numSort.remove(delnum)
        # print(delnumSort)
        return numSort
    
    # 风车位推图
    def Windmill(self, Num, CW, n):
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        if n<1:
            raise Exception("请输入要求的个数")
        (x,y) = self.Num2XY(Num) 
        WindmillTaget = []
        if abs(x)>2*abs(y) or abs(y)>2*abs(x):
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.Num180(WindmillTaget[i-1],CW))
                else:
                    WindmillTaget.append(self.Num180(Num,CW)) 
            return WindmillTaget
        else:
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.JiaoXian(WindmillTaget[i-1],CW))
                else:
                    WindmillTaget.append(self.JiaoXian(Num,CW)) 
            return WindmillTaget

    # Constellate推图
    def Constellate(self, Num, CW, N, dnum=2):
        if N<0:
            raise Exception("请输入大于1的段数")
        if self.BeginValu!=1:
            raise Exception("请使用基数1")
        num11 = self.Num90(Num,CW)
        num21 = self.Num180(Num,CW)
        num22 = self.Num90(num11,CW)
        num31 = self.Num180(num11,CW)
        num32 = self.Num90(num21,CW)
        num33 = self.Num90(num22,CW)       
        num1 = [num11]
        num2 = self.FilterNumbers([num21,num22],CW,dnum) 
        num3 = self.FilterNumbers([num31,num32,num33],CW,dnum) 
        num = [num1,num2,num3]
        if N>3:
            for i in range(3+1,N+1):
                newlist = []
                for ber1 in num[i-2]:
                    newlist.append(self.Num90(ber1,CW))
                for ber2 in num[i-3]:
                    newlist.append(self.Num180(ber2,CW))
                num.append(self.FilterNumbers(newlist,CW,dnum))
        return num[:N]

    # 同位阶
    def Apposition(self, Num, CW):
        n1 = self.Num180(Num,CW)
        n2 = self.Num90(n1,-CW)
        n3 = self.Num90(n2,-CW)
        
        m1 = self.Num90(Num,CW)
        m2 = self.Num90(m1,CW)
        m3 = self.Num180(m2,-CW)

        if n3 == m3:
            return n3
        else:
            return "无同位阶"

    # 四角推图
    def FourCorners(self, Num, CW, N):
        if N<0:
            raise Exception("请输入大于1的段数")
        num11 = self.Num90(Num,CW)
        num12 = self.Num180(num11,-CW)
        num = [[num11,num12]]
        if N>1:
            for i in range(1,N):
                num90 = self.Num90(num[i-1][0],CW)
                num180 = self.Num180(num90,-CW)
                num.append([num90,num180])
        return num[:N]

    # 夹角推图
    # 当冲推回调，加减码使用
    def Angle(self, num1, num2, step, n=6, dnum=2):
        # n为对比的个数
        if num1==num2:
            return "两数相等无夹角"
        else:
            nummax = max([num1,num2])
            nummin = min([num1,num2])
        self.BeginValu = nummax
        self.Step = -abs(step)
        num1Windmill = self.Windmill(nummin,1,n)
        self.BeginValu = nummin
        self.Step = abs(step)
        num2Windmill = self.Windmill(nummax,-1,n)
        # 筛选的数与方向无关
        print(num1Windmill)
        print(num2Windmill)
        numSort = sorted(self.FilterNumbers(num1Windmill,1,dnum)\
            +self.FilterNumbers(num2Windmill,1,dnum))
        print(numSort)
        delnumSort = []
        for i in range(len(numSort)):
            if i>0:
                if abs(numSort[i-1]-numSort[i]) > dnum:
                    delnumSort.append(numSort[i])
        delnumSort.append(numSort[0])
        # print(delnumSort)
        for delnum in delnumSort:
            numSort.remove(delnum)
        return numSort

    # 合并目标价
    def Merge(self, M1, M2, CW, dnum=10):
        print(M1)
        print(M2)
        Mnum = self.traverse(M1)+self.traverse(M2)
        return self.FilterNumbers(Mnum, CW, dnum)
        # if CW == 1:
        #     verse = False
        # else:
        #     verse = True
        # numSort = sorted(
        #     # 1是相连数都取尾数
        #     self.FilterNumbers(Mnum, 1, dnum),
        #     reverse = verse
        #     )
        # return numSort

    # 遍历列表
    def traverse(self, lists, Tnum=[]):
        for i in lists:
            if type(i) != list:
                Tnum.append(i)
            else:
                self.traverse(i)
        return Tnum

class TextAF(Text):
    CONFIG = {
        "font": "Source Han Sans CN",
        "color": BLUE,
        "font_size": 36,
        }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)

class Gann(Scene):
    def construct(self):
        beginNum_Text = TextAF("临时基数")
        cw_Text = TextAF("旋方向")
        
        # 夹角风车位推图
        # # 矩阵步长
        # step = 1
        # # 两个临时基数
        # beginNum1, beginNum2 =1960, 2075
        # # 推断的个数，误差
        # number, dn = 5, 5
        # ANS = helixMatrix().Angle(beginNum1, beginNum2, step=step, n=number, dnum=dn)
        # print("%s %s 夹角位:\n%s"%(beginNum1,beginNum2,ANS))

        # Constellate推图
        # 矩阵基数,矩阵步长
        beginValu,step = 1, 1
        # 临时基数,旋转方向,段数
        beginNum, cw, number =1647, -1, 8
        ANS = helixMatrix(BeginValu=beginValu, Step=step).Constellate(beginNum, CW=cw, N=number)
        print("%s临时基数 %s旋方向 %s段Constellate推图:\n%s"%(beginNum,cw,number,ANS))
        
        beginNum_Num = TextAF(str(beginNum))
        cw_Num = TextAF(str(cw))
        segments_Text = TextAF("Constellate推图")
        segments_Num = TextAF(str(number)+"段")
        Txt = VGroup(
            beginNum_Text,beginNum_Num,
            cw_Text,cw_Num,
            segments_Text,segments_Num,

            )\
                .arrange_in_grid(
                    n_rows=3,
                    n_cols=2,
                    h_buff=-1,
                    aligned_edge=RIGHT,
                    ).next_to(TOP,DOWN)
        self.add(Txt)
        
        ANS_TextVGroup = VGroup()
        for ans in ANS:
            if len(ans)<2:
                tmp_Text = Text(str(int(ans[0])))
            else:
                tmp_Text = VGroup(Text(str(int(ans[0]))),Text(str(int(ans[1])))).arrange(RIGHT,buff=0.5)
            ANS_TextVGroup.add(tmp_Text)
        ANS_TextVGroup.arrange(DOWN,aligned_edge=LEFT).next_to(Txt,DOWN)
        self.add(ANS_TextVGroup)
     
        
        # # 同位阶
        # # # 矩阵基数,矩阵步长
        # beginValu,step = 1, 1
        # # 临时基数,旋转方向
        # beginNum, cw =1678, -1
        # ANS = helixMatrix(BeginValu=beginValu, Step=step).Apposition(beginNum, CW=cw)
        # print("%s的%s旋方向的同位阶:\n%s"%(beginNum,cw,ANS))
        # ANS_TextVGroup = TextAF("%s的%s旋方向的同位阶:\n%s"%(beginNum,cw,ANS))
        # self.add(ANS_TextVGroup)
        
        
        # # 合并两种不同跑图的目标价
        # # 矩阵基数,矩阵步长
        # beginValu1,step1 = 1, 1
        # beginValu2,step2 = 1, 1
        # # 临时基数,旋转方向,段数
        # beginNum1, cw1, number1 =1678, -1, 6
        # beginNum2, cw2, number2 =1644, -1, 6   
        # # 结果排序
        # ansCW = -1
        # print("%s临时基数为 %s旋方向 %s段Constellate推图"%(beginNum1,cw1,number1))
        # print("%s临时基数为 %s旋方向 %s段Constellate推图"%(beginNum2,cw2,number2))
        # ANS = helixMatrix().Merge(
        #             # 大势
        #             helixMatrix(BeginValu=beginValu1, Step=step1)\
        #                 .Constellate(beginNum1, CW=cw1, N=number1),
        #             # 波段
        #             helixMatrix(BeginValu=beginValu2, Step=step2)\
        #                 .Constellate(beginNum2, CW=cw2, N=number2),ansCW
        #         )
        # print("合并结果为:\n%s"%(ANS))
        # ANS_TextVGroup = VGroup()
        # for ans in ANS:
        #     tmp_Text = Text(str(int(ans)))
        #     ANS_TextVGroup.add(tmp_Text)
        # ANS_TextVGroup.arrange(DOWN,aligned_edge=LEFT)
        # self.add(ANS_TextVGroup)
        
        # # 四角推图
        # # 矩阵基数,矩阵步长
        # beginValu,step = 1, 1
        # # 临时基数,旋转方向,段数
        # beginNum, cw, number =1752, 1, 10
        # ANS = helixMatrix(BeginValu=beginValu, Step=step).FourCorners(beginNum, CW=cw, N=number)
        # print("%s临时基数 %s旋方向 %s段四角推图:\n%s"%(beginNum,cw,number,ANS))
        # beginNum_Num = TextAF(str(beginNum))
        # cw_Num = TextAF(str(cw))
        # segments_Text = TextAF("四角推图")
        # segments_Num = TextAF(str(number)+"段")
        # Txt = VGroup(
        #     beginNum_Text,beginNum_Num,
        #     cw_Text,cw_Num,
        #     segments_Text,segments_Num,

        #     )\
        #         .arrange_in_grid(
        #             n_rows=3,
        #             n_cols=2,
        #             h_buff=-1,
        #             aligned_edge=RIGHT,
        #             ).next_to(TOP,DOWN)
        # self.add(Txt)
        
        # ANS_TextVGroup = VGroup()
        # for ans in ANS:
        #     if len(ans)<2:
        #         tmp_Text = Text(str(int(ans[0])))
        #     else:
        #         tmp_Text = VGroup(Text(str(int(ans[0]))),Text(str(int(ans[1])))).arrange(RIGHT,buff=0.5)
        #     ANS_TextVGroup.add(tmp_Text)
        # ANS_TextVGroup.arrange(DOWN,aligned_edge=LEFT).next_to(Txt,DOWN)
        # self.add(ANS_TextVGroup)


        # 风车位推图
        # # 矩阵基数,矩阵步长
        # beginValu,step = 1863, 1
        # # 临时基数,旋转方向,风车数
        # beginNum, cw, number =1907, 1, 9
        # ANS = helixMatrix(BeginValu=beginValu, Step=step).Windmill(beginNum, CW=cw, n=number)
        # print("%s临时基数 %s旋方向 %s位风车推图:\n%s"%(beginNum,cw,number,ANS))
