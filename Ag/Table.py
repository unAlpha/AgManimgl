from manimlib import *

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class Table_mol0(Scene):
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

class Table_mol1(Scene):
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

# 有替换部分的表格
class Table1(Scene):
    def construct(self):
        data = get_coords_from_csvdata(r"Ag\data_files\P2")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        print(row)
        column = dataArray.shape[1]
        print(column)
        # dx,dy 表格的列宽
        dx, dy = 2.618, 0.8
        dataTxt = VGroup()
        dataTxtBackground0 = VGroup()
        dataTxtBackground1 = VGroup()
        dataTxtBackground2 = VGroup()
        for i in range(row):
            for j in range(column):
                if i == 0:
                    weight = 'BOLD'
                else:
                    weight = 'NORMAL'
                target_ij = Text(
                    str(dataArray[i][j]),
                    font="Source Han Sans CN",
                    weight= weight,
                    font_size = 68,
                    )
                if i==0:
                    target_ij.scale(0.5)
                    # target_ij.set_color(RED)
                else:
                    target_ij.scale(0.35)
                target_ij.shift(np.array([j*dx,-i*dy,0]))
                dataTxt.add(target_ij)
            if i==0:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.618,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground0.add(target_i)
                    
            if (i+1)%2:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=WHITE,
                    fill_opacity=0.1,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground1.add(target_i)
            else:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=WHITE,
                    fill_opacity=0.1,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground2.add(target_i)


        pos_and_cont = (
            ([1,1], "\\frac{9}{100} \\times \\frac{99}{100} ", RED),
            ([1,2], "\\frac{91}{100} \\times \\frac{1}{100} ", YELLOW_E),
            ([2,1], "\\frac{9}{100} \\times \\frac{1}{100} ", WHITE),
            ([2,2], "\\frac{91}{100} \\times \\frac{99}{100} ", WHITE),
            )

        for (x,y,z) in pos_and_cont:
            dataTxt[row*x[0]+x[1]].become(
                Tex(
                    y,
                    color = z,
                    font_size = 22,
                    ).move_to(dataTxt[row*x[0]+x[1]])         
                )
        
        allGroup = VGroup(
            dataTxtBackground0,
            VGroup(
                    dataTxtBackground1,
                    dataTxtBackground2),
            dataTxt,
            ).center()
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
                FadeIn(allGroup[0],UP),
                FadeIn(allGroup[1],UP),
                Write(allGroup[2])
            )
        
        self.wait()
        self.play(allGroup.animate.shift(UP*1.5))
        p1_Text = TexText(
                "P(感染|一次阳性)",
                font_size=20,
            )
        p1_Tex = Tex(
            "=\\dfrac{\\dfrac{1}{1000} \\times \\dfrac{99}{100} }{\\dfrac{1}{1000} \\times \\dfrac{99}{100} +\\dfrac{999}{1000} \\times \\dfrac{1}{100} } ",
            font_size=30,
            )
        p1_Group = VGroup(p1_Text,p1_Tex).arrange(RIGHT)
        p1_Group.next_to(allGroup,DOWN)
        self.play(FadeIn(p1_Group,UP))
        self.wait(1)

# 纯表格
class Table2(Scene):
    def construct(self):
        data = get_coords_from_csvdata(r"Ag\data_files\tmpUse")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        print(row)
        column = dataArray.shape[1]
        print(column)
        # dx,dy 表格的列宽
        dx, dy = 2, 0.618
        dataTxt = VGroup()
        dataTxtBackground0 = VGroup()
        dataTxtBackground1 = VGroup()
        dataTxtBackground2 = VGroup()
        for i in range(row):
            for j in range(column):
                if i == 0:
                    weight = 'BOLD'
                else:
                    weight = 'NORMAL'
                target_ij = Text(
                    str(dataArray[i][j]),
                    font="Source Han Sans CN",
                    weight= weight,
                    font_size = 68,
                    )
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(YELLOW)
                else:
                    target_ij.scale(0.386)
                target_ij.shift(np.array([j*dx,-i*dy,0]))
                dataTxt.add(target_ij)
            if i==0:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.618,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground0.add(target_i)
                    
            if (i+1)%2:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=WHITE,
                    fill_opacity=0.1,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground1.add(target_i)
            else:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=WHITE,
                    fill_opacity=0.1,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-((column-1)/2)*dx,0,0]))
                dataTxtBackground2.add(target_i)
  
        allGroup = VGroup(
            dataTxtBackground0,
            VGroup(
                    dataTxtBackground1,
                    dataTxtBackground2),
            dataTxt,
            ).center().scale(0.786)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
                FadeIn(allGroup[0],UP),
                FadeIn(allGroup[1],UP),
                Write(allGroup[2])
            )
        self.wait()

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
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)        
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

class Table():
    CONFIG = {
            "dx": 2.6,
            "dy": 0.6,
        }
    def __init__(self, text, file_path, **kwargs):
        digest_config(self, kwargs)
        self.title = Text(
                text,
                font_size=36,
                font ='Source Han Sans CN Regular',
            )
        data = get_coords_from_csvdata(file_path)
        self.dataArray=np.array(data)
        self.row = self.dataArray.shape[0]
        self.column = self.dataArray.shape[1]
        # 统一设置高度
        self.dx_list = [self.dx] * self.column
        self.dy_list = [self.dy] * self.row
        
    def arrange_table(self):
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i,dyy in zip(range(self.row),self.dy_list):
            for j,dxx in zip(range(self.column),self.dx_list):
                target_ij = Text(
                    str(self.dataArray[i,j]),
                    font ='Source Han Sans CN',
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
                        width=sum(self.dx_list),
                        height=dyy,
                        color=BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.236,
                        stroke_opacity=0
                    ).move_to(target_ij, coor_mask=np.array([0,1,0]))
                dataTxtBackground.add(target_i)
        dataTxt.move_to(dataTxtBackground[-1],coor_mask=np.array([1,0,0]))
        dataTxtBackground[0].set_style(fill_opacity=0.5)
        self.table = VGroup(dataTxtBackground,dataTxt).scale(1).center()
        
        self.tex_column = VGroup()
        for i in range(0,len(dataTxt),self.column):
            self.tex_column.add(dataTxt[i:i+self.column])
            
        self.bg = dataTxtBackground
        
        self.title.next_to(self.table,UP)
        
class Table_use1(Scene):
    def construct(self):
        ble = Table(
                "不同路面的附着系数",
                r"Z:\LiFiles\2022年\6月份\刹车\素材\附着系数"
            )
        ble.dx_list[0] = 3
        ble.dy_list[0] = 0.8
        ble.arrange_table()
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=3
            )

class Table_use2(Scene):
    def construct(self):
        ble = Table(
                "德国与日本队数据对比",
                r"E:\Dropbox\manim\AgManimgl\Ag\data_files\FIFA"
            )
        ble.dx_list[0] = 3
        ble.dy_list[0] = 0.8
        ble.arrange_table()
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)   
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=3
            )
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} Table_use2 -o".format(__file__))