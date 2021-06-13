from Ag.imports_ag import *

class ZeroKnowledgeProof1(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "ZeroKnowledgeProof/Shafi_Goldwasser",
                        "Shafrira Goldwasser",
                        "莎菲·戈德瓦塞尔",
            )
        palyALL(self,allParts)

class ZeroKnowledgeProof2(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "ZeroKnowledgeProof/艾维·维哥德尔森",
                        "Avi Wigderson",
                        "艾维·维哥德尔森",
            )
        palyALL(self,allParts)

class ZeroKnowledgeProof3(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "ZeroKnowledgeProof/查尔斯·拉科夫",
                        "Charles Rackoff",
                        "查尔斯·拉科夫",
            )
        palyALL(self,allParts)

class ZeroKnowledgeProof4(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "ZeroKnowledgeProof/希尔维奥·米卡利",
                        "Silvio Micali",
                        "希尔维奥·米卡利",
            )
        palyALL(self,allParts)

class ZeroKnowledgeProof5(Scene):
    def construct(self):
        allParts = ObjAndText(
                        "ZeroKnowledgeProof/姚期智",
                        "Andrew Yao",
                        "姚期智",
            )
        palyALL(self,allParts)

class suger1(Scene):
    def construct(self):
        path = r"Ag/data_files/2 代糖甜度表"
        table = Table(path)
        table.data_anim(self)
        self.wait()

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

