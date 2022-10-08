
from manimlib import *
import platform
 
sys_str = platform.system()
if sys_str == "Windows":
    Font = 'Source Han Sans CN'
elif sys_str == "Darwin":
    Font = 'Microsoft YaHei Bold'
else:
    Exception("未匹配的操作系统")

dframe=0.2
txt_height=0.3
height=4

def ObjAndText(
                Obj,
                text1,
                text2 = None,
                dframe=dframe,
                txt_height=txt_height,
                OS_font=Font,
            ):

    pic = ImageMobject(Obj)
    pic.set_height(height)

    if text2 is not None:
        picText1 = Text(text1,
                        font=OS_font,
                        color="#308032"
            )\
            .set_height(txt_height-0.068)\
            .next_to(pic,DOWN,buff=SMALL_BUFF)
        picText2 = Text(text2,
                        font=OS_font, 
                        color=BLACK,
            )\
            .set_height(txt_height)\
            .next_to(picText1,DOWN,buff=SMALL_BUFF)
        picAndText = Group(pic,picText1,picText2).center()
    else:  
        picText1=VMobject() 
        picText2 = Text(text1, 
                    font=Font,
                    color=BLACK,
        )\
        .set_height(txt_height+0.068)\
        .next_to(pic, DOWN, buff=dframe-0.06)       
        picAndText = Group(pic,picText1,picText2).center()

    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    stroke_opacity = 0,
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+dframe,
                    width=picAndText.get_width()+dframe
        )

    VGroup(picText1,picText2).move_to((pic.get_bottom()+pic.rect.get_bottom())/2)
    return Group(pic.rect,pic,picText1,picText2)

def palyALL(self,allParts):
    self.play(
        FadeIn(allParts[:2],scale=0.5),
        FadeIn(allParts[2],scale=0.5),
        )
    self.play(Write(allParts[3]))
    self.wait(10)
    self.play(FadeOut(allParts,shift=DOWN))

def introduction(
        self, 
        name_ch, 
        name_eng=None, 
        bir=None, 
        intro=None
        ):
    all_txt = VGroup()
    name_chinese = Text(name_ch, font="思源黑体 CN Heavy", size=2.2)
    all_txt.add(name_chinese)
    if name_eng is not None:
        name_english = Text(name_eng, font="Times New Roman", color = BLUE, size=2)
        all_txt.add(name_english)
    if bir is not None:
        birthday = Text(bir,font="思源黑体 CN",size=1.3)
        all_txt.add(birthday)
    if intro is not None:
        introduction = Text(intro, font="思源黑体 CN Heavy", size=1.5)
        all_txt.add(introduction)
    
    all_txt.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff = 0.5
            ).scale(0.36).to_corner(DL).shift(UP*0.618)
    ret_buff = 0.5
    ret = RoundedRectangle(
        height = all_txt.get_height()+ret_buff,
        width = all_txt.get_width()+ret_buff,
        color = BLACK,
        fill_opacity = 0.5,
        corner_radius = 0.15,
        stroke_opacity = 0
        ).move_to(all_txt)

    if len(all_txt)>=2:
        self.play(
            FadeIn(ret),
            LaggedStartMap(
                FadeInFromDown,all_txt,
            lag_ratio=0.2)
            )
    else:
        self.play(
            FadeIn(ret),
            Write(all_txt)
            )  
    self.wait()
    
def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

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

