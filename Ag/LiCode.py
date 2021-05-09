from manimlib import *
import numpy.linalg as LA

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class SquareLocTxt():
    CONFIG ={
        "grid_color":"#333333",
        "buff":0,
        "num_d_p":0,
        "num_size":25,
    }
    def __init__(self, h, square, loc_txt_colors = None, **kwargs):
        digest_config(self, kwargs)
        self.grid = Square(
                    side_length=2,
                    fill_color=self.grid_color,
                    fill_opacity=1,
                    stroke_color="#111111",
                    stroke_width=2,
                    )\
            .get_grid(square, square, height= h, buff=self.buff)
        
        for i in range(square*square):
            text = DecimalNumber(0,
                    font_size=self.num_size,
                    num_decimal_places=self.num_d_p
                    )
            self.grid[i].txt = text
            self.grid[i].txt.move_to(self.grid[i])
        if loc_txt_colors is not None:
            self.change_sqare(loc_txt_colors)

        self.sq_Vg=VGroup()
        for i in range(len(self.grid)):
            self.sq_Vg.add(VGroup(self.grid[i],self.grid[i].txt))

    def change_sqare(self, locTxtTolors):
        for loc_txt_color in locTxtTolors:
            loc = loc_txt_color[0]
            num = loc_txt_color[1]
            color = loc_txt_color[2]
            self.grid[loc].set_style(
                    fill_color=color,
                    fill_opacity=1,
                    stroke_color="#111111",
                    stroke_width=2,
                    )
            self.grid[loc].txt=DecimalNumber(num,
                    font_size=self.num_size,
                    num_decimal_places=self.num_d_p,
                    color=BLACK
                    )
            self.grid[loc].txt.move_to(self.grid[loc])

class ConvolutionPic(Scene):
    def construct(self):
        white_7loc = [8,12,16,18,24,30,32,36,40] 
        loctc7 = [[]]*len(white_7loc)
        for i,w7 in enumerate(white_7loc):
            loctc7[i]=[w7,1,WHITE]
        sq7_7 = SquareLocTxt(4,7,loctc7)
 
        white_3loc = [0,4,8] 
        loctc3 = [[]]*len(white_3loc)
        for i,w3 in enumerate(white_3loc):
            loctc3[i]=[w3,1,WHITE]
        sq3_3 = SquareLocTxt(4*3/7,3,loctc3)

        white_5loc = [i for i in range(5*5)] 
        loctc5 = [[]]*len(white_5loc)
        areas = [[]]*len(white_5loc)
        formulas = [[]]*len(white_5loc)
        for i,w5 in enumerate(white_5loc):
            div = i // 5  #商
            mod = i % 5   #余
            txt = sq7_7.sq_Vg[8+div*7+mod-8][1].number*sq3_3.sq_Vg[0][1].number\
                + sq7_7.sq_Vg[8+div*7+mod-7][1].number*sq3_3.sq_Vg[1][1].number\
                + sq7_7.sq_Vg[8+div*7+mod-6][1].number*sq3_3.sq_Vg[2][1].number\
                + sq7_7.sq_Vg[8+div*7+mod-1][1].number*sq3_3.sq_Vg[3][1].number\
                + sq7_7.sq_Vg[8+div*7+mod-0][1].number*sq3_3.sq_Vg[4][1].number\
                + sq7_7.sq_Vg[8+div*7+mod+1][1].number*sq3_3.sq_Vg[5][1].number\
                + sq7_7.sq_Vg[8+div*7+mod+6][1].number*sq3_3.sq_Vg[6][1].number\
                + sq7_7.sq_Vg[8+div*7+mod+7][1].number*sq3_3.sq_Vg[7][1].number\
                + sq7_7.sq_Vg[8+div*7+mod+8][1].number*sq3_3.sq_Vg[8][1].number
            
            loctc5[i] = [w5,txt,RED_A]
           
            areas[i] = VGroup(
                    sq7_7.sq_Vg[8+div*7+mod-8],
                    sq7_7.sq_Vg[8+div*7+mod-7],
                    sq7_7.sq_Vg[8+div*7+mod-6],
                    sq7_7.sq_Vg[8+div*7+mod-1],
                    sq7_7.sq_Vg[8+div*7+mod-0],
                    sq7_7.sq_Vg[8+div*7+mod+1],
                    sq7_7.sq_Vg[8+div*7+mod+6],
                    sq7_7.sq_Vg[8+div*7+mod+7],
                    sq7_7.sq_Vg[8+div*7+mod+8],
                )
            jia = Tex("+",font_size=36)
            cheng = Tex("*",font_size=40)
            deng = Tex("=",font_size=40)
            formula1 = VGroup(
                        sq7_7.sq_Vg[8+div*7+mod-8][1].copy(),cheng.copy(),sq3_3.sq_Vg[0][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod-7][1].copy(),cheng.copy(),sq3_3.sq_Vg[1][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod-6][1].copy(),cheng.copy(),sq3_3.sq_Vg[2][1].copy(),
                        ).arrange(RIGHT,buff=0.1)
            formula2 = VGroup(
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod-1][1].copy(),cheng.copy(),sq3_3.sq_Vg[3][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod-0][1].copy(),cheng.copy(),sq3_3.sq_Vg[4][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod+1][1].copy(),cheng.copy(),sq3_3.sq_Vg[5][1].copy(),
                        ).arrange(RIGHT,buff=0.1)
            formula3 = VGroup(
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod+6][1].copy(),cheng.copy(),sq3_3.sq_Vg[6][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod+7][1].copy(),cheng.copy(),sq3_3.sq_Vg[7][1].copy(),
                        jia.copy(),sq7_7.sq_Vg[8+div*7+mod+8][1].copy(),cheng.copy(),sq3_3.sq_Vg[8][1].copy(),
                        ).arrange(RIGHT,buff=0.1).fix_in_frame()
            formula4 = VGroup(deng.copy(),DecimalNumber(txt,font_size=25,num_decimal_places=0))\
                        .arrange(RIGHT,buff=0.1)
            formulas[i]= VGroup(formula1,formula2,formula3,formula4)\
                        .arrange(DOWN,aligned_edge=RIGHT,buff=0.2)\
                        .set_color(RED)\
                        .to_corner(UR,buff=LARGE_BUFF).fix_in_frame()
        sq7_7.formula = formulas
        sq7_7.area = areas
        sq5_5 = SquareLocTxt(4*5/7,5,loctc5)
        sq7_7.sq_Vg.shift(OUT*(-10)).scale(1.2)
        sq3_3.sq_Vg.move_to(sq7_7.sq_Vg[10]).shift(OUT*9.6).scale(0.8)
        sq5_5.sq_Vg.move_to(sq7_7.sq_Vg[17]).shift(OUT*14).scale(0.75)

        lines7_3s = [[]]*len(white_5loc)
        lines3_5s = [[]]*len(white_5loc)
        ret7_7s = [[]]*len(white_5loc)
        ret5_5s = [[]]*len(white_5loc)
        ret3_3s = [[]]*len(white_5loc)
        for numCNA in range(5*5):
            lines7_3 = VGroup()
            lines3_5 = VGroup()
            for point in [UL,UR,DL,DR]:
                line1 = DashedLine(
                    start=sq7_7.area[numCNA].get_corner(point),
                    end=sq3_3.sq_Vg.get_corner(point),
                    color=GREEN,
                    stroke_width=2
                    )
                line2 = DashedLine(
                    start=sq3_3.sq_Vg.get_corner(point),
                    end=sq5_5.sq_Vg[numCNA].get_corner(point),
                    color=GREEN,
                    stroke_width=2
                    )
                lines7_3s[numCNA] = lines7_3.add(line1)
                lines3_5s[numCNA] = lines3_5.add(line2)
            
            ret7_7s[numCNA] = Square().match_height(sq7_7.area[numCNA])\
                        .set_style(
                            fill_color=GREEN,
                            fill_opacity=0.6,
                            stroke_color=GREEN_A,
                            stroke_width=2.5
                            )\
                        .move_to(sq7_7.area[numCNA])
            ret5_5s[numCNA] = Square().match_height(sq5_5.sq_Vg[numCNA])\
                        .set_style(
                            fill_color=GREEN,
                            fill_opacity=0.6,
                            stroke_color=GREEN_A,
                            stroke_width=2.5)\
                        .move_to(sq5_5.sq_Vg[numCNA])

            ret3_3s[numCNA] = Square().match_height(sq3_3.sq_Vg)\
                        .set_style(
                            fill_color=GREEN,
                            fill_opacity=0.2,
                            stroke_color=GREEN_A,
                            stroke_width=2)\
                        .move_to(sq3_3.sq_Vg)
        
        texj = Text("卷积核",size=0.42,color = RED).next_to(sq3_3.sq_Vg,UP ,buff = MED_SMALL_BUFF)
        self.play(FadeIn(sq7_7.grid,scale=0.5))
        self.wait()
        self.play(*[Write(text7.txt) for text7 in sq7_7.grid])
        self.wait()
        frame = self.camera.frame        
        self.play(
            frame.animate.set_euler_angles(
                theta=65 * DEGREES,
                phi=-30 * DEGREES,
                gamma=-65 * DEGREES
                )
            )
        self.play(
            ShowCreation(sq3_3.sq_Vg),
            Write(texj)
            )
        self.wait()
        self.play(FadeIn(sq5_5.sq_Vg,scale=0.5))
        num = 0
        self.play(Write(ret7_7s[num]))
        self.play(ShowCreation(lines7_3s[num]))
        self.play(Write(ret3_3s[num]))
        self.play(ShowCreation(lines3_5s[num]))
        self.play(
                Write(ret5_5s[num]),
                ShowCreation(sq7_7.formula[num]),
                )
        self.wait()
        
        self.play(LaggedStartMap(
            FadeOut,VGroup(
                    ret7_7s[num],
                    lines7_3s[num],
                    ret3_3s[num],
                    lines3_5s[num],
                    ret5_5s[num],
                    )
                )
            )
        self.remove(sq7_7.formula[num])
        self.wait()
        k = 3
        for i in range(1,k):
            self.add(
                VGroup(ret7_7s[i],lines7_3s[i],ret3_3s[i],lines3_5s[i],ret5_5s[i],))
            self.play(ShowCreation(sq7_7.formula[i])) 
            self.wait(1)
            if i < k-1:
                self.remove(VGroup(ret7_7s[i],lines7_3s[i],ret3_3s[i],lines3_5s[i],ret5_5s[i]))
                self.remove(sq7_7.formula[i])
            self.wait(0.5)    
        # self.remove(sq7_7.formula[k-1],texj)       
        self.play(
            LaggedStartMap(
                FadeOut,
                VGroup(ret7_7s[k-1],lines7_3s[k-1],ret3_3s[k-1],lines3_5s[k-1],ret5_5s[k-1],sq7_7.sq_Vg,sq3_3.sq_Vg,texj)),
            FadeOut(sq7_7.formula[k-1])
            )
        self.play(
            sq5_5.sq_Vg.animate.shift(LEFT*2),
            frame.animate.set_euler_angles(
                theta=0* DEGREES,
                phi=0 * DEGREES,
                gamma=0 * DEGREES,
                )
            )
        self.wait()

        sq3loc = [i for i in range(3*3)] 
        sq3loc_datas = [[]]*len(sq3loc)
        sq3loc_areas = [[]]*len(sq3loc)
        areas_num = [
                [0,1,5,6],
                [2,3,7,8],
                [4,9],
                [10,11,15,16],
                [12,13,17,18],
                [14,19],
                [20,21],
                [22,23],
                [24]
            ]
        for i,loc in enumerate(sq3loc):
            txt = max(list(sq5_5.sq_Vg[k][1].number for k in areas_num[i]))
            areas[i] = VGroup(*list(sq5_5.sq_Vg[k] for k in areas_num[i]))
            sq3loc_datas[i] = [loc,txt,WHITE]

        sq5_5.area = areas
        sq3 = SquareLocTxt(4*3/7,3,sq3loc_datas)
        sq3.sq_Vg.next_to(sq5_5.sq_Vg,buff=LARGE_BUFF*2).scale(0.8)
        ret5s = [[]]*len(sq3loc)
        ret3s = [[]]*len(sq3loc) 
        areas_color = [RED,GREEN,YELLOW,BLUE,TEAL_A,GOLD,MAROON,PURPLE,ORANGE]
        for jk in range(3*3):            
            ret5s[jk] = Rectangle(
                            height=sq5_5.area[jk].get_height(),
                            width=sq5_5.area[jk].get_width(),
                            )\
                        .set_style(
                            fill_color=areas_color[jk],
                            fill_opacity=0.6,
                            stroke_color=areas_color[jk],
                            stroke_width=2.5
                            )\
                        .move_to(sq5_5.area[jk])
            ret3s[jk] = Rectangle(
                            height=sq3.sq_Vg[jk].get_height(),
                            width=sq3.sq_Vg[jk].get_width(),
                            )\
                        .set_style(
                            fill_color=areas_color[jk],
                            fill_opacity=0.6,
                            stroke_color=areas_color[jk],
                            stroke_width=2.5)\
                        .move_to(sq3.sq_Vg[jk])

        arrow = Arrow(
            sq5_5.sq_Vg.get_right(),
            sq3.sq_Vg.get_left(),
            fill_color = WHITE ,
            thickness = 0.1)
        tex1 = Text("池化",size=0.6).next_to(arrow,UP,buff=SMALL_BUFF)

        self.play(
            ShowCreation(arrow),
            FadeIn(tex1,scale=0.5),
            Write(sq3.sq_Vg)
            )
        self.wait()
        for i in range(len(ret5s)):
            self.play(FadeIn(ret5s[i],scale=0.5))
            self.wait(0.1)
            self.play(TransformFromCopy(ret5s[i],ret3s[i]))
            self.wait(0.5)
        self.wait()

        self.play(
            FadeOut(sq5_5.sq_Vg),
            *[FadeOut(ret) for ret in it.chain(ret5s)],
            *[FadeOut(ret) for ret in it.chain(ret3s)],
            FadeOut(arrow),
            FadeOut(tex1),
            )
        self.play(sq3.sq_Vg.animate.shift(4.2*LEFT))

        fx_sq3_num = [i for i in range(3*3)] 
        fx_sq3_datas = [[]]*len(fx_sq3_num)
        for i,loc in enumerate(sq3loc):
            num = 1/(1+math.exp(-sq3.sq_Vg[i][1].number))
            fx_sq3_datas[i] = [loc,num,YELLOW]
        fx_sq3 = SquareLocTxt(4*3/7,3,fx_sq3_datas,num_size=18,num_d_p=2)
        fx_sq3.sq_Vg.next_to(sq3.sq_Vg,buff=LARGE_BUFF*3).scale(0.8)

        arrow = Arrow(
            sq3.sq_Vg.get_right(),
            fx_sq3.sq_Vg.get_left(),
            fill_color = WHITE ,
            )
        tex1 = Tex("f\\left(x\\right) =\\frac{1}{1+e^{-x}}",font_size=20)\
                .next_to(arrow,UP,buff=SMALL_BUFF)\
                .set_color(YELLOW)
        
        axes = Axes(
            (-5,5), (-0.3,1.6),
            height=1.2,
            width=9*4/16,
            axis_config={
                "include_ticks": False,
                "tip_config": {
                    "width": 0.12,
                    "length": 0.12,
                    },
                },
            )
        fx_graph = axes.get_graph(
            lambda x: 1/(1+math.exp(-x)),
            color=YELLOW,
            stroke_width=5,
            x_range = np.array([-4.8, 4.8]),
            )
        step_graph = DashedVMobject(
                axes.get_graph(
                    lambda x: 1 if x > -5 else 1.0,
                    color=RED,
                )
            )
        axes_graph = VGroup(axes,fx_graph,step_graph)\
            .next_to(arrow,DOWN,buff=SMALL_BUFF)
        
        self.play(ShowCreation(arrow))
        self.play(
            Write(tex1),
            Write(axes),
            Write(step_graph),
            ShowCreation(fx_graph)
            )
        self.play(FadeIn(fx_sq3.sq_Vg,shift=RIGHT))
        self.wait(3)
      
class LiSa(Scene):
    def construct(self):
        h_step = 0.2
        w_step = 3
        background = Rectangle(
                width=10,
                height=2.8,
                fill_color = BLUE,
                fill_opacity = 1,
            ).move_to(BOTTOM+LEFT_SIDE)

        def harmonic_series(num):
            sum_series=0
            for i in range(1,num):
                sum_series=sum_series+1/i
            return sum_series

        def li_sa_func(shape = 10):
            vg_shapes = VGroup()
            for i in range(1,shape+1):
                rect = Rectangle(width=w_step, height=h_step)
                rect.next_to(background,UP,aligned_edge=RIGHT,buff=0)
                rect.shift(w_step*(harmonic_series(shape+1)-harmonic_series(i))/2*RIGHT+0.18*DOWN)
                txt = Text(str(i)).scale(0.25).next_to(LEFT_SIDE+(background.get_top()[1]-0.0618)*UP,RIGHT).set_color(GREY)
                vg_shapes.add(rect,txt)
                vg_shapes.shift(h_step*UP)
            return vg_shapes
        
        def formula_txt(mob):
            text = Tex(r"\frac{1}{2} L(1+\frac{1}{2} +\frac{1}{3} +\dots +\frac{1}{n} )")
            text.scale(0.6)
            arr = DoubleArrow(
                    background.get_right()[0]*RIGHT,mob.get_right()[0]*RIGHT,
                    buff = 0,
                    thickness=0.075,
                ).move_to(background.get_corner(UR)+0.2*DOWN,coor_mask=[0,1,0]).set_color(YELLOW)
            text.add_updater(lambda m:m.next_to(arr,UP,buff=0))   
            return text,arr

        self.add(background,)
        # frame = self.camera.frame
        # frame.scale(2)
        n = 30   
        for i in range(n):
            model = li_sa_func(i+1)
            arr, text = formula_txt(model)
            if len(model)>30:
                self.add(arr, text )
            self.add(model)
            self.wait(0.5)
            if i != n-1:
                self.remove(model, arr, text )
        self.wait(5)


def PJcurvature(x,y):
    """
    input  : the coordinate of the three point
    output : the curvature and norm direction
    """
    t_a = LA.norm([x[1]-x[0],y[1]-y[0]])
    t_b = LA.norm([x[2]-x[1],y[2]-y[1]])
    M = np.array([
        [1, -t_a, t_a**2],
        [1,    0,   0   ],
        [1,  t_b, t_b**2]
    ])
    a = np.matmul(LA.inv(M),x)
    b = np.matmul(LA.inv(M),y)
    kappa = 2*(a[2]*b[1]-b[2]*a[1])/(a[1]**2.+b[1]**2.)**(1.5)
    return kappa, [b[1], -a[1], 0]/np.sqrt(a[1]**2.+b[1]**2.)

class Curvature(Scene):
    def construct(self):
        d = 1e-2
        vlu = ValueTracker(d)
        coords = np.array((
                (-7,  3, 0),
                (-5,  1, 0),
                (-2, -1, 0),
                ( 0,  0, 0),
                ( 3, -3, 0),
                ( 4,  2, 0),
                ( 7,  3, 0),
            ))
        curve = VMobject()
        curve.set_points_smoothly(coords)
        curve.set_style(stroke_width=8)
        tan_line_and_vector_and_cirle = self.curvature_vector(curve, vlu.get_value())
        tan_line_and_vector_and_cirle.add_updater(
                lambda mob: mob.become(self.curvature_vector(curve, vlu.get_value()))
            )
        self.add(curve, tan_line_and_vector_and_cirle)
        self.play(
                vlu.set_value, 0.587,
                run_time = 30,
                rate_func = linear,
            )

    def curvature_vector(self, curve_mob, alpha, d_alpha=1e-2):
        tan_line = TangentLine(curve_mob, alpha, color=GREY, length=20)
        curve_p = np.array([
                curve_mob.pfp(alpha-d_alpha),
                curve_mob.pfp(alpha),
                curve_mob.pfp(alpha+d_alpha),
            ])
        x, y = curve_p[:,0], curve_p[:,1]
        kappa, norm = PJcurvature(x,y)
        vector = Vector(norm*1/kappa, fill_color=BLUE)
        vector.move_to(curve_mob.pfp(alpha)+vector.get_end()/2)
        circle = Circle(radius = 1/kappa, stroke_width=10)
        circle.move_to(vector.get_end())
        return VGroup(tan_line, vector, circle)

class Table_mol(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        data = get_coords_from_csvdata(r"Ag/data_files/mol_datas")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        x, y, dx, dy = -column+1, 3, 2.1, 0.5
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
 
        allGroupHead = VGroup(
                dataTxtBackground[0],
                dataTxtBackground[0].copy(),
                *dataTxt[:column]
            )

        allGroup = VGroup(
                dataTxtBackground[0].copy(),
                *dataTxtBackground,
                *dataTxt,
            )

        self.play(
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

