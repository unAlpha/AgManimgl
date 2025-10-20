from manimlib import *

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    return coords

class TheBar():
    CONFIG = {
            "bar_height": 0.5,
            "name_size": 30,
            "bar_length": 9,
            "bar_color": None,
            "bar_stroke_width": 1.238,
            "min_length": 1e-2,
            "num_txt_buff": 0.2,
            "bar_space": 0.7,  # 垂直间距
            "deci_config_nums": {
                    "num_decimal_places": 0,
                    "font_size": 30,
                }
        }
    
    def __init__(self, name, value, target_value, max_val, rank=0, **kwargs):
        digest_config(self, kwargs)
        self.name = name
        self.bar = VGroup()
        self.bar.val = ValueTracker(value)  # 当前值
        self.bar.target_val = ValueTracker(target_value)  # 目标值
        self.bar.max_val = max_val
        self.bar.rank = ValueTracker(rank)  # 当前排名
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
        self.bar.add(self.rct, self.text, self.num_txt)
        
        # 添加实时自动更新器
        self.bar.add_updater(self.continuous_updater)
      
    def the_bar(self, length):
        return Rectangle( 
                height=self.bar_height,
                width=length,
                fill_color=self.bar_color,
                fill_opacity=1,
                stroke_width=self.bar_stroke_width,
            )
    
    def text_updater(self, text):
        text.next_to(self.rct, LEFT, buff=0.25)
        text.set_opacity(self.rct.get_opacity())
        
    def num_txt_updater(self, deci_txt):
        deci_txt.set_value(self.bar.val.get_value())
        deci_txt.next_to(self.rct, RIGHT, buff=self.num_txt_buff)
        deci_txt.set_opacity(self.rct.get_opacity())
        
    def bar_updater(self, bar): 
        length = self.value_conversion(self.bar.val.get_value(), self.bar.max_val)
        bar_left = bar.get_left()
        bar.stretch_to_fit_width(length, about_point=bar_left)
    
    def continuous_updater(self, bar, dt):
        # 持续更新位置
        target_y = 3 - self.bar.rank.get_value() * self.bar_space
        current_y = bar.get_center()[1]
        # 平滑过渡到新位置 (使用 dt 使动画速度与帧率无关)
        new_y = current_y + (target_y - current_y) * min(1, 5 * dt)
        bar.move_to([0, new_y, 0], aligned_edge=LEFT)
      
    def value_conversion(self, val, max_val):
        return max(self.min_length, val*self.bar_length/max_val)
    
    def get_current_value(self):
        return self.bar.val.get_value()
    
    def get_target_value(self):
        return self.bar.target_val.get_value()
    
    def set_target_value(self, new_value):
        self.bar.target_val.set_value(new_value)

class DynamicBarChart(Scene):
    def construct(self):
        # 加载CSV数据
        data = get_coords_from_csvdata("Ag/data_files/GNI-data")
        dataArray = np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        print(row, column)
        
        n_row = row
        star = 0  # 起始列索引
        end = 10  # 结束列索引
        
        # 提取数值数据
        datas = dataArray[1:n_row, 2:column].astype(np.float)
        
        # 获取所有从star到end的列的数据
        data_nums = [nums for nums in [datas[:, i] for i in range(star, end)]]
        
        # 找出最大值用于缩放
        datas_nums_max = max([max(data_col) for data_col in data_nums])
        
        # 初始数据和最终数据
        initial_data = data_nums[0]
        
        # 为每个国家/行创建柱状图
        bars = []
        names = dataArray[1:n_row, 0]  # 假设国家名称在第一列
        
        # 创建一个用于管理更新器的 Mobject
        updater_mobject = Mobject()
        self.add(updater_mobject)
        
        # 创建多个柱状图用于不同国家/行
        for i in range(len(initial_data)):
            country_name = names[i] if i < len(names) else f"Country {i+1}"
            initial_value = initial_data[i]
            the_bar = TheBar(
                country_name, 
                0,  # 初始值为0
                initial_value,  # 目标值为第一列数据
                datas_nums_max, 
                rank=i, 
                bar_color=BLUE
            )
            bars.append(the_bar)
            self.add(the_bar.bar)
        
        # 首先动画到初始数据
        self.play(
            *[bar.bar.val.animate.set_value(bar.get_target_value()) for bar in bars],
            run_time=1
        )
        
        # 设置排序方向 (True为从大到小排序)
        sort_descending = True
        
        # 添加实时排序更新器
        def update_ranks(mob, dt):
            # 获取当前所有值并排序
            bar_values = [(i, bars[i].get_current_value()) for i in range(len(bars))]
            
            if sort_descending:
                bar_values.sort(key=lambda x: x[1], reverse=True)  # 从大到小
            else:
                bar_values.sort(key=lambda x: x[1])  # 从小到大
            
            # 设置排名
            for new_rank, (bar_idx, _) in enumerate(bar_values):
                bars[bar_idx].bar.rank.set_value(new_rank)
        
        # 添加实时排序功能
        updater_mobject.add_updater(update_ranks)
        
        # 主动画循环 - 在各列数据之间平滑过渡
        dur_time = 2
        
        for col_idx in range(1, len(data_nums)):
            # 设置新的目标值
            for i, bar in enumerate(bars):
                if i < len(data_nums[col_idx]):
                    bar.set_target_value(data_nums[col_idx][i])
            
            # 创建平滑过渡到新值的动画
            self.play(
                *[bar.bar.val.animate.set_value(bar.get_target_value()) for bar in bars],
                rate_func=linear,
                run_time=dur_time
            )
            
            # 短暂停留在当前状态
            # self.wait(0.5)
        
        # 移除排序更新器
        updater_mobject.remove_updater(update_ranks)

if __name__ == "__main__":
    from os import system
    system("manimgl {} DynamicBarChart -ol".format(__file__))