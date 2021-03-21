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

class TheBars(VGroup, ValueTracker):
    CONFIG = {
        "height" : 0.4,
        "name_size" : 0.618,
        "graph_origin" : 2.6*UP + 4*LEFT,
        "deci_config": {
                "num_decimal_places": 0,
                "font_size": 36,
            }
        }
    def __init__(self, name, value, **kwargs):
        VGroup.__init__(self, **kwargs)
        ValueTracker.__init__(self, value, **kwargs)
        bar = Rectangle(
                height = self.height,
                width = value,
            )
        bar.move_to(self.graph_origin,aligned_edge=LEFT)
        text = Text(str(name), size=self.name_size)
        num_txt = DecimalNumber(value,**self.deci_config)

        self.bar = bar
        self.text = text
        self.num_txt = num_txt
        self.text.add_updater(self.text_updater)
        self.num_txt.add_updater(self.num_txt_updater)
        self.add(self.bar,self.text,self.num_txt,)

    def text_updater(self, text):
        text.next_to(self.bar,LEFT,buff=0.25)
        text.set_opacity(self.bar.get_opacity())

    def num_txt_updater(self,deci_txt):
        deci_txt.set_value(self.get_value())
        deci_txt.next_to(self.bar,RIGHT,buff=0.25)
        deci_txt.set_opacity(self.bar.get_opacity())

    def bar_updater(self, length, value):
        bar = self[0]
        bar_left = bar.get_left()
        bar_right = bar.get_right()
        bar_width = length
        bar.stretch_to_fit_width(bar_width)
        bar.move_to(bar_left, LEFT)
        self.set_value(value)

class BarChartRectangle(VGroup):
    CONFIG = {
        "spacing": 0.6,
        "value_max": 9000,
        "bar_length": 8,
        "bar_num": 9,
        "value_0": 1e-2,
    }
    def __init__(self, names, value0 = None, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add_legends(names, value0)

    def add_legends(self, legends, value0):
        if value0 is None:
            value0 = [self.value_0]*len(legends)
        rand_serial =len(value0)-ss.rankdata(value0,method='ordinal')
        max_value = self.find_max_value(value0)
        for i,legend in enumerate(legends):
            value_length =value0[i]*self.bar_length/max_value
            one_bar = TheBars(legend,self.value_0)
            one_bar.bar.move_to(one_bar.graph_origin+DOWN*self.spacing*(rand_serial[i]),aligned_edge=LEFT)  
            if rand_serial[i] >= self.bar_num:
                one_bar.set_opacity(0)
            self.add(one_bar)

    def rank_bar_anim(self,values):
        rand_serial =len(values)-ss.rankdata(values,method='ordinal')
            # 从小到大写法：
            # rand_serial =ss.rankdata(self.nums)-1
        max_value = self.find_max_value(values)

        for i,the_bar in enumerate(self):            
            value_length =values[i]*self.bar_length/max_value

            if value_length ==0:
                value_length = self.value_0
            the_bar.bar_updater(value_length, values[i])
            
            the_bar.move_to(
                the_bar.graph_origin + DOWN*self.spacing*(rand_serial[i]),
                coor_mask=np.array([0, 1 ,0]))

            mask_position = the_bar.graph_origin + DOWN*self.spacing*(self.bar_num)
            if the_bar.get_center()[1] > mask_position[1]:
                the_bar.set_opacity(1)
            else:
                the_bar.set_opacity(0)

    def find_max_value(self,values):
        max_real = max(values)
        set_max = self.value_max
        if max_real<set_max:
            return set_max
        else:
            return max_real

class PlotBarChart(Scene):
    def construct(self):
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        n_row = row-3
        title = dataArray[1:n_row,1]
        data_nums = []
        for nums in [map(int,dataArray[1:n_row,i]) for i in range(2,5)]:
            coords = [num for num in nums]
            data_nums.append(coords)

        bars = BarChartRectangle(title, data_nums[0])
        self.add(bars)

        for data_num in data_nums:
            self.play(
                    bars.rank_bar_anim, data_num,
                    rate_func=linear,
                    run_time = 2.5
                )
        self.wait(2)
