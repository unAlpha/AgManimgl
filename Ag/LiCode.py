# -*- coding: utf-8 -*-
from calendar import day_abbr
from math import radians
from cv2 import add
from matplotlib.pyplot import pink, title
from sympy import Add, RisingFactorial
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
        curve.set_points_smoothly(coords,true_smooth=True)
        curve.set_style(stroke_width=8)
        tan_line_and_vector_and_circle = self.curvature_vector(curve, vlu.get_value())
        tan_line_and_vector_and_circle.add_updater(
                lambda mob: mob.become(self.curvature_vector(curve, vlu.get_value()))
            )
        self.add(curve, tan_line_and_vector_and_circle)
        self.play(
                vlu.set_value, 0.98,
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
        NumX = Text("（质数）",color=RED,font_size=40).next_to(PTVg,RIGHT)
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
        "legend_scale" : 0.5,
        "scale_k" : 1,
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
        
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} Graph1 -o --hd".format(__file__))