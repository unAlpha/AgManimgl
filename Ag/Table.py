from manimlib import *

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class Table_mol(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        title = Text("城镇企业职工基本养老保险个人账户养老金计发月数表",font_size=30)
        data = get_coords_from_csvdata(r"/Users/pengyinzhong/Downloads/6月份/养老金/素材/月数表")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        x, y, dx, dy = -column+1, 3, 2.1, 0.45
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i in range(row):
            for j in range(column):
                target_ij = Text(str(dataArray[i,j]))
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.35)
                target_ij.shift(np.array([x+j*dx,y-i*dy,0]))
                dataTxt.add(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                        width=column*dx,
                        height=dy,
                        color=BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.236,
                        stroke_opacity=0
                    ).move_to(target_ij, coor_mask=np.array([0,1,0]))
                dataTxtBackground.add(target_i)
        dataTxt.move_to(target_i,coor_mask=np.array([1,0,0]))
        allGroup = VGroup(
                dataTxtBackground[0].copy(),
                *dataTxtBackground,
                *dataTxt,
            ).scale(0.8).center()
        title.next_to(allGroup,UP)
        self.play(
                FadeIn(title,scale=0.5),
                FadeIn(allGroup[0], scale=0.5),
                FadeIn(dataTxtBackground[0], scale=0.5),
                FadeIn(dataTxt[:column], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,dataTxtBackground[1:],lag_ratio=0.1),
                LaggedStartMap(FadeIn,dataTxt[column:],lag_ratio=0.2),
                run_time=3
            )

        self.wait(1) 

class Table_alluse0(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        title = Text("缴费与领取待遇参照表",font_size=30)
        data = get_coords_from_csvdata(r"/Users/pengyinzhong/Downloads/6月份/养老金/素材/缴费与领取待遇参照表")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        x, y, dx, dy = -column+1, 3, 2.4, 0.45
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i in range(row):
            dyy=1
            for j in range(column):
                target_ij = TexText(str(dataArray[i,j]))
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.35)
                    dyy=dy
                target_ij.shift(np.array([x+j*dx,y-(i-1/2)*dyy,0]))
                dataTxt.add(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                        width=column*dx,
                        height=dyy,
                        color=BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.236,
                        stroke_opacity=0
                    ).move_to(target_ij, coor_mask=np.array([0,1,0]))
                dataTxtBackground.add(target_i)
        dataTxt.move_to(target_i,coor_mask=np.array([1,0,0]))
        allGroup = VGroup(
                dataTxtBackground[0].copy(),
                *dataTxtBackground,
                *dataTxt,
            ).scale(0.8).center()
        title.next_to(allGroup,UP)
        self.play(
                FadeIn(title,scale=0.5),
                FadeIn(allGroup[0], scale=0.5),
                FadeIn(dataTxtBackground[0], scale=0.5),
                FadeIn(dataTxt[:column], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,dataTxtBackground[1:],lag_ratio=0.1),
                LaggedStartMap(FadeIn,dataTxt[column:],lag_ratio=0.2),
                run_time=3
            )

        self.wait(1)  

class Table_alluse1(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        title = Text("爱因斯坦奇迹年",font_size=30)
        data = get_coords_from_csvdata(r"/Users/pengyinzhong/Downloads/6月份/相对论/1/素材/发表日期")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        dx, dy = 2, 0.6
        dx_list = [dx] * column
        dy_list = [dy] * row
        dx_list[0] = 5
        dy_list[0] = 0.8
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i,dyy in zip(range(row),dy_list):
            for j,dxx in zip(range(column),dx_list):
                target_ij = Text(str(dataArray[i,j]))
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.4)
                target_ij.shift(np.array([(j-1/2)*dxx,-(i-1/2)*dyy,0]))
                dataTxt.add(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                        width=sum(dx_list),
                        height=dyy,
                        color=BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.236,
                        stroke_opacity=0
                    ).move_to(target_ij, coor_mask=np.array([0,1,0]))
                dataTxtBackground.add(target_i)
        dataTxt.move_to(target_i,coor_mask=np.array([1,0,0]))
        allGroup = VGroup(
                dataTxtBackground[0].copy(),
                *dataTxtBackground,
                *dataTxt,
            ).scale(0.9).center()
        title.next_to(allGroup,UP)
        self.play(
                FadeIn(title,scale=0.618),
                FadeIn(allGroup[0], scale=0.5),
                FadeIn(dataTxtBackground[0], scale=0.5),
                FadeIn(dataTxt[:column], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,dataTxtBackground[1:],lag_ratio=0.1),
                LaggedStartMap(FadeIn,dataTxt[column:],lag_ratio=0.2),
                run_time=3
            )

        self.wait(1)
    
class Table_alluse2(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        title = Text(
            "不同路面的附着系数",
            font_size=36,
            font ='Source Han Sans CN Regular',
            )
        data = get_coords_from_csvdata(r"Z:\\LiFiles\\2022年\\6月份\\刹车\\素材\附着系数")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        # 统一设置高度
        dx, dy = 2.6, 0.6
        dx_list = [dx] * column
        dy_list = [dy] * row
        # 单独设置高度
        dx_list[0] = 3
        dy_list[0] = 0.8
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i,dyy in zip(range(row),dy_list):
            for j,dxx in zip(range(column),dx_list):
                target_ij = Text(
                    str(dataArray[i,j]),
                    font ='SimSun',
                    )
                if i==0:
                    target_ij.scale(0.6)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.5)
                target_ij.shift(np.array([(j-1/2)*dxx,-(i-1/2)*dyy,0]))
                dataTxt.add(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                        width=sum(dx_list),
                        height=dyy,
                        color=BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.236,
                        stroke_opacity=0
                    ).move_to(target_ij, coor_mask=np.array([0,1,0]))
                dataTxtBackground.add(target_i)
        dataTxt.move_to(target_i,coor_mask=np.array([1,0,0]))
        allGroup = VGroup(
                dataTxtBackground[0].copy(),
                *dataTxtBackground,
                *dataTxt,
            ).scale(0.9).center()
        title.next_to(allGroup,UP)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)        
        self.play(
                FadeIn(title,scale=0.618),
                FadeIn(allGroup[0], scale=0.5),
                FadeIn(dataTxtBackground[0], scale=0.5),
                FadeIn(dataTxt[:column], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,dataTxtBackground[1:],scale=0.96,lag_ratio=0.1),
                LaggedStartMap(FadeIn,dataTxt[column:],scale=0.96,lag_ratio=0.2),
                run_time=3
            )

        self.wait(1)    
 
        
