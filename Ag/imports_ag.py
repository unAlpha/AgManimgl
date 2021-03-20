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
                OS_font=Font
            ):

    pic = ImageMobject(Obj)
    pic.height=height

    if text2 is not None:
        picText1 = Text(text1,
                        font=Font,
                        color="#308032"
            )\
            .set_height(txt_height-0.068)\
            .next_to(pic,DOWN,buff=SMALL_BUFF)
        picText2 = Text(text2,
                        font=Font, 
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
    self.play(FadeOut(allParts,shift=TOP))
