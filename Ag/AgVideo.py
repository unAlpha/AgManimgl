# -*- coding: utf-8 -*-
from manimlib import *

class Time1(Scene):
    Q = """
        \\parbox{6cm}{
            Phalaenopsis orchids, three petals unfolded, super clear --v 5 --q 2
            }
        """
    Ans = """
        \\parbox{6cm}{
            蝴蝶兰，三片花瓣展开，超清晰
            }
        """
    Pos = 0
    f = 28
    def construct(self):
        prompt = Text("关键词",color=RED,font = '阿里巴巴普惠体 2.0',font_size=40,)
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        pq = VGroup(prompt,question).arrange(DOWN,aligned_edge=LEFT,buff=0.25)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        translate = Text("翻译",color=GREY,font = '阿里巴巴普惠体 2.0',font_size=40,)
        at = VGroup(translate,answer).arrange(DOWN,aligned_edge=LEFT,buff=0.25)
        VGroup(pq,at).arrange(DOWN,aligned_edge=LEFT,buff=0.5).center().to_edge(LEFT).shift(UP*0.2)
        
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(pq,shift=RIGHT),
            )
        self.wait(2)
        self.play(
            FadeIn(translate),
            ShowIncreasingSubsets(*answer),
            run_time=3,
            ) 
        self.wait(3)


class Time2(Scene):
    Q = ["""
        \\parbox{6cm}{
            Roses, three petals fully expanded, plan view, super clear --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose, only three petals, fully unfolded, flat spread, super clear --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose petal --stop 50 --v 5 --q 2
            }
        """,  
        """
        \\parbox{6cm}{
            A rose petal, flat unfolded, specific --stop 50 --v 5 --q 2
            }
        """,          
        """
        \\parbox{6cm}{
            A rose petal, flat unfolded onto a plain white tabletop, top view --stop 50 --v 5 --q 2
            }
        """,    
        """
        \\parbox{6cm}{
            Three rose petals, flat unfolded onto a plain white table, petals not overlapping each other, top view --stop 50 --v 5 --q 2
            }
        """,  
        """
        \\parbox{6cm}{
            Two rose petals, flat unfolded onto a plain white table, petals do not overlap each other, symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,  
        """
        \\parbox{6cm}{
            There are and only two rose petals unfolded to a pure white tabletop, the same size between each petal, the same color, the petals do not overlap each other, no folds in the petals, no bending of the petals, 360 degrees symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,  
        """
        \\parbox{6cm}{
            There are and only two rose petals unfolded to a pure white tabletop, petals do not overlap each other, petals are not folded, petals are not bent, 360 degrees symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,  
        ]
    Ans = ["""
        \\parbox{6cm}{
            玫瑰花，三片花瓣完全展开，平面图，超级清晰
            }
        """,
        """
        \\parbox{6cm}{
            一朵玫瑰，只有三片花瓣，完全展开，平铺，超级清晰
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣，平铺，特写
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣，平铺在白色的桌面上，俯视图
            }
        """,
        """
        \\parbox{6cm}{
            三片玫瑰花瓣，平铺在白色的桌子上，花瓣之间没有重叠，俯视图
            }
        """,
        """
        \\parbox{6cm}{
            两片玫瑰花瓣，平铺在白色的桌子上，花瓣没有相互重叠，对称放置，俯视，特写
            }
        """,
        """
        \\parbox{6cm}{
            有且仅有两片玫瑰花瓣展开在纯白的桌面上，每片花瓣之间大小相同，颜色相同，花瓣之间没有重叠，花瓣没有褶皱，花瓣没有弯曲，360度对称放置，俯视，特写
            }
        """,
        """
        \\parbox{6cm}{
            有且仅有两片玫瑰花瓣展开在纯白的桌面上，花瓣没有相互重叠，花瓣没有折叠，花瓣没有弯曲，360度对称放置，俯视，特写
            }
        """,
        ]
    Pos = 0
    f = 28
    def construct(self):
        VGpqat = VGroup()
        for i in range(9):
            prompt = Text("关键词",color=RED,font = '阿里巴巴普惠体 2.0',font_size=40,)
            question = TexText(self.Q[i], font_size=self.f,alignment="\\raggedright")
            pq = VGroup(prompt,question).arrange(DOWN,aligned_edge=LEFT,buff=0.25)
            answer= TexText(self.Ans[i], color=YELLOW, font_size=self.f, alignment="\\raggedright")
            translate = Text("翻译",color=GREY,font = '阿里巴巴普惠体 2.0',font_size=40,)
            at = VGroup(translate,answer).arrange(DOWN,aligned_edge=LEFT,buff=0.25)
            VGpqat.add(VGroup(pq,at).arrange(DOWN,aligned_edge=LEFT,buff=0.5).center().to_edge(LEFT).shift(UP*0.2))
            
            # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
            # self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(VGpqat[0][0],shift=RIGHT),
            )
        self.wait(2)
        self.play(
            FadeIn(VGpqat[0][1][0]),
            ShowIncreasingSubsets(*VGpqat[0][1][1]),
            run_time=3,
            ) 
        self.wait(3)
        for j in range(1,9):
            print(j)
            self.play(
                ReplacementTransform(VGpqat[j-1],VGpqat[j])
            )
            self.wait(3)
       
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} Time1 -ot -r 2048x1152".format(__file__))