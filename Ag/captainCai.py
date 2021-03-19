from Ag.imports_ag import *

class Captain2_1(Scene):
    def construct(self):
        chapter="2-1"
        loc = [2.3,0.9]

        open_file_path="media/raster_images/captainCaiPic/%s.txt"%chapter
        open_file = open(open_file_path,'r',encoding="UTF-8")
        chapter_txt=[line for line in open_file]
        pic = ImageMobject(
                "captainCaiPic/%s"%chapter,
                height=FRAME_HEIGHT
                )
        pic_txt_ret = Rectangle(
                height=1.26,
                width=9.6,
                color=BLACK
            ).shift(RIGHT*loc[0]+UP*loc[1])

        def txt_shift_pic(text, pic):
            buff=0.618
            if text.get_width()>(pic.get_width()-buff):
                text.set_width(pic.get_width()-buff)
            text.move_to(pic,aligned_edge=LEFT)
            text.shift(0.3*RIGHT)
                
        txt_title =[]
        for i,txt in enumerate(chapter_txt):
            txt_add_num = "%s "%(i+1)+txt
            txt_title.append(txt_add_num)
            pic_text = Text(txt_add_num,
                    font='Source Han Sans CN',
                    color=BLACK,
                    font_size=60
                    )
            txt_shift_pic(pic_text,pic_txt_ret)
            self.clear()
            self.add(pic,pic_text)
            self.wait()

            file_path = "media/images/%s.%s.png"%(chapter,i+1)
            self.get_image().save(file_path)

        with open("media/images/title.txt","w") as tit_file:
            for title in txt_title:
                tit_file.write(title)
        tit_file.close()

        

            



