"""
动态条形图比赛
增强版 - 实现了实时数值变化、长度变化和排序功能
特点：
1. 自动实时排序
2. 条形图数值平滑过渡
3. 位置平滑移动
4. 基于dt的动画更新，保证不同帧率下表现一致
"""
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
    def __init__(self, name, value, target_value, max_val, rank=0, **kwargs):
        digest_config(self, kwargs)
        self.name = name
        self.bar = VGroup()
        self.bar_container = VGroup()  # 新增容器，仅包含条形本身
        self.bar.val = ValueTracker(value)  # 当前值
        self.bar.target_val = ValueTracker(target_value)  # 目标值
        self.bar.max_val = max_val
        self.bar.rank = ValueTracker(rank)  # 当前排名
        self.bar.duration = 1  # 默认动画持续时间为1秒
        self.init_bar()

    def init_bar(self):
        # 创建条形本身
        rct = self.the_bar(self.value_conversion(self.bar.val.get_value(), self.bar.max_val))
        self.rct = rct
        self.rct = rct.add_updater(self.bar_updater)
        self.bar_container.add(self.rct)  # 仅将条形添加到容器
        
        # 创建文字和数值
        text = Text(str(self.name), font_size=self.name_size)
        num_txt = DecimalNumber(self.bar.val.get_value(), **self.deci_config_nums)
        self.text = text
        self.num_txt = num_txt
        self.text.add_updater(self.text_updater)
        self.num_txt.add_updater(self.num_txt_updater)
        
        # 添加所有元素到主VGroup
        self.bar.add(self.bar_container, self.text, self.num_txt)
        
        # 添加实时自动更新器 - 只更新值，不更新位置
        self.bar.add_updater(self.continuous_updater)
        
    def the_bar(self, length):
        return Rectangle( 
                height = self.bar_height,
                width = length,
                fill_color = self.bar_color,
                fill_opacity = 1,
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
    
    def continuous_updater(self, bar, dt):
        # BarChartRace_ABar中没有连续更新值的逻辑，只是在动画中直接修改值
        # 这可能就是主要差异所在
        pass
        
    def value_conversion(self, val, max_val):
        return max(self.min_length, val*self.bar_length/max_val)
    
    def get_current_value(self):
        return self.bar.val.get_value()
    
    def get_target_value(self):
        return self.bar.target_val.get_value()
    
    def set_target_value(self, new_value):
        self.bar.target_val.set_value(new_value)

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
        super().__init__(path, **kwargs)
        def image_updater(img):
            img.next_to(bar, RIGHT, buff=0.1618)
            img.set_opacity(bar.get_opacity())
        self.add_updater(image_updater)
        
    # 添加必要的方法以确保渲染正常
    def has_fill(self):
        return True
        
    def has_stroke(self):
        return False

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
            "sort_descending": True,  # 排序方向，默认从大到小
        }
    def __init__(  
            self,
            legends,
            data_0 = None,
            **kwargs
        ):
        VGroup.__init__(self, **kwargs)
        self.bars = VGroup()
        self.updater_mobject = Mobject()  # 用于管理排序更新器
        self.add(self.updater_mobject)
        self.init_bars(legends, data_0)
        self.add(self.bars)  # 将bars VGroup添加到主VGroup
        
        if self.add_lines:
            self.init_lines(data_0)
        
        # 添加实时排序更新器
        self.updater_mobject.add_updater(self.update_ranks)

    def init_bars(self, legends, data_0):
        if data_0 is None:
            data_0 = [self.value_0]*len(legends)
        rand_serial = len(data_0)-ss.rankdata(data_0, method='ordinal')
        max_value = self.find_max_value(data_0)
        random.seed(self.color_seed)
        icons = Group()
        
        self.bar_objects = []  # 存储TheBar对象
        
        for i, legend in enumerate(legends):
            cust_color = self.random_color()
            
            if self.star_anim:
                initial_value = self.value_0
            else:
                initial_value = 0  # 初始值为0
                
            # 创建TheBar对象
            one_bar = TheBar(
                    legend, 
                    initial_value,  # 初始值
                    data_0[i],      # 目标值
                    max_value,
                    rank=rand_serial[i],
                    bar_height=self.bars_height,
                    bar_color=cust_color,
                )
            
            # 存储对TheBar对象的引用    
            self.bar_objects.append(one_bar)
            
            if self.add_icons:
                the_icon = TheIcons(self.path+str(legend), one_bar.bar)
                the_icon.set_width(0.65)
                icons.add(the_icon)
                self.icons = icons
                
            # 计算位置
            bottom_down = self.bars_origin + DOWN*self.spacing*(rand_serial[i])
            if bottom_down[1] < (BOTTOM+self.bars_height*DOWN)[1]:
                bottom_down = self.bars_origin*RIGHT + BOTTOM + 2*self.bars_height*DOWN
            
            # 设置位置 - 仅按条形本身的左端对齐，而不是整个VGroup
            one_bar.bar_container.move_to(bottom_down, aligned_edge=LEFT)
            one_bar.bar.set_opacity(self.bars_opacity)
            
            # 将整个bar添加到VGroup中
            self.bars.add(one_bar.bar)

    def init_lines(self, data_0):
        self.line_nums = int(self.datas_value_max/self.value_max)
        max_value = self.find_max_value(data_0)
        num_x = [0, 1, 2, 3, 4]
        while num_x[-1]<self.line_nums:
            num_x.append(num_x[-1]+num_x[-3])
            num_x.append(2*num_x[-1]-num_x[-2])
        
        self.lines = VGroup()  # 创建一个VGroup来存储线条
        
        for i in range(len(num_x)):
            try:
                line = TheLines(
                    self.value_max*num_x[i],
                    max_value,
                    lines_height = self.spacing*(self.bar_num-1)+self.bars_height+0.1,
                    lines_origin = self.bars_origin + (DOWN*self.spacing*(self.bar_num-1))/2,
                    bar_origin = self.bars_origin,
                )
                line.set_opacity(0)
                self.lines.add(line)
            except Exception as e:
                print(f"Error creating line {i}: {e}")
            
        self.add(self.lines)  # 将lines VGroup添加到主VGroup
        self.num_x = num_x

    def rank_bars_anim(self, values, duration=1):
        # 更新目标值
        for i, bar_obj in enumerate(self.bar_objects[:len(values)]):
            if values[i] == 0:
                value = self.value_0
            else:
                value = values[i]
            bar_obj.bar.max_val = self.find_max_value(values)
            bar_obj.set_target_value(value)
            
            # 设置动画持续时间
            bar_obj.bar.duration = duration
        
        # 由于添加了连续更新器，动画会自动进行
        return self

    def rank_lines_anim(self, values):
        max_value = self.find_max_value(values)
        in_lines_index = 0
        
        if not hasattr(self, 'lines') or len(self.lines) == 0:
            return
        
        for i, the_line in enumerate(self.lines):
            the_line.line_updater(the_line.get_value(), max_value)
            if the_line.get_center()[0] < (the_line.bar_origin+the_line.bar_length*RIGHT)[0]:
                in_lines_index+=1
                the_line.set_opacity(self.lines_opacity)
            else:
                the_line.set_opacity(0)
            
        if in_lines_index>=5:
            if in_lines_index%2 == 1:
                for jk in range(in_lines_index):
                    if jk not in [0, in_lines_index-1, in_lines_index-3]:
                        self.lines[jk].set_opacity(0)
            if in_lines_index%2 == 0:
                for jk in range(in_lines_index):
                    if jk not in [0, in_lines_index-1, in_lines_index-2, in_lines_index-4]:
                        self.lines[jk].set_opacity(0)

    def update_ranks(self, mob, dt):
        # 确保有数据可以排序
        if not hasattr(self, 'bar_objects') or len(self.bar_objects) == 0:
            return
        
        # 获取所有条形的当前值并排序
        bar_values = []
        for i, bar_obj in enumerate(self.bar_objects):
            bar_values.append((i, bar_obj.get_current_value()))
        
        if self.sort_descending:
            bar_values.sort(key=lambda x: x[1], reverse=True)  # 从大到小
        else:
            bar_values.sort(key=lambda x: x[1])  # 从小到大
        
        # 设置排名并更新位置
        for new_rank, (bar_idx, _) in enumerate(bar_values):
            # 更新排名
            self.bar_objects[bar_idx].bar.rank.set_value(new_rank)
            
            # 根据排名计算目标位置
            target_y = self.bars_origin[1] - self.spacing * new_rank
            if target_y < (BOTTOM+self.bars_height*DOWN)[1]:
                target_y = (BOTTOM + 2*self.bars_height*DOWN)[1]
                
            # 获取当前bar容器
            current_bar_container = self.bar_objects[bar_idx].bar_container
            
            # 平滑移动到新位置
            current_y = current_bar_container.get_center()[1]
            new_y = current_y + (target_y - current_y) * min(1, 3 * dt)
            
            # 应用新位置 - 对条形容器应用对齐
            current_x = self.bars_origin[0]
            current_bar_container.move_to([current_x, new_y, 0], aligned_edge=LEFT)
            
            # 控制可见性
            mask_position = self.bars_origin[1] - self.spacing * self.bar_num
            if new_y > mask_position:
                self.bar_objects[bar_idx].bar.set_opacity(self.bars_opacity)
            else:
                self.bar_objects[bar_idx].bar.set_opacity(0)
                
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
        # 加载数据
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row,column)
        n_row = row
        star = 40
        end = 50  # 使用前10列数据
        
        # 处理数据
        title = dataArray[1:n_row, 1]  # 名称
        years = dataArray[0, 2:column].astype(np.float)  # 年份
        datas = dataArray[1:n_row, 2:column].astype(np.float)  # 数值数据

        # 准备绘图数据
        data_nums = [nums for nums in [datas[:,i] for i in range(star, end)]]
        datas_nums_max = datas.max()
        year_nums = years[star:end]

        # 创建年份显示
        year_val = ValueTracker(year_nums[0])
        year_text = DecimalNumber(
                year_val.get_value(),
                num_decimal_places = 0,
                group_with_commas = False,
                font_size = 250,
                color = BLUE,
            ).to_corner(DR).shift(UP*0.5)
        year_text.add_updater(lambda mob: mob.set_value(year_val.get_value()))

        # 创建条形图比赛对象
        the_bars = BarChartRace(
            title,
            data_nums[0],
            datas_value_max=datas_nums_max,
            bar_num=len(title),  # 使所有条形都可见
            spacing=0.6,  # 条形间距
            # add_lines=True,  # 是否显示参考线
            sort_descending=True,  # 从大到小排序
            add_icons=True, 
        )
        
        # 添加到场景
        self.add(the_bars,the_bars.icons)
        self.add(year_text)
        
        # 初始动画 - 从0到初始值
        self.play(
            *[bar_obj.bar.val.animate.set_value(bar_obj.get_target_value()) 
              for bar_obj in the_bars.bar_objects],
            rate_func=linear,
            run_time=1
        )
        
        # 主动画 - 各时间点之间的平滑过渡
        dur_time = 1
        for i, data_num in enumerate(data_nums[1:], 1):
            # 更新目标值
            the_bars.rank_bars_anim(data_num, duration=dur_time)
            
            # BarChartRace_ABar的关键差异：使用animate直接设置值，而不是依赖continuous_updater
            self.play(
                *[bar_obj.bar.val.animate.set_value(bar_obj.get_target_value()) 
                  for bar_obj in the_bars.bar_objects],
                year_val.animate.set_value(year_nums[i]),
                rate_func=linear,
                run_time=dur_time,
            )
        
        # 结束等待
        self.wait(2)
        
if __name__ == "__main__":
    from os import system
    system("manimgl {} PlotBarChart -ol".format(__file__))