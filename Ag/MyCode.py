from sympy import false
from manimlib import *


class PicShow(Scene):
    def construct(self):
        file_path = 'Z:\\Drive\\彭导Video\\短视频\\1 不同国家的纸钱\认识一下：世界上的钱币'
        files_names = os.listdir(file_path)
        files_names.reverse()
        pics_g = Group()
        for files_name in files_names:
            if not files_name.endswith('.db'):
                name = files_name.split(".")[0]
                path_name=os.path.join(file_path, name)
                # print(name)
                # print(path_name)
                pics_g.add(self.imageObjAndText(path_name,name))
        title = Title(
                    "不同国家的纸币", 
                    # font = 'Source Han Sans CN',
                    font_size=168,
                    include_underline= false
                    )
        self.play(ShowCreation(title))
        self.rotateAndFade(title, pics_g)
        self.wait()

    def rotateAndFade(self, title, mobs):
        Origin = 6.5*DOWN
        angle = -PI/2
        num_mobs = len(mobs)
        mobs.rotate(angle = angle,about_point = Origin)
        for i in range(num_mobs):
            if i==0:
                self.play(
                        title.animate.set_opacity(0.382),
                        Rotate(mobs[i],angle = -angle,about_point = Origin),
                        run_time= 0.8,
                    )
            self.wait(2)
            if i < num_mobs-1:
                self.play(
                        Rotate(mobs[i],angle = -angle+PI/4,about_point = Origin),
                        Rotate(mobs[i+1],angle = -angle, about_point = Origin),
                        run_time= 0.8,
                    )
                
            if i == num_mobs-1:
                self.play(
                        Rotate(mobs[i],angle = -angle+PI/4,about_point = Origin),
                        title.animate.set_opacity(0),
                        run_time= 0.8,
                    )
                
    def imageObjAndText(self,imageName,text):
        pic = ImageMobject(imageName).scale(1.2)
        pic.rect = SurroundingRectangle(pic,color=WHITE,stroke_width=8,buff=0)
        picText = Text(text, 
                        font = 'Source Han Sans CN',
                        font_size=50).next_to(pic,DOWN)
        return Group(pic,pic.rect,picText)
    
if __name__ == "__main__":
    from os import system
    system("manimgl {} PicShow -o --hd".format(__file__))