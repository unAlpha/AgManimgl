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

class PlotBarChart(Scene):
    def construct(self):
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        n_row = row
        star = 0
        end = 10

        datas = dataArray[1:n_row, 2:column].astype(np.float)
        data_nums = [nums for nums in [datas[:,i] for i in range(star, end)]]
        datas_nums_max = data_nums[0].max()

        the_bar = TheBar("Test", data_nums[0][0],datas_nums_max,)
        self.add(the_bar.bar)
        # self.add(bars.bar, bars.text, bars.num_txt,)
        
        dur_time = 2
        for data_num in data_nums[0]:
            self.play(
                    the_bar.bar.val.animate.set_value(data_num),
                    rate_func=linear,
                    run_time=dur_time,
                )
        self.wait(1)

if __name__ == "__main__":
    from os import system
    system("manimgl {} PlotBarChart -o --hd".format(__file__))