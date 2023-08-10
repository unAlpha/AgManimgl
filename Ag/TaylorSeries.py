from manimlib import *

def derivative(func, x, n = 1, dx = 0.05):
    samples = [func(x + (k - n/2)*dx) for k in range(n+1)]
    while len(samples) > 1:
        samples = [
            (s_plus_dx - s)/dx
            for s, s_plus_dx in zip(samples, samples[1:])
        ]
    return samples[0]

def taylor_approximation(func, highest_term, center_point = 0):
    derivatives = [
        derivative(func, center_point, n = n)
        for n in range(highest_term + 1)
    ]
    coefficients = [
        d/math.factorial(n) 
        for n, d in enumerate(derivatives)
    ]
    return lambda x : sum([
        c*((x-center_point)**n) 
        for n, c in enumerate(coefficients)
    ])

class Ex(Scene):
    CONFIG = {
        "x_range" : (-2,2),
        "y_range" : (-1,3),
        "function" : lambda x : np.exp(x),
        "function_tex" : "e^{x}",
        "function_color" : BLUE,
        "order_sequence" : [0, 1, 2, 3, 4],
        "center_point" : 0,
        "approximation_terms" : ["\\approx 1", "+x", "+\\frac{x^2}{2!}","+\\frac{x^3}{3!}","+ ..."],
        "approximation_color" : GREEN,
        "gap_time" : 1,
    }

    def construct(self):
        axes = Axes(self.x_range, self.y_range)
        axes.add_coordinate_labels()
        func_graph = axes.get_graph(
            self.function,
            color=self.function_color,)
        approx_graphs = [
            axes.get_graph(
                taylor_approximation(self.function, n),
                color=self.approximation_color)
            for n in self.order_sequence]

        near_text = TexText(
            "\\text{在} $x=%d$ \\text{处展开}"%self.center_point,
            font_size = 30)
        near_text.to_corner(DR,buff=1)
        # near_text.add_background_rectangle(opacity = 0.2)
        equation = Tex(
            self.function_tex,
            *self.approximation_terms,
            font_size = 40,)
        equation.to_corner(UP,buff=0.2)
        equation.set_color_by_tex(
            self.function_tex, self.function_color,
            substring = False)
  
        approx_graph = VectorizedPoint(
            axes.i2gp(self.center_point, func_graph))
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        eqcho = equation[:1].copy()
        self.play(Write(axes))
        self.play(
            ShowCreation(func_graph, run_time = 2),
            Write(eqcho),
            Write(near_text),)
        for graph, term in zip(approx_graphs, equation[1:]):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                TransformMatchingShapes(eqcho, VGroup(eqcho,term)),
                # Write(term),
                )
            self.wait(self.gap_time)
        self.wait(2)

class Sinx1(Scene):
    CONFIG = {
        "x_range" : (-4, 4),
        "y_range" : (-2, 2),
        "function" : lambda x : np.sin(x),
        "function_tex" : "sin(x)", 
        "function_color" : BLUE,
        "order_sequence" : [1, 3, 5, 7, 9],
        "center_point" : 0,
        "approximation_terms" : [
            "\\approx x", 
            "-\\frac{1}{6} x^3", 
            "+\\frac{1}{120} x^5",
            "-\\frac{1}{5040} x^7",
            "+ ...",
        ],
        "approximation_color" : WHITE,
        "showRange" : True,
        "gap_time" : 1,
    }

    def construct(self):
        axes = Axes(self.x_range, self.y_range,height=FRAME_HEIGHT-2.5)
        # axes.add_coordinate_labels()
        func_graph = axes.get_graph(
            self.function,
            color=self.function_color,)
        approx_graphs = [
            axes.get_graph(
                taylor_approximation(self.function, n),
                color=self.approximation_color)
            for n in self.order_sequence
        ]

        near_text = TexText(
            "\\text{在} $x=%d$ \\text{处展开}"%self.center_point,
            font_size = 30)
        near_text.to_corner(DR,buff=2)
        # near_text.add_background_rectangle(opacity = 0.2)
        equation = Tex(
            self.function_tex,
            *self.approximation_terms,
            font_size = 40,)
       
        equation.set_color_by_tex(
            self.function_tex, self.function_color,
            substring = False)
  
        approx_graph = VectorizedPoint(
            axes.i2gp(self.center_point, func_graph))

        equation.to_corner(UP,buff=0.2)
        eqcho = equation[:1]
        self.camera.frame.save_state()
        self.camera.frame.scale(0.3).move_to(eqcho),
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        
        self.play(Write(eqcho),run_time = 2)
        
        self.wait()
        self.play(Restore(self.camera.frame))

        axes.lines_x_axis=VGroup()
        axes.lines_y_axis=VGroup()
        x_p=[x for x in np.arange(*axes.x_range)]
        x_p.append(axes.x_axis.x_max)
        y_p=[x for x in np.arange(*axes.y_range)]
        y_p.append(axes.y_axis.x_max)
        for x_point in list(zip(x_p, [axes.y_axis.x_max]*len(x_p), [0]*len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point),color=GREY_D))  
        for x_point in list(zip(x_p, [-axes.y_axis.x_max]*len(x_p), [0]*len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point),color=GREY_D))        
        for y_point in list(zip([axes.x_axis.x_max]*len(y_p), y_p, [0]*len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point),color=GREY_D))
        for y_point in list(zip([-axes.x_axis.x_max]*len(y_p), y_p, [0]*len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point),color=GREY_D)) 
        
        axes.add_coordinate_labels()
        self.add(axes.lines_x_axis,axes.lines_y_axis),
        self.play(
            Write(axes),
            ShowCreation(func_graph, run_time = 2),
            Write(near_text),)
        
        for graph, term in zip(approx_graphs[0:2], equation[1:3]):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Write(term),
                )
            self.wait(self.gap_time)
        if self.showRange==True:    
            self.camera.frame.save_state() 
            self.play(self.camera.frame.animate.scale(0.76))   

        self.wait()
        self.play(Restore(self.camera.frame))
        for graph, term in zip(approx_graphs[2:], equation[3:]):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Write(term),
                )
            self.wait(self.gap_time)            
            
        self.wait(2)

class Cos(Ex):
    CONFIG = {
        "x_range" : (-2*np.pi, 2*np.pi, np.pi),
        "y_range" : (-2, 2),
        "function" : lambda x : np.cos(x),
        "function_tex" : "cos(x)", 
        "function_color" : BLUE,
        "order_sequence" : [0,2,4,6,8],
        "center_point" : 0,
        "approximation_terms" : [
            "\\approx 1", 
            "-\\frac{1}{2 !} x^2", 
            "+\\frac{1}{4 !} x^4",
            "-\\frac{1}{6 !} x^6",
            "+ ...",
        ],
        "approximation_color" : WHITE,
        "gap_time" : 0.5,
    }

class XoneX(Ex):
    CONFIG = {
        "x_range" : (-2, 2, 1),
        "y_range" : (-1, 1),
        "function" : lambda x : x/math.pow((1-x),2),
        "function_tex" : "\\frac{x}{(1-x)^2}", 
        "function_color" : BLUE,
        "order_sequence" : [1,2,3,4,5,6,7],
        "center_point" : 0,
        "approximation_terms" : [
            "\\approx x", 
            "+2x^2", 
            "+3x^3",
            "+4x^4",
            "+5x^5",
            "+6x^6",
            "+7x^7",
        ],
        "approximation_color" : WHITE,
        "gap_time" : 0.5,
    }

class Sinx2(Scene):
    def construct(self):
        tex11 = Tex("\\sin x=x-\\frac{x^{3}}{3 !}+\\frac{x^{5}}{5 !}-\\frac{x^{7}}{7 !}+\\ldots",
                    font ='SimSun',
                    font_size=60
            ).shift(0.5*UP)
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        
        self.play(ShowCreation(tex11))
        self.play(FlashAround(tex11))
        self.wait(1)
        
        Ar = [[np.array([2,-1.5,0]), BLUE, [11,17,23],BOTTOM,"(2n+1) !",DOWN],
              [np.array([1.5,2.5,0]), GREEN, [8,14,20],TOP,"x^{(2n+1)} ",UP],
              [np.array([-1,-1.5,0]), RED, [5,6,12,18],BOTTOM,"(-1)^{n}",DOWN],
              ]
        arGorup = VGroup()
        texGroup = VGroup()
        for arr in Ar:
            # 在这里创建箭头对象
            arstart = arr[0]
            dot = Dot(arstart,color = arr[1])
            argr = VGroup(dot)
            for loc in arr[2]:
                ar = Arrow(start=arstart, end=tex11[0][loc].get_corner(arr[3]), color = arr[1], buff=0.05)
                argr.add(ar)
                
            ttex = Tex(arr[4]).next_to(dot,arr[5],buff=0.1)
            
            arGorup.add(argr)
            texGroup.add(ttex)
        # 显示箭头
        for i in range(len(arGorup)):
            self.play(
                ShowCreation(arGorup[i]),
                ShowCreation(texGroup[i]),
                run_time=3   
                    )
            self.wait()
            
        tex12 = Tex(r"\sin x=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2 n+1) !} x^{2 n+1}",
                    font ='SimSun',
                    font_size=60
            ).shift(0.5*UP)
        tex1g = VGroup(tex11,arGorup,texGroup)
        self.play(tex1g.animate.scale(0.5).to_corner(UP))
        tex12.next_to(tex11,DOWN,buff=1.5)
        rect = SurroundingRectangle(tex12,buff=0.2)
        self.play(
            Write(tex12),
            ShowCreation(rect),
            )
        self.wait()
        
        self.play(
            *map(FadeOut,[tex12,rect,texGroup,arGorup]),
        )
        tex1 = Tex(r" \sin x=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2 n+1) !} x^{2 n+1} =x-\frac{x^{3}}{3 !}+\frac{x^{5}}{5 !}-\frac{x^{7}}{7 !}+\ldots",
                    font ='SimSun',
                    font_size=60).scale(0.618).to_corner(UP,buff=1.2)
        self.play(Transform(tex11,tex1))
        self.wait()
        
        tex2 = Tex(r"\cos x=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2 n) !} x^{2 n} =1-\frac{x^{2}}{2 !}+\frac{x^{4}}{4 !}-\cdots \quad \forall x",
                    font ='SimSun',
                    font_size=60).scale(0.618).next_to(tex1,DOWN,buff=0.8)
        self.play(ShowCreation(tex2),)
        self.wait()

        tex3 = Tex(r"e^{x}=\sum_{n=0}^{\infty} \frac{x^{n}}{n !}=1+x+\frac{x^{2}}{2 !}+\frac{x^{3}}{3 !}+\cdots+\frac{x^{n}}{n !}+\cdots \quad \forall x \quad \text { (对所有x都成立) }",
                    font ='SimSun',
                    font_size=60).scale(0.618).next_to(tex2,DOWN,buff=0.8)
        self.play(ShowCreation(tex3))
        self.wait()

class TexTaylor(Scene):
    def construct(self):
        tex1 = Tex("f(x)", font='SimSun', font_size=100)
        list_text = [
            ["假设 :", r"f(x)=a_0+a_1x+a_2x^2+a_3x^3+...","(1)"],
            ["取$x=0$:", r"f(0)=a_0+a_1\times0+a_2\times0^2+a_3\times0^3+a_4\times0^4..."],
            ["所以：",r"a_0=f(0)"],
            ["(1)式两边求导:",r"f^{\prime}(x)=0+a_1+2a_2x+3a_3x^2+4a_4x^3...","(2)"],
            ["取$x=0$:",r"f^{\prime}(0)=0+a_1+2a_2\times0+3a_3\times0^2+4a_4\times0^3..."],
            ["所以：",r"a_1=f^{\prime}(0)"],
            ["(2)式两边求导:",r"f^{\prime\prime}(x)=0+0+2a_2+2\times3a_3x+3\times4a_4x^2...","(3)"],
            ["取$x=0$:",r"f^{\prime\prime}(0)=0+0+2a_2+2\times3a_3\times0+3\times4a_4\times0^2..."],
            ["所以：",r"a_2=\frac12f^{\prime\prime}(0)"],
            ["... ..."],
            ["观察规律得：",r"a_n=\frac1{n!}f^{(n)}(0)"],
            ["泰勒展开：",r"f(x)=f(0)+\frac{f^{\prime}(0)}{1!}x+\frac{f^{\prime\prime}(0)}{2!}x^2+\frac{f^{\prime\prime}(0)}{3!}x^3+...=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n"],
        ]
        GTexs = VGroup()
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        self.play(Write(tex1))
        self.wait()
        for text in list_text:
            GTex = VGroup()
            if len(text)==1:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                GTex.add(text_obj.move_to(ORIGIN))
            if len(text)>=2:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                tex_obj = Tex(text[1], font='SimSun', font_size=30)
                GTex.add(text_obj.next_to(ORIGIN, LEFT,buff=0.1))
                GTex.add(tex_obj.next_to(ORIGIN, RIGHT,buff=0.1))
            if len(text)>=3:
                textmp = Tex(text[2], font='SimSun', font_size=30)
                textmp.next_to(ORIGIN, RIGHT,buff=8)
                GTex.add(textmp)
                
            GTexs.add(GTex)
        
        GTexs.arrange(
                DOWN,
                buff=0.3,
                coor_mask=np.array([0, 1, 0])
            )
    
        for i in range(len(GTexs)):
            GTexs[i].move_to(ORIGIN, coor_mask=np.array([0, 1, 0]))  # initially set the legend to the center
            GTexs[i].scale(1.2).set_color(YELLOW)
            # if it's not the first item, move all previous items up
            if i > 0 and i<len(GTexs)-1:
                self.play(
                    GTexs[i-1].animate.shift(UP * 1).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            elif i==0:
                self.play(
                    ReplacementTransform(tex1,GTexs[i]),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            # self.wait()
            elif i==len(GTexs)-1:
                GTexs[i].center()
                self.play(
                    GTexs[i-1].animate.shift(UP * 1.236).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN*0.5),
                    FlashAround(GTexs[i],color = RED,run_time=1.8)
                    )
            self.wait()

        self.play(
            FadeOut(GTexs[:i]),
            GTexs[i].animate.center().shift(UP).set_color(WHITE)
        )
        self.wait()
        text_ = TexText("在$x=0$处的泰勒展开式", font='SimSun', font_size=30)
        text_.next_to(GTexs[i],DOWN)
        self.play(
            Write(text_)
        )
        
        self.wait(2)

class TexTaylorEx(Scene):
    CONFIG = {
        "fx" : "f(x)=e^x",
        "texts" :  [
            ["指数函数特点", r"f(x)=f’(x)=f’’(x)=...=f^{(n)}(x)=e^x"],
            ["代入泰勒展开公式", r"e^x=\sum_{n=0}^\infty\frac{x^n}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots+\frac{x^n}{n!}+\cdots\quad\forall x"],
        ],
        "coor_mask": np.array([0, 1, 0])
    }    
    def construct(self):
        tex1 = Tex(self.fx, font='SimSun', font_size=100)
        list_text = self.texts
        GTexs = VGroup()
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        self.play(Write(tex1))
        self.wait()
        for text in list_text:
            GTex = VGroup()
            if len(text)==1:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                GTex.add(text_obj.move_to(ORIGIN))
            if len(text)>=2:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                tex_obj = Tex(text[1], font='SimSun', font_size=30)
                GTex.add(text_obj.next_to(ORIGIN, LEFT,buff=0.1))
                GTex.add(tex_obj.next_to(ORIGIN, RIGHT,buff=0.1))
            if len(text)>=3:
                textmp = Tex(text[2], font='SimSun', font_size=30)
                textmp.next_to(ORIGIN, RIGHT,buff=8)
                GTex.add(textmp)
                
            GTexs.add(GTex)
        
        GTexs.arrange(
                DOWN,
                buff=0.3,
                coor_mask=np.array([0, 1, 0])
            )
    
        for i in range(len(GTexs)):
            GTexs[i].move_to(ORIGIN, coor_mask=self.coor_mask)  # initially set the legend to the center
            GTexs[i].scale(1.2).set_color(YELLOW)
            # if it's not the first item, move all previous items up
            if i > 0 and i<len(GTexs)-1:
                self.play(
                    GTexs[i-1].animate.shift(UP * 1).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            elif i==0:
                self.play(
                    ReplacementTransform(tex1,GTexs[i]),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            # self.wait()
            elif i==len(GTexs)-1:
                GTexs[i].center()
                self.play(
                    GTexs[i-1].animate.shift(UP * 1.236).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN*0.5),
                    FlashAround(GTexs[i],color = RED,run_time=1.8)
                    )
            self.wait()

        self.play(
            FadeOut(GTexs[:i]),
            GTexs[i].animate.center().shift(UP).set_color(WHITE)
        )
        self.wait()
        text_ = TexText("在$x=0$处的泰勒展开式", font='SimSun', font_size=30)
        text_.next_to(GTexs[i],DOWN,buff=MED_LARGE_BUFF)
        self.play(
            Write(text_)
        )
        
        self.wait(2)

class TexTaylorxx2(TexTaylorEx):
    CONFIG = {
        "fx" : "f(x)",
        "texts" :  [
            ["", r"f(x) = \frac x{\left(1-x\right)^2}"],
            ["代入泰勒展开公式", r"\begin{aligned}\frac x{\left(1-x\right)^2}&=x+2x^2+3x^3+4x^4+...,-1<x<1\end{aligned}"],
        ],
        "coor_mask": np.array([1, 1, 0])
    }    

class TexTaylorxx2(TexTaylorEx):
    CONFIG = {
        "fx" : "f(x)",
        "texts" :  [
            ["", r"f(x) = \frac x{\left(1-x\right)^2}"],
            ["代入泰勒展开公式", r"\begin{aligned}\frac x{\left(1-x\right)^2}&=x+2x^2+3x^3+4x^4+...,-1<x<1\end{aligned}"],
        ],
        "coor_mask": np.array([1, 1, 0])
    }    

class TexTaylorNum(Scene):
    CONFIG = {
        "texts" :  [
            ["泰勒展开式:", r"\begin{aligned}\frac x{\left(1-x\right)^2}&=x+2x^2+3x^3+4x^4+...,-1<x<1\end{aligned}",],
            ["取$x=-1$:", "-\\frac{1}{4}=-1+2-3+4-5+6...",["-\\frac{1}{4}","=","1","2","3","4","5","6","...","+","-"]],
            ["移项:", "-\\frac{1}{4}=(2+4+6+...)-(1+3+5+...)",["-\\frac{1}{4}","=","1","2","3","4","5","6","...","+","-"]],
            ["变形:", "-\\frac{1}{4}=(2+2+4+4+6+6+...)-(1+2+3+4+5+6...)",["-\\frac{1}{4}","=","1","2","3","4","5","6","...","+","-"]],
            ["合并:", "-\\frac{1}{4}=(4+8+12+...)-(1+2+3+4+5+6...)",["-\\frac{1}{4}","=","12","1","2","3","4","5","6","...","+","-","8",]],
            ["变形:", "-\\frac{1}{4}=4(1+2+3+...)-(1+2+3+4+5+6...)",["-\\frac{1}{4}","=","1","2","3","4","5","6","...","+","-"]],
            ["合并:", "-\\frac{1}{4}=3(1+2+3+...)",["-\\frac{1}{4}","=","1","2","3","4","5","6","...","+","-"]],
            ["所以:", r"1+2+3+...=-\frac{1}{12}",[]],
        ],
        "coor_mask": np.array([0, 1, 0]),
        "isoflag":False,
    }    
    def construct(self):
        list_text = self.texts
        GTexs = VGroup()
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        for text in list_text:
            GTex = VGroup()
            if len(text)<3:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                tex_obj = Tex(text[1], font='SimSun', font_size=30)
                GTex.add(text_obj.next_to(ORIGIN, LEFT,buff=0.1))
                GTex.add(tex_obj.next_to(ORIGIN, RIGHT,buff=0.1))
            if len(text)>=3:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                tex_obj = Tex(text[1],isolate=text[2], font='SimSun', font_size=30)
                GTex.add(text_obj.next_to(ORIGIN, LEFT,buff=0.1))
                GTex.add(tex_obj.next_to(ORIGIN, RIGHT,buff=0.1))
         
            GTexs.add(GTex)
        
        GTexs.arrange(
                DOWN,
                buff=0.3,
                coor_mask=np.array([0, 1, 0])
            ).shift(RIGHT*0.236)
    
        for i in range(len(GTexs)):
            if i ==0:
                GTexs[i].center().shift(0.236*UP+0.382*LEFT)  # initially set the legend to the center
                GTexs[i].scale(1.2)
            else:
                GTexs[i].move_to(ORIGIN, coor_mask=self.coor_mask)  # initially set the legend to the center
                GTexs[i].scale(1.2)
            if self.isoflag==True:
                for line in GTexs[i]:
                    line.set_color_by_tex_to_color_map({
                        "1": TEAL_E,
                        "2": GREEN_E,
                        "3": YELLOW_E,
                        "4": GOLD_E,
                        "5": RED_E,
                        "6": MAROON_E,
                        "8": PURPLE_E,
                        "-\\frac{1}{4}":WHITE,
                        "取$x=-1$:":WHITE,
                        r"\begin{aligned}\frac x{\left(1-x\right)^2}&=x+2x^2+3x^3+4x^4+...,-1<x<1\end{aligned}": WHITE,
                        r"12": WHITE,
                        r"1+2+3+...=-\frac{1}{12}":WHITE
                    })

            if i > 0 and i<len(GTexs)-1:
                if i == 1:
                    self.play(
                        GTexs[i-1].animate.shift(UP * 1).scale(1/1.2,).set_color(WHITE),
                        *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                        TransformMatchingParts(GTexs[i-1][0].copy(),GTexs[i][0]),
                        TransformMatchingParts(GTexs[i-1][1].copy(),GTexs[i][1]),
                        FlashAround(GTexs[i],color = RED,run_time=1.8),
                        run_time=2
                        ),
                else:
                    self.play(
                        GTexs[i-1].animate.shift(UP * 1).scale(1/1.2,),
                        *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                        TransformMatchingTex(GTexs[i-1][0].copy(),GTexs[i][0]),
                        TransformMatchingTex(GTexs[i-1][1].copy(),GTexs[i][1],path_arc=90 * DEGREES,),
                        run_time=2
                        ),
    
            elif i==0:
                self.play(
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN*0.5),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))    
                
            elif i==len(GTexs)-1:
                self.play(
                    GTexs[i-1].animate.shift(UP * 1).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP * 1) for legend in GTexs[:i-1]],
                    TransformMatchingParts(GTexs[i-1][0].copy(),GTexs[i][0]),
                    TransformMatchingParts(GTexs[i-1][1].copy(),GTexs[i][1]),
                    FlashAround(GTexs[i],color = RED,run_time=1.8),
                    run_time=2,
                    )
            self.wait()

        self.play(
            FadeOut(GTexs[:i]),
            GTexs[i].animate.center().scale(2).shift(UP*0.618).set_color(WHITE)
        )
        self.wait()  
        GTexs[0].next_to(GTexs[i],DOWN)
        self.play(
            FadeIn(GTexs[0],shift=UP,scale=0.618),
        )      
        self.play(
            FlashAround(GTexs[0][1][0][-6:],shift=UP,scale=0.618),
        )         
        self.wait() 

class TexTransform1(Scene):
    CONFIG={
        "tex1":"-1",
        "ios1":[],
        "tex2":"-1 = e^{(i\\pi)}",
        "ios2":["-1","=", "e^(i\\pi)"]
    }
    def construct(self):
        lines = VGroup(
            Tex(self.tex1,isolate=self.ios1),
            Tex(self.tex2,isolate=self.ios2),
        ).scale(2.618).shift(UP*0.382)
        play_kw = {"run_time": 2}
        self.add(lines[0])

        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        self.play(
            TransformMatchingTex(
                lines[0], lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

class TexTransform2(Scene):
    CONFIG={
        "tex1":"e^x",
        "ios1":["e^x"],
        "tex2":r"e^x=\sum_{n=0}^{\infty} \frac{1}{n !} x^{n}",
        "ios2":["e^x"],
        "tex3":r"e^{i \pi}=\sum_{n=0}^{\infty} \frac{(i \pi)^{n}}{n !}"
    }
    def construct(self):
        lines = VGroup(
            Tex(self.tex1,isolate=self.ios1),
            Tex(self.tex2,isolate=self.ios2),
            Tex(self.tex3),
        ).scale(1.618).shift(UP*0.382)
        play_kw = {"run_time": 2}
        self.add(lines[0])

        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        self.play(
            TransformMatchingTex(
                lines[0], lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(lines[1].animate.scale(0.618).shift(LEFT*3.75),)
        lines[2].next_to(lines[1],RIGHT, buff=2)  # Increase the buffer distance
        arr = Arrow(lines[1].get_right(), lines[2].get_left(),color=RED)
        arr_lg = TexText("$x=i\\pi$代入",font_size=28 ,color=RED).next_to(arr,UP)
        self.play(
            FadeIn(lines[2]),
            GrowArrow(arr),
            Write(arr_lg))
        
        self.wait()

class TexTaylorNum2(Scene):
    CONFIG = {
        "texts" :  [
            ["第一项是:", r"\frac{\left(i\pi\right)^0}{0!}=1",],
            ["第二项是:", r"\frac{\left(i\pi\right)^{\mathrm{l}}}{1!}=i\pi=3.14159265i"],
            ["第三项是:", r"\frac{\left(i\pi\right)^{3}}{3!}=-\frac{\pi^{3}}6i=-5.1677i"],
        ],
        "coor_mask": np.array([0, 1, 0])
    }   
    def construct(self):
        list_text = self.texts
        GTexs = VGroup()
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"],height=10)
        self.add(bg)
        for text in list_text:
            GTex = VGroup()
            if len(text)==1:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                GTex.add(text_obj.move_to(ORIGIN))
            if len(text)>=2:
                text_obj = TexText(text[0], font='SimSun', font_size=30)
                tex_obj = Tex(text[1], font='SimSun', font_size=30)
                GTex.add(text_obj.next_to(ORIGIN, LEFT,buff=0.1))
                GTex.add(tex_obj.next_to(ORIGIN, RIGHT,buff=0.1))
            if len(text)>=3:
                textmp = Tex(text[2], font='SimSun', font_size=30)
                textmp.next_to(ORIGIN, RIGHT,buff=8)
                GTex.add(textmp)
            GTexs.add(GTex)

        for i in range(len(GTexs)):
            GTexs[i].center()
            GTexs[i].scale(1.2).set_color(YELLOW)
            if i > 0 and i<len(GTexs)-1:
                self.play(
                    GTexs[i-1].animate.shift(UP *  1.236).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP *  1.236) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            elif i==0:
                self.play(
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN),
                    FlashAround(GTexs[i],color = RED,run_time=1.8))
            # self.wait()
            elif i==len(GTexs)-1:
                
                self.play(
                    GTexs[i-1].animate.shift(UP * 1.236).scale(1/1.2,).set_color(WHITE),
                    *[legend.animate.shift(UP *  1.236) for legend in GTexs[:i-1]],
                    FadeIn(GTexs[i], scale=1.5,shift=DOWN*0.5),
                    FlashAround(GTexs[i],color = RED,run_time=1.8)
                    )
            self.wait()
        self.wait()

        
        self.wait(2)        

if __name__ == "__main__":
    from os import system
    system("manimgl {} Cos -o".format(__file__))