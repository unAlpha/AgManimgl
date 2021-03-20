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

class TheBars(VGroup):
    CONFIG = {
        "height" : 0.4,
        "name_size" : 0.618,
        "graph_origin" : 2.6*UP + 4*LEFT,
        }
    def __init__(self, name, value = 0.1, **kwargs):
        VGroup.__init__(self, **kwargs)

        bar = Rectangle(
                height = self.height,
                width = value,
            )
        bar.move_to(self.graph_origin,aligned_edge=LEFT)
        text = Text(str(name), size=self.name_size)
        num_txt = DecimalNumber(value)

        self.value = ValueTracker(value)
        self.bar = bar
        self.text = text
        self.num_txt = num_txt
        self.text.add_updater(lambda d: d.next_to(self.bar,LEFT,buff=0.25))
        self.num_txt.add_updater(lambda d: d.set_value(self.value.get_value()))
        self.num_txt.add_updater(lambda d: d.next_to(self.bar,RIGHT,buff=0.25))
        self.add_updater(lambda d: d.change_bar_values(self.value.get_value()))
        self.add(self.bar,self.text,self.num_txt,)

    def change_bar_values(self, value):
        bar = self.bar      
        bar_left = bar.get_left()
        bar_right = bar.get_right()
        bar_width = value
        if bar_width>0:
            # 1e-3是柱图有边框导致的偏移
            if bar_left[0]<self.graph_origin[0]-1e-3:
                bar.stretch_to_fit_width(-bar_width)
                bar.move_to(bar_right, LEFT)    
            else: 
                bar.stretch_to_fit_width(bar_width)
                bar.move_to(bar_left, LEFT)
        else:
            # 1e-3是柱图有边框导致的偏移
            if bar_left[0]<self.graph_origin[0]+1e-3:
                bar.stretch_to_fit_width(-bar_width)
                bar.move_to(bar_right, RIGHT)
            else:
                bar.stretch_to_fit_width(bar_width)
                bar.move_to(bar_left, RIGHT)
        return self

class BarChartRectangle(VGroup):
    CONFIG = {
        "spacing":0.6
    }
    def __init__(self, names, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add_legends(names)
        
    def add_legends(self, legends):
        for i,legend in enumerate(legends):
            one_bar = TheBars(legend)
            bar = one_bar.bar
            bar.move_to(one_bar.graph_origin+DOWN*self.spacing*i,aligned_edge=LEFT)
            self.add(one_bar)

    def rank_bar(self,values):
        # 从大到小
        rand_serial =len(values)-ss.rankdata(values)
        # 从小到大
        # rand_serial =ss.rankdata(self.nums)-1
        for i,the_bar in enumerate(self):
            the_bar.move_to(
                the_bar.graph_origin + DOWN*self.spacing*(rand_serial[i]),
                aligned_edge=the_bar.graph_origin,
                coor_mask=np.array([0, 1 ,0])
                )

class PlotBarChart(Scene):
    def construct(self):
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        # row = dataArray.shape[0]
        column = dataArray.shape[1]
        title = dataArray[1:5,1]
        data_nums = []
        for nums in [map(int,dataArray[1:5,i]) for i in range(2,column)]:
            coords = [num/1000 for num in nums]
            data_nums.append(coords)

        bars = BarChartRectangle(title)
        self.add(bars)
        for data_num in data_nums:
            self.play(
                    *[ApplyMethod(the_bar.value.set_value,value) for the_bar,value in zip(bars,data_num)],
                    bars.rank_bar,data_num,
                    rate_func=linear,
                )
        self.wait(2)
