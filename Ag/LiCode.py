# -*- coding: utf-8 -*-
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

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

# This classes returns graphs
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)
        
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
        curve.set_points_smoothly(coords,true_smooth=True)
        curve.set_style(stroke_width=8)
        tan_line_and_vector_and_circle = self.curvature_vector(curve, vlu.get_value())
        tan_line_and_vector_and_circle.add_updater(
                lambda mob: mob.become(self.curvature_vector(curve, vlu.get_value()))
            )
        self.add(curve, tan_line_and_vector_and_circle)
        self.play(
                vlu.animate.set_value(0.98),
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
        vector = Vector(norm*1/kappa, color=BLUE)
        vector.move_to(curve_mob.pfp(alpha)+vector.get_end()/2)
        circle=VMobject()
        if abs(1/kappa)>50:
            circle = circle.become(tan_line.copy().set_style(stroke_width=10,stroke_color=RED))
            circle.move_to(vector.get_start())
        else:
            circle = circle.become(Circle(radius = abs(1/kappa), stroke_width=10))
            circle.move_to(vector.get_end())
        return VGroup(tan_line, vector, circle)
 
class PrimalityTest(Scene):
    def construct(self):
        fz = 48
        aText = Tex("a","=",font_size=fz)
        PText = Tex("P","=",font_size=fz)
        aPText = Tex(
            "(","a","^P","-","a",")","\\ ","mod","\\ ","P",
            font_size=fz,
            )
        VgText = VGroup(aText,PText,aPText)
        for line in VgText:
                line.set_color_by_tex_to_color_map({
                "a": BLUE,
                "P": GREEN,
            })
                
        a = ValueTracker(1)
        aTxt = DecimalNumber(
            a.get_value(),
            font_size=fz,
            num_decimal_places=0,
            ).add_updater(lambda v: v.set_value(a.get_value()))
        aTVg = VGroup(aText,aTxt).arrange(RIGHT).shift(UP*2.5)
        
        P = ValueTracker(13)
        PTxt = DecimalNumber(
            P.get_value(),
            font_size=fz,
            num_decimal_places=0,
            color = GREEN,
            ).add_updater(lambda v: v.set_value(P.get_value()))
        PTVg = VGroup(PText,PTxt).arrange(RIGHT).next_to(aTVg,DOWN,buff=MED_LARGE_BUFF)
        NumX = Text("（质数）",font ='SimSun',color=RED,font_size=40).next_to(PTVg,RIGHT)
        aPText.next_to(PTVg,DOWN,buff=LARGE_BUFF)
        
        pwText=DecimalNumber(
                    math.pow(a.get_value(),P.get_value())-a.get_value(),
                    font_size=fz,
                    num_decimal_places=0,
                )\
                .add_updater(lambda v: v.set_value(
                            math.pow(a.get_value(),P.get_value())-a.get_value(),
                        )
                    )
        
        eq = VGroup(Tex("="),pwText)\
            .arrange(RIGHT)\
            .next_to(aPText,DOWN,aligned_edge=LEFT,buff=MED_LARGE_BUFF)
            
        mod = Tex("mod").add_updater(lambda v: v.next_to(eq,RIGHT))
        PTxtCp = PTxt.copy().add_updater(lambda v: v.next_to(mod,RIGHT))
        
        aPTxt = DecimalNumber(
                (math.pow(a.get_value(),P.get_value())-a.get_value())\
                    %P.get_value(),
                font_size=fz,
                num_decimal_places=0,
                color = RED
                )\
            .add_updater(lambda v: v.set_value(
                (math.pow(a.get_value(),P.get_value())-a.get_value())\
                    %P.get_value(),
                    )
                )
        aPTVg = VGroup(Tex("="),aPTxt)\
                .arrange(RIGHT)\
                .next_to(eq,DOWN,buff=MED_LARGE_BUFF,aligned_edge=LEFT)
                
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.add(aTVg,PTVg,aPText,aPTVg,eq,PTxtCp,mod,NumX)
        self.wait()
        for val in range(1,17):
            self.wait(0.5)
            a.set_value(val)
        self.wait()

class CChess(Scene):
    def construct(self):
        from Ag.CChessClass import CCClass
        ran = CCClass().pieces.astype(int)
        print(ran)
        ranloc = []
        for i in range(1,ran.size+1):
            ranloc.append(np.append(np.argwhere(ran == i),[0]))
        print(ranloc)
        ranloc.append(ranloc[0])
        
        sqrSVg=VGroup()
        for loc in ranloc:
            sqr = Square(
                    fill_color=WHITE,
                    fill_opacity=0.5,
                    stroke_opacity=0,
                ).scale(0.486).move_to(loc)
            sqrSVg.add(sqr)
        sqrSVg.scale(0.8).rotate(PI/2).center()
        
        polyline = VMobject(stroke_width=8,color=BLUE)
        polyline.set_points_as_corners(ranloc).scale(0.8).rotate(PI/2).center()
        
        # ma = ImageMobject("LiPics/Xiangqi_hl1.png").scale(0.16)
        ma = Dot().scale(2)
        self.play(
            LaggedStart(
                ShowCreation(polyline),
                MoveAlongPath(ma,polyline),
                lag_ratio=-1,
                ),
            run_time=5,
            rate_func=linear
            )
        self.wait()

class PieChart(VMobject):
    CONFIG = {
        "start_per" : 0,
        "r" : 2,
        "gap" : 0,
        "stroke" : 100,
        "legend_style" : "Dot",
        "legend_loc" : 3.6*RIGHT + 0*UP,
        "legend_scale" : 1,
        "y_buff" : MED_SMALL_BUFF 
    }

    def create_arc(self, percentage, arc_color):
        arc = Arc(
            radius = self.r,
            start_angle = self.start_per/100*TAU,
            angle = percentage/100*TAU-self.gap,
            color = arc_color,
            stroke_width = self.stroke,
        )
        # 很有启示
        self.start_per += percentage
        return arc

    def craet_arcs(self, args):
        arc_group = VGroup()
        for per, color, name in args:
            arc_group.add(self.create_arc(per, color))
        self.arcs = arc_group
        return self.arcs

    def create_legend(self, per, arc_color, name):
        per_text = Text(
            str(per)+"%", 
            font ='SimSun',
            font_size=48,
        )

        name_text = Text(
            name, 
            font ='SimSun',
            font_size=48,
        )

        if self.legend_style == "Dot":
            dot_color = Dot(color = arc_color).scale(2.5)
        elif self.legend_style == "Rect":
            dot_color = Square(
                color = arc_color,
                fill_color = arc_color,
                fill_opacity = 1,
            ).scale(0.16)
        
        dot_color.shift(self.legend_loc)
        name_text.next_to(dot_color, RIGHT)
        per_text.next_to(dot_color, LEFT)
        return VGroup(dot_color, name_text, per_text)

    def create_legends(self, args):
        legend_group = VGroup()
        for per, dot, name in args:
            legend_group.add(
                self.create_legend(
                    per, dot, name,
                )
            )
        self.legends = legend_group.scale(self.legend_scale).arrange(
                DOWN,
                buff=self.y_buff,
                index_of_submobject_to_align=0
            )
        return self.legends

    def create_title(self, title):
        return Text(title)
    
    def highlight_items_arcs(self, arcs, item=0):
        arcs[item].scale(1.1,about_point=arcs.get_center())
        return arcs

    def highlight_items_legends(self, legends, item=0):
        legends[item].scale(1.5,about_point=legends[item][0].get_center())
        legends.arrange(
            DOWN,
            center=False,
            buff=self.y_buff,
            index_of_submobject_to_align=0
        )
        return legends

class PieChartScene(Scene):
    def construct(self):
        pc_data = [
            # 百分比形式
            (7, BLUE, "第一支柱 联邦养老金 2.85万亿"),
            (58, RED, "第二支柱 401k 22.8万亿"),
            (35, GOLD, "第三支柱 IRA 13.9万亿"),
            # (58.7, BLUE, "第一支柱 基本养老金 6.3万亿"),
            # (41.3, RED, "第二支柱 企业/职业年金 4.4万亿"),
            # (0.01, GOLD, "第三支柱 个人养老金账户 6亿"),
        ]
        pie_chart = PieChart()
        pc_arcs = pie_chart.craet_arcs(pc_data)
        pc_legends = pie_chart.create_legends(pc_data)
        VGroup(pc_arcs,pc_legends).arrange(RIGHT, buff=LARGE_BUFF*1.5)
            
        self.play(
            LaggedStartMap(ShowCreation,pc_arcs,lag_ratio=1),
            LaggedStartMap(Write,pc_legends,lag_ratio=1),
            run_time=5,
        )

        highlight_items = [0, 1, 2]
        for item in highlight_items:
            self.play(
                Transform(
                    pc_arcs,
                    pie_chart.highlight_items_arcs(pc_arcs.copy(),item)
                ),
                Transform(
                    pc_legends,
                    pie_chart.highlight_items_legends(pc_legends.copy(),item)
                ),
                rate_func=there_and_back_with_pause,
                run_time = 2,
            )
        self.wait()
    
class TexTextTransform1(Scene):
    def construct(self):
        tex = TexText(
            "$$\\text { (1) } \\ t_{2}^{\\prime \\prime} \\ \\text {时间内} \\ v=v_{0}-\\frac{1}{2} \\cdot \\frac{a_{m}}{t_{2}^{\\prime \\prime}} \\cdot t^{2}$$",
            "$$t_{2}^{\\prime \\prime} \\ \\text {末速度} \\ v_{2}=v_{0}-\\frac{1}{2} a_{m} t_{2}^{\\prime \\prime}$$",
            "$$\\text { (2) } \\ t_{3} \\ \\text {时间内} \\ a=a_m,\\ \\text {末速度为}0，$$",
            "$$\\text {由匀变速运动公式} $$",
            "$$0^{2}-v_{2}^{2}=2(-a) \\cdot s_{3}$$",
            "$$\\text {得} \\ s_{3}=\\frac{v_{2}^{2}}{2 a}=\\frac{\\left(v_{0}-\\frac{1}{2} a_{m} t_{2}{ }^{\\prime \\prime}\\right)^{2}}{2 a_{m}} $$",
            "$$\\text {得} \\ s_{3}=\\frac{v_{0}^{2}}{2 a_{m}}-\\frac{v_{0} t_{2}^{\\prime \\prime}}{2}+\\frac{a_{m} t^{\\prime \\prime}_{2}{ }^{2}}{8} $$",
            font ='SimSun',
        ).arrange(DOWN, buff = 0.5,aligned_edge = LEFT)
        tex[0].shift(LEFT)
        tex[2].shift(LEFT)
        tex.scale(0.6)
        tex.center()
        tex.shift(0.5*UP)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(Write(tex))
        self.wait()
    
class TexTextTransform2(Scene):
    def construct(self):
        tex = TexText(
            "$$\\text { (1) } t_{2}^{\\prime} \\text { 时间 }: a=0,\\quad {  v=v_{0}}, \\quad s_{2}^{\\prime}=v_{0} t_{2}^{\\prime}$$",
            "$$\\text { (2) } t_{2}^{\\prime \\prime} \\text { 时间 }: a=\\frac{t}{t_{2}^{\\prime \\prime}} a_{m}$$",
            "$$\\frac{d v}{d t}=-a=-\\frac{t}{t_{2}^{\\prime \\prime}} a_{m} , \\quad d v=-\\frac{a_{m}}{t_{2}^{\\prime \\prime}} t \\cdot d t$$",
            "$$ v=v_{0}-\\frac{1}{2} \\cdot \\frac{a_{m}}{t_{2}^{\\prime \\prime}} \\cdot t^{2}, \\quad \\frac{d s_{2}^{\\prime \\prime}}{d t}=v_{0}-\\frac{1}{2} \\frac{a_{m}}{t^{\\prime \\prime}_{2}} t^{2} $$",
            "$$ds_{2}^{\\prime \\prime}=v_{0} d t-\\frac{1}{2} \\cdot \\frac{a_{m}}{t_{2}{ }^{\\prime \\prime}} t^{2} \\cdot d t$$",
            "$$s_{2}^{\\prime \\prime}=v_{0} t_{2}^{\\prime \\prime}-\\frac{1}{6} \\frac{a_{m}}{t^{\\prime \\prime}_{2}} \\cdot t^{\\prime \\prime3 }_{2}=v_{0} t_{2}^{\\prime \\prime}-\\frac{1}{6} a_{m} {t^{\\prime \\prime}_{2}}$$",
            "$$\\text { (3) } s_{2}=s_{2}^{\\prime}+s_{2}^{\\prime \\prime}=v_{0} t_{2}^{\\prime}+v_{0} t_{2}^{\\prime \\prime}-\\frac{1}{6} a_{m} t_{2}^{\\prime \\prime 2} $$",
            font ='SimSun',
        ).arrange(DOWN, buff = 0.5,aligned_edge = LEFT)
        tex[0].shift(LEFT*0.8)
        tex[1].shift(LEFT*0.8)
        tex[6].shift(LEFT*0.8)
        tex.scale(0.6)
        tex.center()
        tex.shift(0.3*UP)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(Write(tex))
        self.wait()
        
class TexTextTransform3(Scene):
    def construct(self):
        tex = TexText(
            "$$s=v_{0}\\left(t_{1}+t_{2}{ }^{\\prime}+\\frac{1}{2} t_{2}{ }^{\\prime \\prime}\\right)+\\frac{v_{0}^{2}}{2 a_{m}}-\\frac{a_{m} t_{2}^{\\prime \\prime 2}}{24}$$",
            "$$v_{0}:\\text{汽车初速度}$$",
            "$$t_1:\\text{驾驶员反应时间}$$",
            "$$t_2^{\prime}:\\text{制动系统反应时间}$$",
            "$$t_2^{\prime \prime}:\\text{制动力增加时间}$$",
            "$$a_m=\\varphi_m g:\\text{最大制动力加速度}$$",
            "$$\\varphi_m:\\text{峰值附着系数}$$",
            font ='SimSun',
        )
        tex[0].scale(0.7)
        tex[1:].arrange(DOWN, buff = 0.5,aligned_edge = LEFT)
        tex[1:].scale(0.6)
        tex.center()
        tex.shift(0.3*UP)        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(Write(tex))
        self.wait()
        
class Graph1(Scene):
    def construct(self):
        axes = Axes(
            (-1, 13), 
            (-1, 6),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                }
            )
        x_label = Text("t").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("a").next_to(axes.y_axis.get_corner(UR),RIGHT)
        
        def fun(x):
            if x <= 5:
                return 0
            if x>5 and x<=7:
                return 10*x/5-10
            if x>7:
                return 10*7/5-10
            
        step_graph = axes.get_graph(
            fun,
            x_range = [0,12],
            use_smoothing=False,
            color=RED,
            stroke_width=10,
        )
        
        # axes_merge = VGroup(axes,step_graph).scale(0.8)
        point_text = [
            [[0,0],[3,0],"t_1", DOWN],
            [[3,0],[5,0],"t_2^{\prime}", UP],
            [[5,0],[7,0],"t_2^{\prime \prime}", UP],
            [[7,0],[12,0],"t_3", DOWN],
            [[3,0],[7,0],"t_2", DOWN],
        ]
        
        dot_points = [
            [3,0],
            [5,0],
            [7,0],
            [12,0],
        ]
        
        BLG = VGroup()
        
        for pt in point_text:
            BLG.add(
                BraceLabel(
                    Line(axes.c2p(*pt[0]),axes.c2p(*pt[1])),
                    pt[2],
                    brace_direction=pt[3],
                    )
                )
        dots = VGroup()
        for dt in dot_points:
            dots.add(Dot(color=YELLOW).move_to(axes.c2p(*dt)))
            
            
        lh7 = axes.get_v_line_to_graph(7,step_graph)
        lh12 = axes.get_v_line_to_graph(12,step_graph)
        
        tex = TexText(
            "$$t_{1} :\\text{驾驶员反应时间}$$",
            "$$t_{2}^{\prime}:\\text{杀车系统反应时间}$$",
            "$$t_{2}^{\prime \prime} :\\text{地面制动力增大时间}$$",
            "$$t_{3} :\\text{匀减速制动时间}$$",
            font ='SimSun',
        ).arrange_in_grid(2,2,aligned_edge=LEFT)
        tex.scale(0.6).to_edge(UP)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.play(
            ShowCreation(step_graph),
            LaggedStartMap(FadeIn,VGroup(dots,lh7,lh12,x_label,y_label,tex),lag_ratio=1),
        )
        self.add(BLG)
        self.wait()

class PieChartElec1(Scene):
    def construct(self):
        pc_data = [
            # 百分比形式
            (67.4, BLUE, "火电 56463亿"),
            (16.0, RED, "水电 13401亿"),
            (4.9, GOLD, "核电 4075亿"),
            (7.8, TEAL_D, "风电 6556亿"),
            (3.9, PURPLE_C, "太阳能 3270亿"),
        ]
        pie_chart = PieChart()
        pc_arcs = pie_chart.craet_arcs(pc_data)
        pc_legends = pie_chart.create_legends(pc_data)
        VGroup(pc_arcs,pc_legends).arrange(RIGHT, buff=LARGE_BUFF*1.5)
            
        self.play(
            LaggedStartMap(ShowCreation,pc_arcs,lag_ratio=1),
            LaggedStartMap(Write,pc_legends,lag_ratio=1),
            run_time=5,
        )

        highlight_items = [0, 1, 2]
        for item in highlight_items:
            self.play(
                Transform(
                    pc_arcs,
                    pie_chart.highlight_items_arcs(pc_arcs.copy(),item)
                ),
                Transform(
                    pc_legends,
                    pie_chart.highlight_items_legends(pc_legends.copy(),item)
                ),
                rate_func=there_and_back_with_pause,
                run_time = 2,
            )
        self.wait()

class PieChartElec2(Scene):
    def construct(self):
        pc_data = [
            # 百分比形式
            (15.3, BLUE, "火电 663亿"),
            (81.6, RED, "水电 3531.4亿"),
            (0, GOLD, "核电 0亿"),
            (2.4, TEAL_D, "风电 106.2亿"),
            (0.7, PURPLE_C, "太阳能 28.8亿"),
        ]
        pie_chart = PieChart()
        pc_arcs = pie_chart.craet_arcs(pc_data)
        pc_legends = pie_chart.create_legends(pc_data)
        VGroup(pc_arcs,pc_legends).arrange(RIGHT, buff=LARGE_BUFF*1.5)
            
        self.play(
            LaggedStartMap(ShowCreation,pc_arcs,lag_ratio=1),
            LaggedStartMap(Write,pc_legends,lag_ratio=1),
            run_time=5,
        )

        highlight_items = [0, 1, 2]
        for item in highlight_items:
            self.play(
                Transform(
                    pc_arcs,
                    pie_chart.highlight_items_arcs(pc_arcs.copy(),item)
                ),
                Transform(
                    pc_legends,
                    pie_chart.highlight_items_legends(pc_legends.copy(),item)
                ),
                rate_func=there_and_back_with_pause,
                run_time = 2,
            )
        self.wait()

class TexTextTransform4(Scene):
    def construct(self):
        tex = TexText(
            "$$\\text{求证：三角形内角和等于}180^{\\circ}$$",
            "$$\\text{证明：需证C,D,E三点共线，即}(x-x_2)(y_1-y)-(x_1-x)(y-y_2)=0$$",
            "$$\\text{由于M是BC中点},x_M=\\frac{1}{2}(x+1), y_{M}=\\frac{1}{2}(y+0)$$",
            "$$\\text{由于M是AD中点}x_1=2x_M-0, y_1=2y_M-0$$",
            "$$\\text{可见: }x_1\\text{是}x\\text{的一次函数、}y_1\\text{是}y\\text{的一次函数。}$$",
            "$$\\text{同理：}x_2\\text{是}x\\text{的一次函数、}y_2\\text{是}y\\text{的一次函数。}$$",
            "$$(x-x_{2})(y_{1}-y)-(x_{1}-x)(y-y_{2})=0\\ \\text{中的}x,y\\text{最高次都是1次。}$$",
            "$$\\text{只需要}2\\times2=4\\text{个例证，即}(x,y)=(0,0),(1,0),(0,1),(1,1)\\text{即可。}$$",
            font ='SimSun',
        )
        tex.scale(0.7)
        tex.arrange(DOWN, buff = 0.2,aligned_edge = LEFT)
        tex[0:2].shift(LEFT*0.9)
        tex.to_edge(RIGHT)
        tex.shift(0.3*UP)        
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.play(Write(tex))
        self.wait()
        
class TexTextTransform5(Scene):
    def construct(self):
        tex = TexText(
            "$$\\text{代数基本定理：}$$",
            "$$\\text{任何一个非零的一元n次复系数多项式}$$",
            "$$a_{n}x^{n}+a_{n-1} x^{n-1}+a_{n-2} x^{n-2}+\ldots+a_{1} x+a_{0}=0,$$",
            "$$\\text{都正好有n个复数根。}$$",

            font ='SimSun',
        )
        tex[1:].scale(0.7)
        tex.arrange(DOWN, buff = 0.5,aligned_edge = LEFT)
        tex.to_edge(RIGHT*2)
        tex.shift(0.3*UP)        
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.play(Write(tex))
        self.wait()

class Graph2(Scene):
    def construct(self):
        axes = Axes(
            (-1, 13), 
            (-1, 6),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                }
            )
        x_label = Text("t").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("a").next_to(axes.y_axis.get_corner(UR),RIGHT)
        
        def fun(x):
            if x <= 5:
                return 0
            if x>5 and x<=7:
                return 10*x/5-10
            if x>7:
                return 10*7/5-10
            
        step_graph = axes.get_graph(
            fun,
            x_range = [0,12],
            use_smoothing=False,
            color=RED,
            stroke_width=10,
        )
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.play(
            ShowCreation(step_graph),
            LaggedStartMap(FadeIn,VGroup(x_label,y_label),lag_ratio=1),
        )
        self.wait()

class Formula1(Scene):
    def construct(self):
        text =Text("目前找到的最大孪生素数对",font_size=68,font="思源黑体",gradient=[RED,YELLOW],weight=BOLD)
        tex1 =Tex("2996863034895 \\times 2^{1290000}+1")
        tex2 =Tex("2996863034895 \\times 2^{1290000}-1")
        tex = VGroup(text,tex1,tex2).arrange(DOWN)
        text.shift(UP*0.5)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            ShowCreation(tex),
        )
        self.wait()

class Formula2(Scene):
    def construct(self):
        text =Text("哈代-李特伍德猜想",font_size=68,font="思源黑体",gradient=[RED,YELLOW],weight=BOLD)
        tex1 =TexText("$$\\pi_{2}(x) \\sim 2 C_{2} \\int_{2}^{x} \\frac{d t}{\\ln ^{2} t} \\sim 2 C_{2} \\frac{x}{\\ln ^{2}(x)}$$")
        tex2 =TexText("$$\\text{其中} \\ C_{2}=\\prod_{\\substack{prime \\\ p \\geq 3}}\\left (1-\\frac{1}{(p-1)^{2}}\\right)=0.6601618158 \\ldots$$",)
        tex = VGroup(text,tex1,tex2).arrange(DOWN)
        text.shift(UP*0.5)
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.play(
            ShowCreation(tex),
        )
        self.wait()

class CustomGraph4(Scene):
    def construct(self):
        axes = Axes(
            (0,12000000,2000000), 
            (0,72000,12000,),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                "include_tip":True,
                },
            )
        axes.add_coordinate_labels()
        axes.scale(0.9618)
        x_label = Text("自然数N",font="思源黑体").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("对数",font="思源黑体").next_to(axes.y_axis.get_corner(UR),RIGHT)
        self.add(axes,x_label,y_label)
        # Get coords
        text1 = Text("小于自然数N的孪生素数对(白线)",font="思源黑体",font_size=36)
        text2 = Text("哈-李猜想估计出的孪生素数对(红线)",font="思源黑体",font_size=36,color=RED)
        text = VGroup(text1,text2).arrange(DOWN,aligned_edge=LEFT).shift(RIGHT)
        coords1 = get_coords_from_csv(r"Ag\data_files\Littlewood_conjecture1")
        coords2 = get_coords_from_csv(r"Ag\data_files\Littlewood_conjecture2")
        points1 = [axes.c2p(px,py) for px,py in coords1]
        points2 = [axes.c2p(px,py) for px,py in coords2]
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points1,color=WHITE,stroke_width=10)
        graph2 = DiscreteGraphFromSetPoints(points2,color=RED,stroke_width=10,stroke_opacity=0.68)
        # Set dots
        dots1 = VGroup(*[
            Dot(radius=0.06,color=WHITE).move_to([px,py,pz])
            for px,py,pz in points1])
        dots2 = VGroup(*[
            Dot(radius=0.06,color=RED).move_to([px,py,pz])
            for px,py,pz in points2])
        self.add(text.to_corner(UP))
        self.play(ShowCreation(dots1,run_time=2))
        self.play(ShowCreation(graph1,run_time=1))
        self.play(ShowCreation(dots2,run_time=1))
        self.play(ShowCreation(graph2,run_time=4))
        self.wait(3)

class TexTextTransform4(Scene):
    def construct(self):
        tex = TexText(
                "$$\\text{黎曼Zeta函数:}$$",
                "$$\\zeta(s)=\\frac{1}{\\Gamma(s)} \\int_{0}^{\\infty} \\frac{x^{s-1}}{e^{x}-1} dx$$",
                "$$\\text{其中伽马函数}$$",
                "$$\\Gamma(s)=\\int_{0}^{\\infty} t^{s-1} e^{-t} dt$$",
                font ='SimSun',
            )

        text = TexText(
            "$$\\text{复平面中一矩形区域的黎曼}\\zeta\\text{函数}$$",
            font_size=30,
            font ='SimSun',
            )
        
        tex.arrange(DOWN, buff = 0.5,aligned_edge = LEFT)
        tex.scale(0.618).shift(UP*0.618)
        tex[1].shift(RIGHT)
        tex[3].shift(RIGHT)
        text.to_corner(UR).shift(LEFT*1.5)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)

        self.play(
            tex.animate.to_corner(LEFT*3),
            FadeIn(text,scale=0.618)
            )
        self.wait()

class CustomGraph5(Scene):
    def construct(self):
        axes = Axes(
            (0,6,1), 
            (0,1.1,0.2,),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 4,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                "include_tip":True,},
            y_axis_config={ 
                "decimal_number_config": {
                    "num_decimal_places": 2,
                },
            },
            )
        
        axes.add_coordinate_labels()
        axes.scale(0.86)
        x_label = Text("进球数",font="思源黑体").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("概率",font="思源黑体").next_to(axes.y_axis.get_corner(UR),RIGHT)
        
        # Get coords
        title = Text("奇数个进球情况",font="思源黑体",font_size=60)
        title.to_corner(UP)
        text1 = Text("日本队获胜",font="思源黑体",font_size=36)
        text2 = Text("德国队获胜",font="思源黑体",font_size=36,color=RED)
        coords1 = [
            [1,0.3],
            [3,0.22],
            [5,0.16]
            ]
        coords2 = [
            [1,0.7],
            [3,0.78],
            [5,0.84]
            ]
        points1 = [axes.c2p(px,py) for px,py in coords1]
        points2 = [axes.c2p(px,py) for px,py in coords2]
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points1,color=WHITE,stroke_width=10)
        graph2 = DiscreteGraphFromSetPoints(points2,color=RED,stroke_width=10)
        # Set dots
        dots1 = VGroup(*[
            Dot(radius=0.1,color=WHITE).move_to([px,py,pz])
            for px,py,pz in points1])
        
        p1 = VGroup(*[
            Tex(str(coords[1]*100)+"\\%").scale(0.618).next_to([px,py,pz],DOWN,buff=0.2)
            for [px,py,pz],coords in zip(points1,coords1)])
        
        dots2 = VGroup(*[
            Dot(radius=0.1,color=RED).move_to([px,py,pz])
            for px,py,pz in points2])

        p2 = VGroup(*[
            Tex(str(coords[1]*100)+"\\%",color=RED).scale(0.618).next_to([px,py,pz],UP,buff=0.2)
            for [px,py,pz],coords in zip(points2,coords2)])
        
        axes.lines_x_axis=VGroup()
        axes.lines_y_axis=VGroup()
        x_p=[x for x in np.arange(*axes.x_range)]
        y_p=[x for x in np.arange(*axes.y_range)]
        for x_point in list(zip(x_p, [axes.y_axis.x_max]*len(x_p), [0]*len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point),color=GREY_D))
        for y_point in list(zip([axes.x_axis.x_max]*len(y_p), y_p, [0]*len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point),color=GREY_D))
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.add(axes.lines_x_axis[1:],axes.lines_y_axis[1:],axes,x_label,y_label)
        text1.next_to(graph1,RIGHT).shift(LEFT+UP*0.2)
        text2.next_to(graph2,RIGHT).shift(LEFT+DOWN*0.2)
        self.play(
                Write(title),
                ShowCreation(graph1),
                ShowCreation(dots1),
                ShowCreation(p1),
                ShowCreation(graph2),
                ShowCreation(dots2),
                ShowCreation(p2),
                GrowFromCenter(text1),
                GrowFromCenter(text2),
                run_time=4,
                )
        self.wait(3)

class CustomGraph6(Scene):
    def construct(self):
        axes = Axes(
            (0,7,1), 
            (0,1.1,0.2,),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 4,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                "include_tip":True,},
            y_axis_config={ 
                "decimal_number_config": {
                    "num_decimal_places": 2,
                },
            },
            )
        
        axes.add_coordinate_labels()
        axes.scale(0.86)
        
        x_label = Text("进球数",font="思源黑体").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("概率",font="思源黑体").next_to(axes.y_axis.get_corner(UR),RIGHT)
        
        # Get coords
        title = Text("偶数个进球情况",font="思源黑体",font_size=60)
        title.to_corner(UP)
        text1 = Text("日本队获胜",font="思源黑体",font_size=36)
        text2 = Text("德国队获胜",font="思源黑体",font_size=36,color=RED)
        textm = Text("平局",font="思源黑体",font_size=36,color=YELLOW)
        coords1 = [
            [0,0],
            [2,0.09],
            [4,0.08],
            [6,0.07],
            ]
        coords2 = [
            [0,0],
            [2,0.49],
            [4,0.65],
            [6,0.74]
            ]
        coordsm = [
            [0,1],
            [2,0.42],
            [4,0.27],
            [6,0.19]
        ]
        
        points1 = [axes.c2p(px,py) for px,py in coords1]
        points2 = [axes.c2p(px,py) for px,py in coords2]
        pointsm = [axes.c2p(px,py) for px,py in coordsm]
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points1,color=WHITE,stroke_width=10)
        graph2 = DiscreteGraphFromSetPoints(points2,color=RED,stroke_width=10)
        graphm = DiscreteGraphFromSetPoints(pointsm,color=YELLOW,stroke_width=10)
        
        # Set dots
        dots1 = VGroup(*[
            Dot(radius=0.1,color=WHITE).move_to([px,py,pz])
            for px,py,pz in points1])
        
        p1=VGroup()
        for i,([px,py,pz],coords) in enumerate(zip(points1,coords1)):
            if i==0:
                direct = DL
            else:
                direct = UP
            tex1 = Tex(str(round(coords[1]*100,2))+"\\%",color=WHITE).scale(0.618).next_to([px,py,pz],direct,buff=0.2)
            p1.add(tex1)
        
        dots2 = VGroup(*[
            Dot(radius=0.1,color=RED).move_to([px,py,pz])
            for px,py,pz in points2])
        
        p2=VGroup()
        for i,([px,py,pz],coords) in enumerate(zip(points2,coords2)):
            if i==0:
                direct = UL
            else:
                direct = UP
            tex2 = Tex(str(round(coords[1]*100,2))+"\\%",color=RED).scale(0.618).next_to([px,py,pz],direct,buff=0.2)
            p2.add(tex2)
        
        dotsm = VGroup(*[
            Dot(radius=0.1,color=YELLOW).move_to([px,py,pz])
            for px,py,pz in pointsm])
        
        pm=VGroup()
        for i,([px,py,pz],coords) in enumerate(zip(pointsm,coordsm)):
            if i==0 or i==1:
                direct = RIGHT
            else:
                direct = UP
            texm = Tex(str(round(coords[1]*100,2))+"\\%",color=YELLOW).scale(0.618).next_to([px,py,pz],direct,buff=0.2)
            if i==1:
                texm.shift(UP*0.22)
            pm.add(texm)
        
        axes.lines_x_axis=VGroup()
        axes.lines_y_axis=VGroup()
        x_p=[x for x in np.arange(*axes.x_range)]
        y_p=[y for y in np.arange(*axes.y_range)]
        for x_point in list(zip(x_p, [axes.y_axis.x_max]*len(x_p), [0]*len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point),color=GREY_D))
        for y_point in list(zip([axes.x_axis.x_max]*len(y_p), y_p, [0]*len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point),color=GREY_D))
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        # self.add(axes,x_label,y_label)
        self.add(axes.lines_x_axis[1:],axes.lines_y_axis[1:],axes,x_label,y_label)
        text1.next_to(graph1.get_points()[2],UP,buff=0.55)
        text2.next_to(graph2.get_points()[-1],UP,buff=0.55)
        textm.next_to(graphm.get_points()[-1],UP,buff=0.55)
        self.add(text1,text2,textm,title)
        self.play(
                Write(title),
                GrowFromCenter(text1),
                GrowFromCenter(text2),
                GrowFromCenter(textm),
                ShowCreation(graph1),
                ShowCreation(dots1),
                ShowCreation(p1),
                ShowCreation(p2),
                ShowCreation(pm),
                ShowCreation(graph2),
                ShowCreation(dots2),
                ShowCreation(dotsm),
                ShowCreation(graphm),
                run_time=4,
                )
        self.wait(3)

class Property1(Scene):
    def construct(self):
        def gen_imgs(text, list_n, row, col, tex=None, x_buff = 1.1, y_buff = 1.2, scl_boat=0.86):
            objs = []
            for lin in list_n:
                if lin == 1:
                    obj = ImageMobject("日本进球",height=1)
                if lin == 0:
                    obj = ImageMobject("德国进球",height=1)
                objs.append(obj)
                
            for i in range(row):
                for j in range(col):
                    objs[i*col+j].move_to(np.array([j*x_buff,i*y_buff,0]))
            
            objvg = Group(*objs).scale(scl_boat)
            txt = Text(text,font_size=70).next_to(objvg,LEFT,buff=MED_LARGE_BUFF)
            
            if tex is not None:
                brace = Brace(objvg,RIGHT)
                brace_text = brace.get_tex(tex)
                return Group(txt, *objs, brace, brace_text)
            else:
                return Group(*objs)
            
        list_110 = [1]        
        obj_110 = gen_imgs("1:0", list_110, 1 , 1, tex="P=30\\%")
        title1 = Text(
                    "总进球数是1个 日本获胜的概率",
                    font="思源黑体",
                    font_size=50,
                    t2c={"1": RED} 
                ).to_edge(UP)
        
        list_330 = [1,1,1]
        obj_330 = gen_imgs("3:0", list_330, 1 , 3, tex="P_1=(30\\%)^3=2.7\\%")
        
        title3 = Text(
                    "总进球数是3个 日本获胜的概率",
                    font="思源黑体",
                    font_size=50,
                    t2c={"3": RED} 
                ).to_edge(UP)
        
        list_321 = [
                1,0,1,
                0,1,1,
                1,1,0,
                ]
        obj_321 = gen_imgs("2:1", list_321, 3 , 3, tex="P_2=3\\times(30\\%)^2\\times 70 \\%=18.9\\%")
        Group(obj_330,obj_321).arrange(DOWN,buff=0.6,aligned_edge=LEFT).center().scale(0.8).shift(UP*0.36)
        
        P3_tex = Tex("P = P_1+P_2 = 21.6 \\%",font_size=55).next_to(obj_321,DOWN,buff=MED_LARGE_BUFF)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)

        self.play(Write(title1))
        self.play(FadeIn(obj_110[0],scale=0.5))
        self.play(*[FadeIn(ob,scale=0.8) for ob in obj_110[1:]])
        self.wait()        
        
        self.remove(*obj_110)
        
        self.play(ReplacementTransform(title1,title3))
        self.play(FadeIn(obj_330[0],scale=0.5))
        self.play(*[FadeIn(ob,scale=0.8) for ob in obj_330[1:]])
        self.wait()

        self.play(FadeIn(obj_321[0],shift=UP))
        self.play(*[FadeIn(ob,shift=UP) for ob in obj_321[1:-2]])
        self.play(*[FadeIn(ob,shift=LEFT) for ob in obj_321[-2:]])
        self.wait()
        self.play(Write(P3_tex))
        self.wait(3)
        
        self.remove(*obj_330,*obj_321,P3_tex)
        
        title5 = Text(
                    "总进球数是5个 日本获胜的概率",
                    font="思源黑体",
                    font_size=50,
                    t2c={"5": RED} 
                ).to_edge(UP)
        
        self.play(ReplacementTransform(title3,title5))
        
        scale_boat = 0.6
        list_550 = [1,1,1,1,1]
        obj_550 = gen_imgs("5:0", list_550, 1 , 5, tex="P_1=(30\\%)^5=0.243\\%", scl_boat=scale_boat)
        
        list_541 = [
                1,1,1,1,0,
                1,1,1,0,1, 
                1,1,0,1,1, 
                1,0,1,1,1, 
                0,1,1,1,1, 
                ]
        obj_541 = gen_imgs("4:1", list_541, 5 , 5, tex="P_2=5\\times (30\\%)^4\\times 70 \\%=2.835\\%", scl_boat=scale_boat)
        
        
        list_532_1 = [
                1,1,1,0,0,
                1,1,0,1,0, 
                1,0,1,1,0, 
                0,1,1,1,0, 
                1,1,0,0,1, 
                ]
        list_532_2 = [
                1,0,1,0,1,
                0,1,1,0,1, 
                1,0,0,1,1, 
                0,1,0,1,1, 
                0,0,1,1,1, 
                ]
        
        obj_532_1 = gen_imgs("3:2", list_532_1, 5 , 5, tex=None, scl_boat=scale_boat)
        obj_532_2 = gen_imgs("3:2", list_532_2, 5 , 5, tex=None, scl_boat=scale_boat)
        obj_532 = Group(obj_532_1, obj_532_2).arrange(LEFT,buff=0.5,aligned_edge=UP).center().shift(UP*0.8)
        
        txt_532 = Text("3:2",font_size=70).next_to(obj_532,LEFT,buff=MED_LARGE_BUFF)
        brace532 = Brace(obj_532,RIGHT)
        brace532_text = brace532.get_tex("P_3=10\\times(30\\%)^3 \\times (70\\%) ^2=13.23\\%")
        obj_532.add(txt_532, brace532, brace532_text)
        
        obj_5 = Group(obj_550,obj_541,obj_532).arrange(DOWN,buff=0.5,aligned_edge=LEFT).center().scale(0.6).shift(UP*0.1)
        
        P5_tex = Tex("P = P_1+P_2+P_3 = 16.308 \\%",font_size=36).next_to(obj_5,DOWN,buff=MED_SMALL_BUFF)
        
        self.play(*[FadeIn(ob,scale=0.8) for ob in obj_550])
        self.play(*[FadeIn(ob,scale=0.8) for ob in obj_541[0:-2]])
        self.wait()
        self.play(*[FadeIn(ob,shift=LEFT) for ob in obj_541[-2:]])
        self.wait()
        self.play(FadeIn(txt_532,scale=0.8),
                  *[FadeIn(ob,scale=0.8) for ob in obj_532_1],
                  *[FadeIn(ob,scale=0.8) for ob in obj_532_2],)
        self.play(
                  FadeIn(brace532,shift=LEFT),
                  FadeIn(brace532_text,shift=LEFT),
                  )
        self.wait()
        self.play(Write(P5_tex))
        
        self.wait(5)

class BarChartRectangle(VGroup):
    CONFIG = {
        "stroke_opacity":0.8,
        "fill_opacity":0.5,
    }
    def __init__(self, axes, coords, width, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.graph_origin_y = axes.x_axis.number_to_point(0)[1]
        self.axes = axes
        points_zero = [axes.c2p(px,1e-3) for px,py in coords]
        for point in points_zero:
            bar = Rectangle(
                height = abs(point[1]-self.graph_origin_y),
                width = width,
                stroke_opacity = self.stroke_opacity,
                fill_opacity = self.fill_opacity,
            )
            bar.next_to(np.array(point),DOWN,buff=0)
            self.add(bar)
        self.change_bar_values(coords)
            
    def change_bar_values(self, coords) -> None:
        points = [self.axes.c2p(px,py) for px,py in coords]
        for bar, value in zip(self, points):
            bar_bottom = bar.get_bottom()
            bar_top = bar.get_top()
            bar_height = value[1]-self.graph_origin_y
            if bar_top[1]>=bar_bottom[1]:
                bar.stretch_to_fit_height(bar_height)
                bar.move_to(bar_bottom, DOWN)
            else:
                bar.stretch_to_fit_height(-bar_height)
                bar.move_to(bar_bottom, DOWN)


class PlotBarChart1(Scene):
    def construct(self):
        axes = Axes(
            (0,8,1), 
            (0,30,5,),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 4,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                "include_tip":True,
                "numbers_to_exclude": None,
                },
            y_axis_config={ 
                "decimal_number_config": {
                    "num_decimal_places": 2,
                },
            },
        )
        
        axes.add_coordinate_labels()
        axes.scale(0.86)
        x_label = Text("x",font="思源黑体").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("y",font="思源黑体").next_to(axes.y_axis.get_corner(UR),RIGHT)
        
        x = [1, 2, 3, 4,  5,  6, 7]
        y = [2, 4, 6, 8, 10, 20, 25]

        coords = [[px,py] for px,py in zip(x,y)]
        points = [axes.c2p(px,py) for px,py in coords]
        bars = BarChartRectangle(axes, points, 0.618)
        bars.set_color_by_gradient(BLUE, YELLOW)
        self.add(axes,x_label,y_label)
        self.play(
            LaggedStart(
                *[FadeIn(bar) for bar in bars], 
            lag_ratio = 0.1618,
            run_time = 2
        ))
        self.wait()

class PlotBarChart2(Scene):
    def construct(self):
        axes = Axes(
            (0,8,1), 
            (-10,30,5,),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 4,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                    },
                "include_tip":True,
                "numbers_to_exclude": [0],
                },
            y_axis_config={ 
                "decimal_number_config": {
                    "num_decimal_places": 0,
                },
            },
        )
        
        axes.add_coordinate_labels()
        axes.scale(0.86)
        x_label = Text("x",font="思源黑体").next_to(axes.x_axis.get_corner(UR),UP)
        y_label = Text("y",font="思源黑体").next_to(axes.y_axis.get_corner(UR),RIGHT)
    
        x0 = [1, 2, 3, 4,  5,  6, 7 ]
        
        y0 = [1e-3] * len(x0)
        y1 = [-4, 2, -5, 10, 10, 2, 25]
        y2 = [dy-6 for dy in y1]
        y3 = [dy-2 for dy in y2]
        y4 = [dy+8 for dy in y3]

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        coords1 = [[px,py] for px,py in zip(x0,y1)]
        coords2 = [[px,py] for px,py in zip(x0,y2)]
        coords3 = [[px,py] for px,py in zip(x0,y3)]
        coords4 = [[px,py] for px,py in zip(x0,y4)]
        
        bars = BarChartRectangle(axes, coords0, 0.618)
        bars.set_color_by_gradient(YELLOW, RED)

        self.add(bars)
        self.add(axes, x_label, y_label, bars)
        self.play(bars.animate.change_bar_values(coords1))
        self.play(bars.animate.change_bar_values(coords2))
        self.play(bars.animate.change_bar_values(coords3))
        self.play(bars.animate.change_bar_values(coords4))
        self.wait()
        
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} PlotBarChart2 -o".format(__file__))