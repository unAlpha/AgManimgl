from manimlib import *

class Music1(Scene):
    def construct(self):
        # manimpango.register_font("E:/Dropbox/manim/字体/阿里巴巴普惠体/阿里巴巴普惠体/Alibaba-PuHuiTi-Light.otf")
        # print(manimpango.list_fonts())
        text1 = Text(
            "三个层次",
            font="Source Han Sans CN",
            weight='BOLD',
            size=1.68
            )
        self.play(FadeIn(text1,scale=0.5))
        self.wait()
        
        text2 = TexText(
            "层次一 : 欣赏音乐",
            "层次二 : 自娱自乐",
            "层次三 : 玩音乐",
            )\
            .arrange(
                DOWN,
                aligned_edge=LEFT
                )
        self.remove(text1)
        self.play(Write(text2[0]))
        self.wait()
        self.play(Write(text2[1]))
        self.wait()
        self.play(Write(text2[2]))
        self.wait()

class Music2(Scene):
    def construct(self):
        # manimpango.register_font("E:/Dropbox/manim/字体/阿里巴巴普惠体/阿里巴巴普惠体/Alibaba-PuHuiTi-Light.otf")
        # print(manimpango.list_fonts())
        text1 = Text(
            "旧琴练习",
            font="Source Han Sans CN",
            weight='BOLD',
            size=1.238
            ).shift(0.238*UP)

        text2 = Text(
            "新琴练习",
            font="Source Han Sans CN",
            weight='BOLD',
            size=1.238
            ).shift(0.238*UP)

        self.play(FadeIn(text1,scale=0.5))
        self.wait()
        self.remove(text1)
        self.play(FadeIn(text2,scale=0.5))
        self.wait()
