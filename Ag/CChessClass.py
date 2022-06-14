# -*- coding: utf-8 -*-
import numpy as np

class CCClass():
    def __init__(self):
        # self.direction = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]#八个方向
        self.direction = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
        self.succ = False
        self.m = 5
        self.n = 5 #棋盘维n*m维
        #起始点
        self.x0 = 2
        self.y0 = 3
        print("nxm:%sx%s"%(self.n,self.m))
        print("起始点:(%d,%d)\n"%(self.x0,self.y0))
        self.init()#初始化
        self.play(self.x0,self.y0,1)#开始巡游

        if self.succ:
            print("找到一条巡游路径")
            # self.printP()
        else:
            print("不存在巡游路径")

    def printP(self):
        for i in range(self.n):
            for j in range(self.m):
                print("%d\t"%self.pieces[i][j],end=" ")
            print("")
    
    def init(self):
        '''
        初始化棋盘
        '''
        self.pieces = np.zeros((self.n,self.m))
        self.point = []
        for i in range(self.n):
            for j in range(self.m):
                self.point.append((i,j))
    
    def checkXY(self,x,y):
        '''
        检查点（x,y）是否在棋盘上
        '''
        if x>=0 and x<self.n and y>=0 and y<self.m:
            return True
        return False  
        
    def out1(self,x,y):
        '''
        找出所有方向（包括已经被走过的点）
        '''
        outLine1 = []
        for i in range(len(self.direction)):
            x1 = x+self.direction[i][0]
            y1 = y+self.direction[i][1]
            if self.checkXY(x1,y1):
                outLine1.append((x1,y1))
        return outLine1
    
    def out(self,x,y):
        '''
        找出所有可能走的路径
        '''
        outLine1 = self.out1(x,y)
        outLine = []
        for item in outLine1:
            if self.pieces[item[0]][item[1]]==0:
                outLine.append(item)
        return outLine
    
    def check1(self):
        '''
        剪枝1： 判断初始点各个方向上的点是否已经全走过
        '''
        for i in range(len(self.direction)):
            x1 = self.x0+self.direction[i][0]
            y1 = self.y0+self.direction[i][1]
            if self.checkXY(x1,y1):
                if (x1,y1) in self.point:
                    return True
        return False
    
    def check2(self,x,y):
        '''
        判断剩余点中是否存在孤立点
        '''
        for p in self.point:
            if p[0]==x and p[1]==y:
                continue
            if len(self.out(p[0],p[1]))<1:
                return True
        return True
        
    def play(self,x,y,k):
        self.pieces[x][y] = k
        self.point.remove((x,y))
        if k==self.n*self.m:#找到一条巡游路径
            if (self.x0,self.y0) in self.out1(x,y):#判断能否回到初始点
                self.succ = True
            return
        k += 1
        outLine = self.out(x,y)
        l = len(outLine)
        if l == 0:#该点没有出路回溯
            return
        else:
            outDic=dict()
            for item in outLine:
                outDic[item] = len(self.out(item[0],item[1]))
            #按出路从小到大排序
            outDic = sorted(outDic.items(),key=lambda d:d[1], reverse = False)
            
            for item in outDic:
                if self.check1()==False:
                    continue
                if self.check2(x,y)==False:
                    continue
                self.play(item[0][0],item[0][1],k)
                if self.succ:#如果已经找到则跳出循环
                    break
                self.pieces[item[0][0],item[0][1]]=0#还原步骤，继续搜索
                self.point.append((item[0][0],item[0][1]))
            return #搜索不到则回溯
        
if __name__=="__main__":
    CCClass()