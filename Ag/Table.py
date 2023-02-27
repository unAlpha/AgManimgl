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
    def __init__(
        self, 
        text, 
        file_path, 
        dx=2.6,
        dy=0.6,
        title_font="Source Han Sans CN Regular"
    ):
        self.dx = dx
        self.dy = dy
        self.title_font = title_font
        self.title = Text(
                text,
                font_size=36,
                font = self.title_font,
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
                    font = self.title_font,
                    )
                if i==0:
                    target_ij.scale(0.6)
                    target_ij.set_color(ORANGE)
                else:
                    target_ij.scale(0.5)
                target_ij.shift(np.array([sum(self.dx_list[0:j+1])-dxx/2,-(sum(self.dy_list[0:i+1])-dyy/2),0]))
                dataTxt.add(target_ij)
            if (i+1)%2:
                fop = 0.2;
            else:
                fop = 0.1;
            target_i = Rectangle(
                    width=sum(self.dx_list),
                    height=dyy,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=fop,
                    stroke_opacity=0,
                    # stroke_color=WHITE,
                    # stroke_width=DEFAULT_STROKE_WIDTH/2,
                ).move_to(target_ij, coor_mask=np.array([0,1,0]))
            target_i.next_to(ORIGIN,RIGHT,buff=0,coor_mask=np.array([1,0,0]))
            dataTxtBackground.add(target_i)
        dataTxtBackground[0].set_style(fill_opacity=0.618)
        self.table = VGroup(dataTxtBackground,dataTxt).center()
        
        
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

class Table_use3(Scene):
    def construct(self):
        ble = Table(
                "台湾2020-2021年新冠感染者和死亡人数统计",
                r"Z:\LiFiles\2022年\12月份\抗原检测\素材\台湾2020-2021年新冠感染者和死亡人数统计",
                dx=1.73,
                dy=0.5,
            )
        ble.dx_list[0] = 2
        ble.dy_list[0] = 0.6
        ble.arrange_table()
        ble.table.to_corner(LEFT,buff=LARGE_BUFF)
        ble.title.next_to(ble.table,UP)
        tex = TexText(
                "$$\\text{2020-2021年新冠病毒致死率（台湾）}$$",
                "$$\\frac{838}{14603} \\times 100\\%=5.74\\%$$",
                font ='Source Han Sans CN',
                font_size=36,
            ).arrange(DOWN)
        tex.set_color_by_tex("5.74",RED)
        tex[0].scale(0.8)
        tex.next_to(ble.table,RIGHT,buff=MED_LARGE_BUFF)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                Write(tex),
                run_time=3
            )
        self.wait(2)

class Table_use4(Scene):
    def construct(self):
        ble = Table(
                "台湾2022年新冠病毒感染者和死亡人数统计",
                r"Z:\LiFiles\2022年\12月份\抗原检测\素材\台湾2022年新冠病毒感染者和死亡人数统计",
                dx=1.73,
                dy=0.5,
            )
        ble.dx_list[0] = 2
        ble.dy_list[0] = 0.6
        ble.arrange_table()
        ble.table.to_corner(LEFT,buff=LARGE_BUFF)
        ble.title.next_to(ble.table,UP)
        tex = TexText(
                "$$\\text{2022年新冠病毒致死率（台湾）}$$",
                "$$\\text{截至12月9日}$$",
                "$$\\frac{13786}{8403234} \\times 100\\%=0.16\\%$$",
                "$$\\text{60岁以下致死率}$$",
                "$$\\frac{1296}{7027792} \\times 100\\%=0.018\\%$$",
                font ='Source Han Sans CN',
                font_size=36,
            ).arrange(DOWN)
        tex.set_color_by_tex("0.16",RED)
        tex.set_color_by_tex("0.018",RED)
        tex[0:2].scale(0.9)
        tex[3:].shift(DOWN*0.4)
        
        tex.next_to(ble.table,RIGHT,buff=MED_LARGE_BUFF)
        tex.shift(UP*0.68)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                Write(tex[:3]),
                run_time=3
            )
        self.wait()
        self.play(
                Write(tex[3:]),
                run_time=1
            )
        self.wait()
        self.play(
            FlashAround(ble.tex_column[7]),
            ble.tex_column[7].animate.set_color(YELLOW)
        )
        self.wait()
        self.play(
            FlashAround(ble.tex_column[8]),
            ble.tex_column[8].animate.set_color(YELLOW)
        )
        self.wait()
        self.play(
            FlashAround(ble.tex_column[9]),
            ble.tex_column[9].animate.set_color(YELLOW)
        )
        self.wait()
        self.play(
            FlashAround(ble.tex_column[10]),
            ble.tex_column[10].animate.set_color(YELLOW)
        )
        self.wait(2)

class Table_use5(Scene):
    def construct(self):
        ble = Table(
                "台湾新冠病毒感染者和死亡人数统计",
                r"Z:\LiFiles\2022年\12月份\抗原检测\素材\台湾新冠病毒感染者和死亡人数统计",
                dx=1.73,
                dy=0.5,
            )
        ble.dx_list[0] = 2
        ble.dy_list[0] = 0.6
        ble.arrange_table()
        ble.table.scale(1.26).shift(UP*0.5)
        ble.title.scale(1.3).next_to(ble.table,UP,buff=MED_LARGE_BUFF)
        ble.bg[2].stretch_to_fit_height(1.18, about_point = ble.bg[2].get_top())
        ble.bg[-1].become(VMobject())
        for txt in ble.tex_column[3]:
            txt.scale(0.8).shift(0.1*UP)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=2
            )
        
        self.wait()
        for i in range(1,4):
            self.play(
                FlashAround(ble.tex_column[i]),
                ble.tex_column[i].animate.set_color(YELLOW)
            )
            self.wait()
        self.wait(2)

class Table_use6(Scene):
    def construct(self):
        ble = Table(
                "台湾2022年新冠病毒感染者和死亡人数统计",
                r"Z:\LiFiles\2022年\12月份\抗原检测\素材\台湾2022年新冠病毒感染者和死亡人数统计合并",
                dx=1.73,
                dy=0.5,
            )
        ble.dx_list[0] = 2
        ble.dy_list[0] = 0.6
        ble.arrange_table()
        ble.table.scale(1.26).shift(UP*0.1)
        ble.title.scale(1.3).next_to(ble.table,UP,buff=MED_LARGE_BUFF)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=1
            )
        self.wait()
        for i in range(2,6):
            self.play(
                FlashAround(ble.tex_column[i]),
                ble.tex_column[i].animate.set_color(YELLOW)
            )
            self.wait()
        self.wait(2)

class Fifa1(Scene):
    t1 = "世界杯决赛某博彩公司开出的赔率和销售彩票金额比例"
    path = r"Z:\LiFiles\2022年\12月份\足彩\素材\抽水"
    ptxt = [
        "总销售额：$34.6+32.47+35.59=102.66$元",
        "抽水：$102.66-100=2.66$元"]
    def construct(self):
        ble = Table(
                self.t1,
                self.path,
                dx=1.6,
                dy=0.5,
            )
        ble.dx_list[0] = 3
        ble.dy_list[0] = 0.6
        ble.arrange_table()

        if self.ptxt != None:
            ble.table.shift(UP).scale(1.2)
            ble.title.next_to(ble.table,UP*1.5).scale(1.1)
            pvg = VGroup()
            for p in self.ptxt:
                pvg.add(TexText(p,font_size=35,))

            pvg.arrange(DOWN)
            pvg.next_to(ble.table,DOWN*2)
        else:
            ble.table.shift(UP*0.5).scale(1.2)
            ble.title.next_to(ble.table,UP*1.5).scale(1.1)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=1
            )
        if self.ptxt != None:
            for pm in pvg:
                self.play(FadeIn(pm,scale=0.9))
                
        self.wait(2)
 
class Fifa2(Scene):
    def construct(self):
        ble = Table(
                "世界杯小组赛德国VS日本的价值投注分析",
                r"Z:\LiFiles\2022年\12月份\足彩\素材\价值投注",
                dx=2,
                dy=0.6,
            )
        ble.dx_list[0] = 2.2
        ble.dy_list[0] = 0.7
        ble.arrange_table()
        ble.table.scale(1.2).shift(0.2*UP)
        ble.title.next_to(ble.table,UP*1.8).scale(1.1)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=1
            )
        self.wait(2)

class Fifa3(Fifa1):
    t1 = "开赛前购买4只球队夺冠的彩票"
    path = r"Z:\LiFiles\2022年\12月份\足彩\素材\多组合"
    ptxt = [
        "$$\\text{成本：}16.67+14.29+13.33+12.5=56.79 \\text{元}$$",
        "$$\\text{利润：}100元-56.79元=43.21\\text{元}$$"]

class Fifa4(Scene):
    t1 = "开赛前购买两只球队夺冠的彩票："
    path1 = r"Z:\LiFiles\2022年\12月份\足彩\素材\对冲套利-1"
    t2 = "世界杯决赛某博彩公司开出的赔率和销售彩票金额比例"
    path2 = r"Z:\LiFiles\2022年\12月份\足彩\素材\对冲套利-2"
    t3 = "决赛前购买阿根廷获胜和平局的彩票："
    p1 = "$$\\text{共花费：}16.67+14.29+34.6+32.47=98\\text{元}$$"
    p2 = "$$\\text{锁定至少2元利润}$$"
    
    def construct(self):
        ble1 = Table(
                self.t1,
                self.path1,
                dx=1.73,
                dy=0.5,
            )
        ble1.dx_list[0] = 2
        ble1.dy_list[0] = 0.6
        ble1.arrange_table()
        ble1.table.to_edge(UP,buff=LARGE_BUFF)
        ble1.title.next_to(ble1.table,UP).scale(0.8)

        title3 = Text(
                self.t3,
                font_size=36,
                font ='Source Han Sans CN Regular',
            ).scale(0.8)

        ble2 = Table(
                self.t2,
                self.path2,
                dx=1.73,
                dy=0.5,
            )
        ble2.dx_list[0] = 2
        ble2.dy_list[0] = 0.6
        ble2.arrange_table()
        ble2.table.next_to(ble1.table,DOWN,buff=1.5)
        ble2.title.next_to(ble2.table,UP).scale(0.8)
                
        title3.next_to(ble2.title,UP)
        
        p1 = TexText(
                self.p1,
                font_size=30,
            )
        p2 = TexText(
                self.p2,
                font_size=30,
            )
        p1.next_to(ble2.table,DOWN*1.8)
        p2.next_to(p1,DOWN)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        
        self.play(
                LaggedStartMap(FadeIn,VGroup(ble1.title,ble1.table,ble2.title,ble2.table,title3),scale=0.9,lag_ratio=0.1),
                run_time=1
            )

        self.play(FadeIn(p1,scale=0.9))
        self.wait()
        self.play(FadeIn(p2,scale=0.9))
        self.wait(2)

class Fifa5(Fifa1):
    t1 = "日本队夺冠的彩票"
    path = r"Z:\LiFiles\2022年\12月份\足彩\素材\撤单套现"
    ptxt = [
        "$$\\text{以200元价格撤单套现，则}$$",
        "$$\\text{彩民锁定利润：}200-100=100\\text{元}$$",
        "$$\\text{博彩公司继续盈利：}313.75-200=113.75\\text{元}$$",
        ]

class Fifa6(Fifa1):
    t1 = "不同博彩公司开出赔率"
    path = r"Z:\LiFiles\2022年\12月份\足彩\素材\不同公司赔率"
    ptxt = None
    
class Fifa7(Fifa1):
    t1 = "A、B两家博彩公司开出不同赔率"
    path = r"Z:\LiFiles\2022年\12月份\足彩\素材\无风险套利"
    ptxt = [
        "$$\\text{总花费：}25+28.57+35.59=89.16\\text{元}$$",
        "$$\\text{利润：}100-89.16=10.84\\text{元}$$",
        ]

class GPT_p(Scene):
    title = "GPT高考物理测试汇总"
    path = r"./Ag/data_files/GPT物理测试"
    def construct(self):
        ble = Table(
                self.title,
                self.path,
                dx=1.73,
                dy=0.5,
            )
        ble.dx_list[0] = 2.1
        ble.dy_list[0] = 0.6
        ble.arrange_table()
        ble.table.scale(1.26).shift(UP*0.1)
        ble.title.scale(1.3).next_to(ble.table,UP,buff=MED_LARGE_BUFF)
        
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=1
            )
        self.wait()

class GPT_b(GPT_p):
    title = "GPT高考生物测试汇总"
    path = r"./Ag/data_files/GPT生物测试"

class GPT_h(GPT_p):
    title = "GPT高考历史测试汇总"
    path = r"./Ag/data_files/GPT历史测试"

class GPT_z(GPT_p):
    title = "GPT高考政治测试汇总"
    path = r"./Ag/data_files/GPT政治测试"

class GPT_e1(GPT_p):
    title = "GPT高考英语测试汇总（客观题）"
    path = r"./Ag/data_files/GPT英语测试-1"

class GPT_e2(GPT_p):
    title = "GPT高考英语测试汇总（主观题）"
    path = r"./Ag/data_files/GPT英语测试-2"

class GPT_y(GPT_p):
    title = "GPT高考语文写作测试汇总"
    path = r"./Ag/data_files/GPT语文测试"
    
class GPT_end1(GPT_p):
    title = "GPT高考各科正确率"
    path = r"./Ag/data_files/GPT测试统计1"

class GPT_end2(Scene):
    title = "GPT高考得分情况"
    path = r"./Ag/data_files/GPT测试统计2"
    def construct(self):
        ble = Table(
                self.title,
                self.path,
                dx=1.5,
                dy=0.5,
            )
        ble.dx_list[2] = 2.68
        ble.arrange_table()
        ble.title.scale(1.3).next_to(ble.table,UP,buff=MED_LARGE_BUFF)
        self.play(FadeIn(ble.title,scale=0.618),
                  FadeIn(ble.bg[0], scale=0.5),
                  FadeIn(ble.tex_column[0], scale=0.9)
            )
        self.play(
                FlashAround(ble.table),
                LaggedStartMap(FadeIn,ble.bg[1:],scale=0.9,lag_ratio=0.1),
                LaggedStartMap(FadeIn,ble.tex_column[1:],scale=0.9,lag_ratio=0.1),
                run_time=1
            )
        self.wait()
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} Fifa7 -o".format(__file__))