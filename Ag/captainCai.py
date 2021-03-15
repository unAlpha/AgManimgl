from Ag.imports_ag import *

class Captain2_1(Scene):
    def construct(self):
        chapter_two1_txt = [
            "植物演化的复习",
            "植物器官简介",
            "植物根的外型",
            "根的纵切面",
            "根毛的细胞核位置",
            "根的横切面",
            "双子叶植物的根的横切面",
            "单子叶植物根的横切面",
            "根的其他功能(特化根)",
            "茎的简介",
            "茎的外部类型",
            "双子叶植物茎基本结构",
            "双子叶植物草本茎",
            "双子叶植物木本茎-1",
            "双子叶植物木本茎-2",
            "为何年轮有颜色的深浅",
            "单子叶植物茎",
            "茎的其他功能(特化茎)",
            "根和茎的外型比较(表格)",
            "根和茎的比较(表格)",
            "根和茎的比较(图形)",
            "(补充)植物的分生组织与生长方式",
            "叶的外部类型",
            "叶型",
            "叶序",
            "叶的内部结构",
            "叶的其他功能(特化叶)",
            ]
        pic = ImageMobject(
                "captainCaiPic/2-1",
                height=FRAME_HEIGHT
                )

        pic_txt_ret = Rectangle(
                height=1.26,
                width=9.6,
                color=BLACK
            ).shift(0.9*UP+2.3*RIGHT)

        def txt_shift_pic(text, pic):
            text.move_to(pic,aligned_edge=LEFT)
            text.shift(0.3*RIGHT)
            buff=0.618
            if text.get_width()>(pic.get_width()-buff):
                text.set_width(pic.get_width()-buff)
                text.move_to(pic,aligned_edge=LEFT)
                text.shift(0.3*RIGHT)
                
        txt_title =[]
        for i,txt in enumerate(chapter_two1_txt):
            txt_adj = "%s "%(i+1)+txt
            txt_title.append(txt_adj)
            pic_text = Text(txt_adj,
                    font='Source Han Sans CN',
                    color=BLACK,
                    font_size=60
                    )
            txt_shift_pic(pic_text,pic_txt_ret)
            self.clear()
            self.add(pic,pic_text)
            self.wait()

            file_path = "media/images/2-%s.png"%(i+1)
            self.get_image().save(file_path)

        with open("media/images/title.txt","w") as tit_file:
            for title in txt_title:
                tit_file.write(title)
                tit_file.write('\n')
        tit_file.close()

        

            



