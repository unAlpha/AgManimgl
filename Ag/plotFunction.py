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
        