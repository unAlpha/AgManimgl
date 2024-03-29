from manimlib import *
import scipy.stats as ss
import colorsys
def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class TheBar():
    CONFIG = {
            "bar_height" : 0.5,
            "name_size" : 30,
            "bar_length": 9,
            "bar_color": None,
            "bar_stroke_width": 1.238,
            "min_length": 1e-2,
            "num_txt_buff": 0.2,
            "deci_config_nums": {
                    "num_decimal_places": 0,
                    "font_size": 30,
                }
        }
    def __init__(self, name, value, max_val, **kwargs):
        digest_config(self, kwargs)
        self.name = name
        self.bar = VGroup()
        self.bar.val = ValueTracker(value)
        self.bar.max_val = max_val
        self.init_bar()

    def init_bar(self):
        rct = self.the_bar(self.value_conversion(self.bar.val.get_value(), self.bar.max_val))
        text = Text(str(self.name), font_size=self.name_size)
        num_txt = DecimalNumber(self.bar.val.get_value(), **self.deci_config_nums)
        self.rct = rct
        self.text = text
        self.num_txt = num_txt
        self.rct = rct.add_updater(self.bar_updater)
        self.text.add_updater(self.text_updater)
        self.num_txt.add_updater(self.num_txt_updater)
        # 下面这句话无法产生连续动画
        # self.add(self.bar,self.text,self.num_txt)
        self.bar.add(self.rct,self.text,self.num_txt)
        
    def the_bar(self, length):
        return Rectangle( 
        # return RRectangle( 
                height = self.bar_height,
                width = length,
                fill_color = self.bar_color,
                fill_opciaty = 1,
                stroke_width = self.bar_stroke_width,
            )

    def text_updater(self, text):
        text.next_to(self.rct, LEFT, buff=0.25)
        text.set_opacity(self.rct.get_opacity())

    def num_txt_updater(self, deci_txt):
        deci_txt.set_value(self.bar.val.get_value())
        deci_txt.next_to(self.rct, RIGHT,buff=self.num_txt_buff)
        deci_txt.set_opacity(self.rct.get_opacity())

    def bar_updater(self,bar): 
        length = self.value_conversion(self.bar.val.get_value(), self.bar.max_val)
        bar_left = bar.get_left()
        bar.stretch_to_fit_width(length, about_point = bar_left)
        
    def value_conversion(self, val, max_val):
        return max(self.min_length, val*self.bar_length/max_val)
    
class TheLines(TheBar):
    CONFIG = { 
            "lines_height": None,
            "lines_origin": ORIGIN,
            "text_direction": UP,
            "deci_config_ruler": {
                    "num_decimal_places": 0,
                    "font_size": 50,
                }
        }
    def __init__(self, value, max_val, **kwargs):
        VGroup.__init__(self, **kwargs)
        ValueTracker.__init__(self, value, **kwargs)
        self.init_line(value, max_val)
        self.set_value(value)

    def init_line(self, value, max_val):  
        line = Line(
                start= UP*self.lines_height/2,
                end= DOWN*self.lines_height/2,
            ).shift(self.lines_origin)
        line.move_to(
                self.bar_origin + RIGHT*self.value_conversion(value, max_val),
                coor_mask=np.array([1, 0 ,0])
            )
        line_txt = DecimalNumber(
                value, 
                **self.deci_config_ruler
            )
        self.line = line
        self.line_txt = line_txt
        self.line_txt.add_updater(self.line_txt_updater)
        self.add(self.line, self.line_txt)

    def line_txt_updater(self, mob_txt):
        mob_txt.set_value(self.get_value())
        mob_txt.next_to(self.line, self.text_direction, buff=0.1)
        mob_txt.set_opacity(self.line.get_opacity())
  
    def line_updater(self, value, max_value):
        length = self.value_conversion(value, max_value)
        self.move_to(
                self.bar_origin + RIGHT*length,
                coor_mask=np.array([1, 0 ,0])
            )
        self.set_value(value)

class TheIcons(ImageMobject):
    def __init__(self, path, bar, **kwargs):
        ImageMobject.__init__(self, path, **kwargs)
        def image_updater(img):
            img.next_to(bar, RIGHT, buff=0.1618)
            img.set_opacity(bar.get_opacity())
        self.add_updater(image_updater)

class BarChartRace(VGroup):
    CONFIG = {
            "bars_origin": 2.9*UP + 4.5*LEFT,
            "bars_height": 0.5,
            "bars_opacity": 0.9,
            "spacing": 0.6,
            "datas_value_max": None,
            "value_max": 10000,
            "bar_num": 2,
            "value_0": 1e-2,
            "lines_opacity": 0.236,
            "lightness": 0.9,
            "color_seed": 100,  
            "star_anim": False,
            "add_lines": False,
            "add_icons": True,
            "path": "GNI_icon/",
        }
    def __init__(  
            self,
            legends,
            data_0 = None,
            **kwargs
        ):
        VGroup.__init__(self, **kwargs)
        self.bars = VGroup()
        self.init_bars(legends, data_0,)
        if self.add_lines:
            self.init_lines(data_0)

    def init_bars(self, legends, data_0,):
        if data_0 is None:
            data_0 = [self.value_0]*len(legends)
        rand_serial =len(data_0)-ss.rankdata(data_0, method='ordinal')
        max_value = self.find_max_value(data_0)
        random.seed(self.color_seed)
        icons = Group()
        for i,legend in enumerate(legends):
            cust_color = self.random_color()
            if self.star_anim:
                one_bar = TheBar(
                        legend, 
                        self.value_0, 
                        max_value,
                        bar_height = self.bars_height,
                        bar_color = cust_color,
                    )
            else:
                one_bar = TheBar(
                        legend, 
                        data_0[i],
                        max_value,
                        bar_height = self.bars_height,
                        bar_color = cust_color,
                    )
            if self.add_icons:
                the_icon = TheIcons(self.path+str(legend), one_bar.bar)
                the_icon.set_width(0.65)
                icons.add(the_icon)
            bottom_down = self.bars_origin + DOWN*self.spacing*(rand_serial[i])
            if bottom_down[1] < (BOTTOM+self.bars_height*DOWN)[1]:
                bottom_down = self.bars_origin*RIGHT + BOTTOM + 2*self.bars_height*DOWN
            one_bar.bar.move_to(bottom_down, aligned_edge=LEFT)
            one_bar.bar.set_opacity(0)
            self.bars.add(one_bar.bar)
            self.icons = icons

    def init_lines(self, data_0):
        self.line_nums = int(self.datas_value_max/self.value_max)
        max_value = self.find_max_value(data_0)
        num_x = [0, 1, 2, 3, 4]
        while num_x[-1]<self.line_nums:
            num_x.append(num_x[-1]+num_x[-3])
            num_x.append(2*num_x[-1]-num_x[-2])
        for i in range(len(num_x)):
            line = TheLines(
                    self.value_max*num_x[i],
                    max_value,
                    lines_height = self.spacing*(self.bar_num-1)+self.bars_height+0.1,
                    lines_origin = self[0].bar_origin + (DOWN*self.spacing*(self.bar_num-1))/2,
                    bar_origin = self.bars_origin,
                )
            line.set_opacity(0)
            self.add(line) 
        self.num_x = num_x

    def rank_bars_anim(self, values):
        rand_serial =len(values)-ss.rankdata(values, method='ordinal')
            # 从小到大写法：
            # rand_serial =ss.rankdata(self.nums)-1
        max_value = self.find_max_value(values)
        for i, the_bar in enumerate(self.bars[:len(values)]):
            if values[i] == 0:
                value = self.value_0
            else:
                value = values[i]
            the_bar.max_val = max_value
            the_bar.val.set_value(value)
            bottom_down = self.bars_origin + DOWN*self.spacing*(rand_serial[i])
            if bottom_down[1] < (BOTTOM+self.bars_height*DOWN)[1]:
                bottom_down = self.bars_origin*RIGHT + BOTTOM + 2*self.bars_height*DOWN
            the_bar.move_to(bottom_down,coor_mask=np.array([0, 1 ,0]))
            mask_position = self.bars_origin + DOWN*self.spacing*self.bar_num
            
            if the_bar.get_center()[1] > mask_position[1]:
                the_bar.set_opacity(self.bars_opacity)
            else:
                the_bar.set_opacity(0)

    def rank_lines_anim(self, values):
        max_value = self.find_max_value(values)
        in_lines_index = 0
        for the_line in self[len(values):]:
            the_line.line_updater(the_line.get_value(),max_value)
            if the_line.get_center()[0] < (the_line.bar_origin+the_line.bar_length*RIGHT)[0]:
                in_lines_index+=1
                the_line.set_opacity(self.lines_opacity)
            else:
                the_line.set_opacity(0)
        if in_lines_index>=5:
            if in_lines_index%2 == 1:
                for jk in range(in_lines_index):
                    if jk not in [0, in_lines_index-1, in_lines_index-3]:
                        self[jk+len(values)].set_opacity(0)
            if in_lines_index%2 == 0:
                for jk in range(in_lines_index):
                    if jk not in [0, in_lines_index-1, in_lines_index-2, in_lines_index-4]:
                        self[jk+len(values)].set_opacity(0)

    def find_max_value(self, values):
        return max(*values, self.value_max)

    def random_color(self):
        col = list(map(
                lambda x: hex(x).split('x')[1].zfill(2), 
                tuple(round(i * 255) for i in colorsys.hsv_to_rgb(
                        random.random(),
                        random.random(),
                        self.lightness)
                    )
                )
            )
        return "#%s%s%s"%(col[0],col[1],col[2])
 
class PlotBarChart(Scene):
    def construct(self):
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        n_row = row
        star = 0
        end = 3
        
        title = dataArray[1:n_row, 1]
        years = dataArray[0, 2:column].astype(np.float)
        datas = dataArray[1:n_row, 2:column].astype(np.float)

        data_nums = [nums for nums in [datas[:,i] for i in range(star, end)]]
        datas_nums_max = datas.max()
        year_nums = years[star:end]

        year_val = ValueTracker(year_nums[0])
        year_text = DecimalNumber(
                year_val.get_value(),
                num_decimal_places = 0,
                group_with_commas = False,
                font_size = 250,
                color = BLUE,
            ).to_corner(DR).shift(UP*0.5)
        year_text.add_updater(lambda mob: mob.set_value(year_val.get_value()))

        the_bars = BarChartRace(title, data_nums[0], datas_value_max = datas_nums_max, bar_num=5)
        
        self.add(the_bars.bars, year_text, the_bars.icons,)
        
        dur_time = 2
        for i,data_num in enumerate(data_nums):
            self.play(
                    # bars.rank_lines_anim, data_num,
                    the_bars.animate.rank_bars_anim(data_num),
                    year_val.animate.set_value(year_nums[i]),
                    rate_func=linear,
                    run_time=dur_time,
                )
        self.wait(1)
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} PlotBarChart -ol".format(__file__))