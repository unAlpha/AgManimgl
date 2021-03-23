from manimlib import *
import scipy.stats as ss

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class TheBars(ValueTracker, VGroup):
    CONFIG = {
        "bar_height" : 0.4,
        "name_size" : 0.618,
        "graph_origin" : 2.6*UP + 4*LEFT,
        "bar_length": 8,
        "deci_config": {
                "num_decimal_places": 0,
                "font_size": 30,
            }
        }
    def __init__(self, name, value, max_val, **kwargs):
        VGroup.__init__(self, **kwargs)
        ValueTracker.__init__(self, value, **kwargs)
        self.init_bar(name, value, max_val)

    def init_bar(self, name, value, max_val):        
        bar = Rectangle(
                height = self.bar_height,
                width = self.value_conversion(value, max_val),
            )
        text = Text(str(name), size=self.name_size)
        num_txt = DecimalNumber(value, **self.deci_config)
        self.set_value(value)
        self.bar = bar
        self.text = text
        self.num_txt = num_txt
        self.text.add_updater(self.text_updater)
        self.num_txt.add_updater(self.num_txt_updater)
        self.add(self.bar, self.text, self.num_txt,)

    def text_updater(self, text):
        text.next_to(self.bar, LEFT, buff=0.25)
        text.set_opacity(self.bar.get_opacity())

    def num_txt_updater(self, deci_txt):
        deci_txt.set_value(self.get_value())
        deci_txt.next_to(self.bar, RIGHT,buff=0.25)
        deci_txt.set_opacity(self.bar.get_opacity())

    def bar_updater(self, value, max_value):   
        length = self.value_conversion(value, max_value)
        bar = self[0]
        bar_left = bar.get_left()
        bar_right = bar.get_right()
        bar_width = length
        bar.stretch_to_fit_width(bar_width)
        bar.move_to(bar_left, LEFT)
        self.set_value(value)

    def value_conversion(self, val, max_val):
        return max(1e-3, val*self.bar_length/max_val)

class TheLines(TheBars):
    CONFIG = {
        "line_height": 6,
        "line_txt_size": 1,
        }
    def __init__(self, value, max_val, **kwargs):
        VGroup.__init__(self, **kwargs)
        ValueTracker.__init__(self, value, **kwargs)
        self.init_line(value, max_val)
        self.set_value(value)

    def init_line(self, value, max_val):  
        line = Line(
                start= UP*self.line_height/2,
                end= DOWN*self.line_height/2,
            )
        line.move_to(
            self.graph_origin + RIGHT*self.value_conversion(value, max_val),
            coor_mask=np.array([1, 0 ,0])
            )
        line_txt = DecimalNumber(value, **self.deci_config)

        self.line = line
        self.line_txt = line_txt
        self.line_txt.add_updater(self.line_txt_updater)
        self.add(self.line, self.line_txt)

    def line_txt_updater(self, mob_txt):
        mob_txt.set_value(self.get_value())
        mob_txt.next_to(self.line, DOWN, buff=0.25)
        mob_txt.set_opacity(self.line.get_opacity())
  
    def line_updater(self, value, max_value):
        length = self.value_conversion(value, max_value)
        self.move_to(
            self.graph_origin + RIGHT*length,
            coor_mask=np.array([1, 0 ,0])
            )
        self.set_value(value)

class BarChartRectangle(VGroup):
    CONFIG = {
        "spacing": 0.6,
        "datas_value_max": None,
        "value_max": 10000,
        "bar_num": 9,
        "value_0": 1e-2,       
        }
    def __init__(  
                self,
                legends,
                data_0 = None,
                star_anim=True,
                add_lines=True,
                **kwargs
            ):
        VGroup.__init__(self, **kwargs)
        self.init_bars(legends, data_0, star_anim)
        self.in_lines_num = 0
        if add_lines:
            self.line_nums = int(self.datas_value_max/self.value_max)
            self.init_lines(data_0)
        
    def init_bars(self, legends, data_0, star_anim):
        if data_0 is None:
            data_0 = [self.value_0]*len(legends)
        rand_serial =len(data_0)-ss.rankdata(data_0, method='ordinal')
        max_value = self.find_max_value(data_0)
        for i,legend in enumerate(legends):
            if star_anim:
                one_bar = TheBars(legend, self.value_0, max_value)
            else:
                one_bar = TheBars(legend, data_0[i], max_value)
            one_bar.bar.move_to(
                one_bar.graph_origin + DOWN*self.spacing*(rand_serial[i]),
                aligned_edge=LEFT)
            one_bar.set_opacity(0)
            self.add(one_bar)

    def init_lines(self, data_0):
        max_value = self.find_max_value(data_0)
        num_x = [1, 2, 3, 4]
        while num_x[-1]<self.line_nums:
            num_x.append(num_x[-1]+num_x[-3])
            num_x.append(2*num_x[-1]-num_x[-2])
        
        for i in range(len(num_x)):
            line = TheLines(self.value_max*num_x[i], max_value,)
            line.set_opacity(0)
            self.add(line)
        self.num_x = num_x

    def rank_bar_anim(self, values):
        rand_serial =len(values)-ss.rankdata(values, method='ordinal')
            # 从小到大写法：
            # rand_serial =ss.rankdata(self.nums)-1
        max_value = self.find_max_value(values)
        for i, bar_or_line in enumerate(self):
            if type(bar_or_line) == TheBars: 
                the_bar = bar_or_line
                if values[i] == 0:
                    value = self.value_0
                else:
                    value = values[i]
                the_bar.bar_updater(value, max_value)
                the_bar.move_to(
                    the_bar.graph_origin + DOWN*self.spacing*(rand_serial[i]),
                    coor_mask=np.array([0, 1 ,0]))
                mask_position = the_bar.graph_origin + DOWN*self.spacing*(self.bar_num)
                if the_bar.get_center()[1] > mask_position[1]:
                    the_bar.set_opacity(1)
                else:
                    the_bar.set_opacity(0)
            
            if type(bar_or_line) == TheLines:
                the_line = bar_or_line
                the_line.line_updater(
                        the_line.get_value(),
                        max_value
                    )         
                if the_line.get_center()[0] < (the_line.graph_origin+the_line.bar_length*RIGHT)[0]:
                    if the_line.get_opacity()<0.5:
                        self.in_lines_num +=1
                    the_line.set_opacity(0.5)
                    if self.in_lines_num == 6:
                        if the_line.get_value() == self.num_x[0]*self.value_max:
                            the_line.set_opacity(0)
                        if the_line.get_value() == self.num_x[2]*self.value_max:
                            the_line.set_opacity(0)
                        self.in_lines_num -= 2
                        self.num_x.pop(0)
                        self.num_x.pop(1)
                else:
                    the_line.set_opacity(0)

    def find_max_value(self, values):
        return max(*values, self.value_max)

class PlotBarChart(Scene):
    def construct(self):
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        n_row = row
        n_column = column
        title = dataArray[1:n_row, 1]
        datas = dataArray[1:n_row, 2:column].astype(np.float)
        datas_max = datas.max()

        data_nums = []
        for nums in [map(int,dataArray[1:n_row, i]) for i in range(2, n_column)]:
            coords = [num for num in nums]
            data_nums.append(coords)
        
        bars = BarChartRectangle(
                    title,
                    data_nums[0],
                    star_anim = False,
                    add_lines = True,
                    datas_value_max = datas_max,
                    value_max = 10000,
                )
        self.add(bars)
        for data_num in data_nums:
            self.play(
                    bars.rank_bar_anim, data_num,
                    rate_func=linear,
                    run_time=2,
                )
        self.wait(1)
