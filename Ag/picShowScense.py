from Ag.imports_ag import *

class pic1(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "pics/15 伯恩哈德·黎曼",
                        "Bernhard Riemann",
                        "伯恩哈德·黎曼",
            )
        palyALL(self,allParts)

class pic2(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "pics/21 可乐",
                        "可展曲面设计的产品",
            )
        palyALL(self,allParts)

class Music8(Scene):
    def construct(self):
        img = ImageMobject("pic/茱莉亚学院",height=FRAME_HEIGHT)
        self.add(img)
        introduction(
            self,
            name_ch = "茱莉亚学院",
            name_eng = "The Juilliard School",
            bir = "成立于1905年",
            intro = "世界顶级的表演艺术学校之一",
            )

class Music10(Scene):
    def construct(self):
        introduction(
            self,
            name_ch = "西方音乐之父巴赫在弹风琴（钢琴前身）",
            )

