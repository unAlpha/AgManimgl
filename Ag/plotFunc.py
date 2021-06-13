from manimlib import *
from numpy import mean
from itertools import groupby


def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class BarChartRectangle(VGroup):
    CONFIG = {
        "stroke_opacity":0.8,
        "fill_opacity":0.5,
        # graph_origin_down是坐标系的原点值
        "graph_origin_down":-2.6,
    }
    def __init__(self,values, width, **kwargs):
        VGroup.__init__(self, **kwargs)
        for value in values:
            # print(value)
            bar = Rectangle(
                height = abs(value[1]-self.graph_origin_down),
                width = width,
                stroke_opacity = self.stroke_opacity,
                fill_opacity = self.fill_opacity,
            )
            print(np.array(value))
            bar.next_to(np.array(value),DOWN,buff=0)
            self.add(bar)
            
    def change_bar_values(self, values):
        for bar, value in zip(self, values):
            bar_bottom = bar.get_bottom()
            bar_top = bar.get_top()
            bar_height = value-self.graph_origin_down
            if bar_height>0:
                # 1e-3是柱图有边框导致的偏移
                if bar_bottom[1]<self.graph_origin_down-1e-3:
                    bar.stretch_to_fit_height(-bar_height)
                    bar.move_to(bar_top, DOWN)    
                else: 
                    bar.stretch_to_fit_height(bar_height)
                    bar.move_to(bar_bottom, DOWN)
            else:
                # 1e-3是柱图有边框导致的偏移
                if bar_top[1]<self.graph_origin_down+1e-3:
                    bar.stretch_to_fit_height(-bar_height)
                    bar.move_to(bar_top, UP)
                else:
                    bar.stretch_to_fit_height(bar_height)
                    bar.move_to(bar_bottom, UP)

class PieChart(VMobject):
    CONFIG = {
        "start_per" : 0,
        "r" : 2,
        "gap" : TAU*2/1000,
        "stroke" : 100,
        "legend_style" : "Dot",
        "legend_loc" : 3.6*RIGHT + 0*UP,
        "legend_scale" : 0.618,
        "scale_k" : 1,
    }

    def create_arc(self, percentage, arc_color):
        arc = Arc(
            radius = self.r,
            start_angle = self.start_per/100*TAU,
            angle = percentage/100*TAU-self.gap,
            color = arc_color,
            stroke_width = self.stroke,
        )
        # 很有启示
        self.start_per += percentage
        return arc

    def craet_arcs(self, args):
        arc_group = VGroup()
        for per, color, name in args:
            arc_group.add(self.create_arc(per, color))
        self.arcs = arc_group
        return self.arcs

    def create_legend(self, per, arc_color, name):
        per_text = Text(
            str(per)+"%", 
            font ='SimSun',
            size = 1,
        )

        name_text = Text(
            name, 
            font ='SimSun',
            size = 1,
        )

        if self.legend_style == "Dot":
            dot_color = Dot(color = arc_color).scale(2.5)
        elif self.legend_style == "Rect":
            dot_color = Square(
                color = arc_color,
                fill_color = arc_color,
                fill_opacity = 1,
            ).scale(0.16)
        
        dot_color.shift(self.legend_loc)
        name_text.next_to(dot_color, RIGHT)
        per_text.next_to(dot_color, LEFT)
        return VGroup(dot_color, name_text, per_text)

    def create_legends(self, args):
        legend_group = VGroup()
        for per, dot, name in args:
            legend_group.add(
                self.create_legend(
                    per, dot, name,
                )
            )
        self.legends = legend_group.scale(self.legend_scale).arrange(
                DOWN,
                buff=MED_SMALL_BUFF,
                index_of_submobject_to_align=0
            )
        return self.legends

    def create_title(self, title):
        return Text(title)
    
    def highlight_items_arcs(self, arcs, item=0):
        arcs[item].scale(1.1,about_point=arcs.get_center())
        return arcs

    def highlight_items_legends(self, legends, item=0):
        legends[item].scale(1.5,about_point=legends[item][0].get_center())
        legends.arrange(
            DOWN,
            center=False,
            buff=MED_SMALL_BUFF,
            index_of_submobject_to_align=0
        )
        return legends

class PieChartScene(Scene):
    def construct(self):
        pc_data = [
            # 百分比形式
            (40, BLUE, "广东"),
            (20, RED, "四川"),
            (30, YELLOW, "湖南"),
            (5, PINK, "江西"),
            (5, GOLD, "河南"),
        ]
        pie_chart = PieChart()
        pc_arcs = pie_chart.craet_arcs(pc_data)
        pc_legends = pie_chart.create_legends(pc_data)
        VGroup(pc_arcs,pc_legends).arrange(RIGHT, buff=LARGE_BUFF*2)
            
        self.play(
            LaggedStartMap(ShowCreation,[obj for obj in pc_arcs],lag_ratio=1),
            LaggedStartMap(FadeInFromDown,[obj for obj in pc_legends],lag_ratio=1),
            run_time=5,
        )

        highlight_items = [0, 1, 2, 3, 4]
        for item in highlight_items:
            self.play(
                Transform(
                    pc_arcs,
                    pie_chart.highlight_items_arcs(pc_arcs.copy(),item)
                ),
                Transform(
                    pc_legends,
                    pie_chart.highlight_items_legends(pc_legends.copy(),item)
                ),
                rate_func=there_and_back_with_pause,
                run_time = 2,
            )

        self.wait()

class YYaxis(GraphScene):
    CONFIG = {
        "y2_min": 0,
        "y2_max": 1000,
        "y2_axis_height": 6,
        "y2_tick_frequency": 100,
        "y2_bottom_tick": None,  # Change if different from y_min
        "y2_labeled_nums": list(np.arange(0, 1000, 100)),
        "y2_axis_label": "$y2$",
        "y2_num_decimal_places":0,
        "y2_label_direction":RIGHT,
        "y2_axes_color":RED,
        "graph_origin": 2.6 * DOWN + 4.5 * LEFT,
    }
    def setup_axes(self, animate=False, reback=False):
        GraphScene.setup_axes(self, animate=False, reback=False)
        y2_num_range = float(self.y2_max - self.y2_min)
        self.space_unit_to_y2 = self.y2_axis_height / y2_num_range

        if self.y2_labeled_nums is None:
            self.y2_labeled_nums = []
        if self.y2_bottom_tick is None:
            self.y2_bottom_tick = self.y2_min
        y2_axis = NumberLine(
            x_min=self.y2_min,
            x_max=self.y2_max,
            unit_size=self.space_unit_to_y2,
            tick_frequency=self.y2_tick_frequency,
            leftmost_tick=self.y2_bottom_tick,
            numbers_with_elongated_ticks=self.y2_labeled_nums,
            color=self.y2_axes_color,
            line_to_number_vect=LEFT,
            label_direction=self.y2_label_direction,
            stroke_opacity=self.xyStrokeOpacity,
            decimal_number_config={"num_decimal_places": self.y2_num_decimal_places}
        )
        y2_axis.shift(self.x_axis.number_to_point(self.x_max) - y2_axis.number_to_point(0))
        y2_axis.rotate(np.pi / 2, about_point=y2_axis.number_to_point(0))
        if len(self.y2_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.y2_labeled_nums = [y2 for y2 in self.y2_labeled_nums if y2 != 0]
            y2_axis.add_numbers(*self.y2_labeled_nums)
        if self.y2_axis_label:
            y2_label = TextMobject(self.y2_axis_label)
            y2_label.next_to(
                y2_axis.get_corner(UP + RIGHT), UP + RIGHT,
                buff=SMALL_BUFF
            )
            y2_label.shift_onto_screen()
            y2_axis.add(y2_label)
            self.y2_axis_label_mob = y2_label

        self.x_axis, self.y_axis, self.y2_axis = self.axes = VGroup(self.x_axis, self.y_axis, y2_axis)
        
        return self.reback_or_anim_axis(reback, animate, self.y2_axis)

    # 坐标到点
    def y2_coords_to_point(self, x, y2):
        assert(hasattr(self, "x_axis") and hasattr(self, "y2_axis"))
        result = self.x_axis.number_to_point(x)[0] * RIGHT
        result += self.y2_axis.number_to_point(y2)[1] * UP
        return result

    def y2_get_graph(
        self, func,
        color=None,
        x_min=None,
        x_max=None,
        **kwargs):
        if color is None:
            color = next(self.default_graph_colors_cycle)
        if x_min is None:
            x_min = self.x_min
        if x_max is None:
            x_max = self.x_max

        def parameterized_function(alpha):
            x = interpolate(x_min, x_max, alpha)
            y2 = func(x)
            if not np.isfinite(y2):
                y2 = self.y2_max
            return self.y2_coords_to_point(x, y2)

        graph = ParametricFunction(
            parameterized_function,
            color=color,
            **kwargs)
        graph.underlying_function = func
        return graph

class Plotyy1(YYaxis):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "y_tick_frequency" : 0.1, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,121,10),
        "y_labeled_nums": list(np.arange(0, 1.01, 0.1)),
        "x_num_decimal_places": 0,
        "y_num_decimal_places": 1,
        "x_axis_label": None,
        "y_axis_label": None,
        "y2_axis_label": None,
        "y2_labeled_nums": list(np.arange(0, 1001, 100)),
        "add_coordinate_grid":True
    }
    def construct(self):
        self.setup_axes(animate=True)
        y_graph = self.get_graph(lambda x : 1-0.99**x,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 100
                                    )

        y2_graph = self.y2_get_graph(lambda x : 10*x,  
                                    color = RED,
                                    x_min = 0, 
                                    x_max = 100
                                    )
        p1=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        p2=Dot().move_to(self.coords_to_point(self.x_max, self.y_min))
        self.add(p1,p2)

        y_graph.set_stroke(width=10)
        y2_graph.set_stroke(width=5)
        y_graph_label = self.get_graph_label(y_graph, label="1-0.99^N", x_val=90, direction=DOWN,buff=0.4)
        y2_graph_label = self.get_graph_label(y2_graph, label="10x", x_val=90, direction=UP,buff=0)

        self.play(
            ShowCreation(y_graph),
            ShowCreation(y2_graph),
            Write(y_graph_label),
            Write(y2_graph_label),
            run_time = 2
        )
        self.wait()

class PlotBarChart1(GraphFromData):
    CONFIG = {
        "x_max" : 8,
        "x_min" : 0,
        "y_max" : 30,
        "y_min" : 0,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 5, 
        "axes_color" : BLUE, 
        "x_axis_label": "x",
        "y_axis_label": "y",
    }
    def construct(self):
        self.setup_axes()
        x = [1, 2, 3, 4,  5,  6, 7]
        y = [2, 4, 6, 8, 10, 20, 25]

        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)

        bars = BarChartRectangle(points,0.618)
        bars.set_color_by_gradient(BLUE, YELLOW)
        self.play(
            LaggedStart(
                *[FadeIn(xy) for xy in it.chain(*bars)], 
            lag_ratio = 0.1618,
            run_time = 2
        ))
        self.wait()

class SimulateWaitTimes1(GraphFromData):
    CONFIG = {
        "x_max" : 50,
        "x_min" : 0,
        "y_max" : 1200,
        "y_min" : 0,
        "x_tick_frequency" : 5, 
        "y_tick_frequency" : 200, 
        "x_labeled_nums": range(0,51,5),
        "y_labeled_nums": range(0,1201,200),
        "axes_color" : BLUE, 
        "x_axis_label": "\\heiti{等待时间(min)}",
        "y_axis_label": "\\heiti{次数}",
        "add_coordinate_grid":True,
    }
    def construct(self):
        self.setup_axes()
        def data_N_wait_times(carSeed,npSeed,nP=100):
            N = 6 # 公交车数量
            tau = 10 # 平均到站间隔
            N_passengers = nP # 乘客数量
            rand = np.random.RandomState(carSeed)  # 随机种子
            bus_arrival_times = N * tau * np.sort(rand.rand(N))
            # intervals = np.append(np.diff(bus_arrival_times),N*tau-bus_arrival_times[-1]+bus_arrival_times[0])
            # print(bus_arrival_times,"\n",intervals,"\n-------------------------------")
            def simulate_wait_times(arrival_times,
                                    rseed=npSeed,  # Jenny的随机种子
                                    n_passengers=N_passengers):
                rand = np.random.RandomState(rseed)
                arrival_times = np.asarray(arrival_times)
                passenger_times = N * tau * rand.rand(n_passengers)
                # 为每个模拟乘客找到下一辆公交车
                w_times = np.array([])
                for p_time in passenger_times:
                    i = np.searchsorted(arrival_times, p_time, side='right')
                    if i < N:
                        w_times=np.append(w_times, arrival_times[i] - p_time)
                    if i == N:
                        w_times=np.append(w_times, N * tau - p_time + arrival_times.min())
                if np.any(w_times < 0):
                    raise Exception("程序有bug")
                return w_times
            wait_times = simulate_wait_times(bus_arrival_times) 
            return wait_times
        allWaitTimes=np.array([])
        for k in range(500,600,1):
            allWaitTimes=np.append(allWaitTimes,data_N_wait_times(k,8))
        print(len(allWaitTimes))
        print(mean(allWaitTimes))
        binsize = 1
        y = np.bincount((allWaitTimes // binsize).astype(int))
        x = [i for i in range(1,len(y)+1)]
        mean_line = self.get_vertical_line_to_axis(mean(allWaitTimes),color=RED,stroke_width=5)
        self.add(mean_line)
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        bars = BarChartRectangle(points,0.11,stroke_opacity=0.8)
        bars.set_color_by_gradient(YELLOW, RED)
        self.add(bars)
        self.wait()

class SimulateWaitTimes2(GraphFromData):
    CONFIG = {
        "x_max" : 50,
        "x_min" : 0,
        "y_max" : 1200,
        "y_min" : 0,
        "x_tick_frequency" : 5, 
        "y_tick_frequency" : 200, 
        "x_labeled_nums": range(0,51,5),
        "y_labeled_nums": range(0,1201,200),
        "axes_color" : BLUE, 
        "x_axis_label": "\\heiti{等待时间(min)}",
        "y_axis_label": "\\heiti{次数}",
        "add_coordinate_grid":True,
    }
    def construct(self):
        self.setup_axes()
        def data_N_wait_times(carSeed,npSeed,nP=100):
            N = 6 # 公交车数量
            tau = 10 # 平均到站间隔
            N_passengers = nP # 乘客数量
            rand = np.random.RandomState(carSeed)  # 随机种子
            bus_arrival_times = N * tau * np.sort(rand.rand(N))
            # intervals = np.append(np.diff(bus_arrival_times),N*tau-bus_arrival_times[-1]+bus_arrival_times[0])
            # print(bus_arrival_times,"\n",intervals,"\n-------------------------------")
            def simulate_wait_times(arrival_times,
                                    rseed=npSeed,  # Jenny的随机种子
                                    n_passengers=N_passengers):
                rand = np.random.RandomState(rseed)
                arrival_times = np.asarray(arrival_times)
                passenger_times = arrival_times.max() * rand.rand(n_passengers)
                # 为每个模拟乘客找到下一辆公交车
                i = np.searchsorted(arrival_times, passenger_times, side='right')
                return arrival_times[i] - passenger_times
            wait_times = simulate_wait_times(bus_arrival_times) 
            # print(wait_times.mean())
            return wait_times
        allWaitTimes=np.array([])
        for k in range(500,600,1):
            allWaitTimes=np.append(allWaitTimes,data_N_wait_times(k,8))
        print(len(allWaitTimes))
        print(mean(allWaitTimes))
        binsize = 1
        y = np.bincount((allWaitTimes // binsize).astype(int))
        x = [i for i in range(1,len(y)+1)]
        mean_line = self.get_vertical_line_to_axis(mean(allWaitTimes),color=RED,stroke_width=5)
        self.add(mean_line)
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        bars = BarChartRectangle(points,0.11,stroke_opacity=0.8)
        bars.set_color_by_gradient(YELLOW, RED)
        self.add(bars)
        self.wait()

class SimulateWaitTimes3(GraphFromData):
    CONFIG = {
        "x_max" : 40,
        "x_min" : 0,
        "y_max" : 1200,
        "y_min" : 0,
        "x_tick_frequency" : 5, 
        "y_tick_frequency" : 200, 
        "x_labeled_nums": range(0,41,5),
        "y_labeled_nums": range(0,1201,200),
        "axes_color" : BLUE, 
        "x_axis_label": "\\heiti{等待时间(min)}",
        "y_axis_label": "\\heiti{次数}",
        "add_coordinate_grid":True,
    }
    def construct(self):
        self.setup_axes()
        def data_N_wait_times(carSeed,npSeed,nP=10000):
            N_passengers = nP # 乘客数量
            bus_arrival_times = np.array([5,10,15,20,25,60])
            intervals = np.diff(bus_arrival_times)
            print(intervals.mean())
            def simulate_wait_times(arrival_times,
                                    rseed=npSeed,  # Jenny的随机种子
                                    n_passengers=N_passengers):
                rand = np.random.RandomState(rseed)
                arrival_times = np.asarray(arrival_times)
                passenger_times = arrival_times.max() * rand.rand(n_passengers)
                # 为每个模拟乘客找到下一辆公交车
                i = np.searchsorted(arrival_times, passenger_times, side='right')
                return arrival_times[i] - passenger_times
            wait_times = simulate_wait_times(bus_arrival_times) 
            # print(wait_times.mean())
            return wait_times
        allWaitTimes=np.array([])
        for k in range(99,100,1):
            allWaitTimes=np.append(allWaitTimes,data_N_wait_times(k,1))
        binsize = 1
        y = np.bincount((allWaitTimes // binsize).astype(int))
        x = [i for i in range(1,len(y)+1)]
        print(mean(allWaitTimes))
        mean_line = self.get_vertical_line_to_axis(mean(allWaitTimes),color=RED,stroke_width=5)
        self.add(mean_line)
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        bars = BarChartRectangle(points,0.12,stroke_opacity=0.8)
        bars.set_color_by_gradient(YELLOW, RED)
        self.add(bars)
        self.wait()

class PlotBarChart2(GraphFromData):
    CONFIG = {
        "x_max" : 8,
        "x_min" : 0,
        "y_max" : 30,
        "y_min" : -5,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 5, 
        "y_labeled_nums": range(-5,31,5),
        "axes_color" : BLUE, 
        "x_axis_label": "x",
        "y_axis_label": "y",
    }
    def construct(self):
        self.setup_axes()
        x0 = [1, 2, 3, 4,  5,  6, 7 ]
        y0 = [1e-3] * len(x0)
        y1 = [-1, 2, -5, 10, 10, 20, 25]
        y2 = [dy+4 for dy in y1]

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        points0 = self.get_points_from_coords(coords0)

        coords1 = [[px,py] for px,py in zip(x0,y1)]
        points1 = self.get_points_from_coords(coords1)

        coords2 = [[px,py] for px,py in zip(x0,y2)]
        points2 = self.get_points_from_coords(coords2)

        bars = BarChartRectangle(points0, 0.618)
        bars.set_color_by_gradient(YELLOW, RED)

        self.add(bars.set_opacity(0))
        self.play(
                bars.set_style,{"stroke_opacity":1,"fill_opacity":0.5},
                bars.change_bar_values,
                [dp[1] for dp in points1],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.play(
                bars.change_bar_values,
                [dp[1] for dp in points2],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.wait(2)

class PlotBarChart3(GraphFromData):
    CONFIG = {
        "x_max" : 8,
        "x_min" : 0,
        "y_max" : 30,
        "y_min" : 0,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 5, 
        "axes_color" : BLUE, 
        "x_axis_label": "x",
        "y_axis_label": "y",
        "graph_origin": 2.6 * DOWN + 4 * LEFT,
    }
    def construct(self):
        self.setup_axes()
        x0 = [1, 2, 3, 4,  5,  6, 7 ]
        y0 = [1e-3] * len(x0)
        y1 = [1, 2, 5, 10, 10, 20, 12]
        y2 = [dy+5 for dy in y1]

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        points0 = self.get_points_from_coords(coords0)

        coords1 = [[px,py] for px,py in zip(x0,y1)]
        points1 = self.get_points_from_coords(coords1)

        coords2 = [[px,py] for px,py in zip(x0,y2)]
        points2 = self.get_points_from_coords(coords2)

        bars = BarChartRectangle(points0, 0.618, graph_origin_down=self.graph_origin[1])
        bars.set_color_by_gradient(YELLOW, RED)

        self.add(bars.set_opacity(0))
        self.play(
                bars.set_style,{"stroke_opacity":1,"fill_opacity":0.5},
                bars.change_bar_values,
                [dp[1] for dp in points1],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.play(
                bars.change_bar_values,
                [dp[1] for dp in points2],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.wait(2)
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        
        values_decimal_y=[value_y for value_y in range(self.y_min, self.y_max+1, self.y_tick_frequency)]
        list_y = [*["%s"%i for i in values_decimal_y]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.y_axis.add(self.y_axis_labels)  

        values_decimal_x=[*[value_x for value_x in range(self.x_min+1, self.x_max, self.x_tick_frequency)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)   

        self.add(self.x_axis,self.y_axis)

class PlotBarChart4(GraphFromData):
    CONFIG = {
        "x_max" : 8,
        "x_min" : 0,
        "y_max" : 30,
        "y_min" : 0,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 5, 
        "axes_color" : BLUE, 
        "x_axis_label": "x(年/月)",
        "y_axis_label": "y",
        "graph_origin": 2.6 * DOWN + 4 * LEFT,
        "camera_config":{
                "frame_width": FRAME_WIDTH+8,
        },
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        x0 = [1, 2, 3, 4,  5,  6, 7 ]
        y0 = [1e-3] * len(x0)
        y1 = [1, 2, 5, 10, 10, 20, 12]
        y2 = [dy+5 for dy in y1]

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        points0 = self.get_points_from_coords(coords0)

        coords1 = [[px,py] for px,py in zip(x0,y1)]
        points1 = self.get_points_from_coords(coords1)

        coords2 = [[px,py] for px,py in zip(x0,y2)]
        points2 = self.get_points_from_coords(coords2)

        bars = BarChartRectangle(points0, 0.618, graph_origin_down=self.graph_origin[1])
        bars.set_color_by_gradient(YELLOW, RED)

        # 把内容全部合并
        allVG = VGroup(axes,bars)
        # 加入背景和文字
        allParts = ObjAnd1Text(
                allVG,
                "“相互宝”参与人数与时间的关系",
                dframe=0.3,
                txt_height=0.5,
        )
        # 展示进入
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFrom(allParts[2]),
                    lag_ratio=5
            )
        )    
        # 正常的动画
        self.add(bars.set_opacity(0))
        self.play(
                bars.set_style,{"stroke_opacity":1,"fill_opacity":0.5},
                bars.change_bar_values,
                [dp[1] for dp in points1],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.play(
                bars.change_bar_values,
                [dp[1] for dp in points2],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.wait(2)

        # 渐隐消失
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))
        
    def setup_axes(self, reback=False):
        GraphScene.setup_axes(self)
  
        values_decimal_y=[value_y for value_y in range(self.y_min, self.y_max+1, self.y_tick_frequency)]
        list_y = [*["%s"%i for i in values_decimal_y]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.y_axis.add(self.y_axis_labels)  

        values_decimal_x=[*[value_x for value_x in range(self.x_min+1, self.x_max, self.x_tick_frequency)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)   

        if reback:
            return VGroup(self.x_axis, self.y_axis)

class PlotBarChart5G1(GraphFromData):
    CONFIG = {
        "x_max" : 15,
        "x_min" : 0,
        "y_max" : 80,
        "y_min" : 0,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_axis_label": "x(年/月)",
        "y_axis_label": "y(占比)",
        "graph_origin": 2.6 * DOWN + 4 * LEFT,
        "camera_config":{
                "frame_width": FRAME_WIDTH+8,
        },
    }
    def construct(self):
        axes = self.setup_axes(reback=True)

        coords = get_coords_from_csv(r"Ag\MyCode\DataFile\data5G")
        points1 = self.get_points_from_coords(coords)
        # Set graph
        graph = SmoothGraphFromSetPoints(points1,color=WHITE)
        graph.set_stroke(width=5)
        graph_dash = DashedVMobject(graph,num_dashes=50,positive_space_ratio=0.618)

        x0 = [num for num in range(1,15)]
        y0 = [1e-3] * len(x0)

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        points0 = self.get_points_from_coords(coords0)

        bars = BarChartRectangle(points0, 0.4, graph_origin_down=self.graph_origin[1])
        bars.set_color_by_gradient(YELLOW, RED)

        # 把内容全部合并
        allVG = VGroup(axes,bars,graph_dash)
        # 加入背景和文字
        allParts = ObjAnd1Text(
                allVG,
                "中国5G手机出货量占比",
                dframe=0.4,
                txt_height=0.5,
        )
        # 展示进入
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFrom(allParts[2]),
                    lag_ratio=5
            )
        )    
        # 正常的动画
        self.add(bars.set_opacity(0))
        self.play(
                bars.set_style,{"stroke_opacity":1,"fill_opacity":0.5},
                bars.change_bar_values,[dp[1] for dp in points1],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.play(ShowCreation(graph_dash),run_time=3)
        self.wait(2)

        # 渐隐消失
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))
        
    def setup_axes(self, reback=False):
        GraphScene.setup_axes(self)
  
        values_decimal_y=[value_y for value_y in range(self.y_min, self.y_max+1, self.y_tick_frequency)]
        list_y = [*["%s"%i for i in values_decimal_y]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.y_axis.add(self.y_axis_labels)  

        values_decimal_x=[*[value_x for value_x in range(self.x_min+1, self.x_max, self.x_tick_frequency)]]
        list_x = [
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            "2020/09",
            "2020/10",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)   

        if reback:
            return VGroup(self.x_axis, self.y_axis)

class PlotBarChart5G2(GraphFromData):
    CONFIG = {
        "x_max" : 15,
        "x_min" : 0,
        "y_max" : 80,
        "y_min" : 0,
        "x_tick_frequency" : 1, 
        "y_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_axis_label": "x(年/月)",
        "y_axis_label": "y(中国5G手机出货量占比)",
        "graph_origin": 2.6 * DOWN + 4 * LEFT,
        "camera_config":{
                "frame_width": FRAME_WIDTH+3,
        },
    }
    def construct(self):
        axes = self.setup_axes(reback=True)

        coords = get_coords_from_csv(r"Ag\MyCode\DataFile\data5G")
        points1 = self.get_points_from_coords(coords)
        # Set graph
        graph = SmoothGraphFromSetPoints(points1,color=WHITE)
        graph.set_stroke(width=5)
        graph_dash = DashedVMobject(graph,num_dashes=50,positive_space_ratio=0.618)

        x0 = [num for num in range(1,15)]
        y0 = [1e-3] * len(x0)

        coords0 = [[px,py] for px,py in zip(x0,y0)]
        points0 = self.get_points_from_coords(coords0)

        bars = BarChartRectangle(points0, 0.4, graph_origin_down=self.graph_origin[1])
        bars.set_color_by_gradient(YELLOW, RED)

        # 正常的动画
        self.add(bars.set_opacity(0))
        self.play(
                bars.set_style,{"stroke_opacity":1,"fill_opacity":0.5},
                bars.change_bar_values,[dp[1] for dp in points1],
                lag_ratio = 0.5,
                run_time = 2
            )
        self.play(ShowCreation(graph_dash),run_time=3)
        self.wait(2)
        
    def setup_axes(self, reback=False):
        GraphScene.setup_axes(self)
  
        values_decimal_y=[value_y for value_y in range(self.y_min, self.y_max+1, self.y_tick_frequency)]
        list_y = [*["%s"%i for i in values_decimal_y]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.y_axis.add(self.y_axis_labels)

        values_decimal_x=[*[value_x for value_x in range(self.x_min+1, self.x_max, self.x_tick_frequency)]]
        list_x = [
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            "2020/09",
            "2020/10",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)   

        if reback:
            return VGroup(self.x_axis, self.y_axis)

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "y_tick_frequency" : 0.1, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,121,10),
        "y_labeled_nums": list(np.arange(0, 1.01, 0.1)),
        "x_num_decimal_places": 0,
        "y_num_decimal_places": 1,
        "x_axis_label": "$N(year)$",
        "y_axis_label": "$P(probability)$",
        "add_coordinate_grid":True,
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : 1-0.99**x,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 100
                                    )

        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)

        graph.set_stroke(width=10)

        graph_label = self.get_graph_label(graph, label="1-0.99^N", direction=UP+LEFT,buff=0)

        self.play(
        	ShowCreation(graph),
            ShowCreation(graph_label),
            run_time = 2
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "y_tick_frequency" : 0.1, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,121,10),
        "x_num_decimal_places": 0,
        "x_axis_label": "$N(year)$",
        "y_axis_label": "$P(probability)$",
        "add_coordinate_grid":True
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : 1-0.99**x,  
                                    color = RED,
                                    x_min = 0, 
                                    x_max = 100
                                    )

        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph.set_stroke(width=10)
        graph_label = self.get_graph_label(graph, label="1-0.99^N", direction=UP+LEFT,buff=0)
        self.play(
        	ShowCreation(graph),
            Write(graph_label),
            run_time = 3.6
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        values_decimal_y=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
        list_y = [*["%s"%i for i in range(10,101,10)]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.add(self.y_axis_labels)

class Plot3(GraphFromData):
    CONFIG = {
        "y_max" : 14000,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : 0,
        "y_tick_frequency" : 2000, 
        "x_tick_frequency" : 2,
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,14001,2000),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{时间(年/月)}",
        "y_axis_label": "\\heiti{参与分摊人数(万人)}",
        "add_coordinate_grid":True
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData1")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.618).shift(LEFT*0.8+UP*0.2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”参与人数与时间的关系",
                        dframe=0.2618
            )

        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFrom(allParts[2]),
                        lag_ratio=5
                )
            )        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)
        # self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

    def setup_axes(self, reback=False):
        GraphScene.setup_axes(self)
        values_decimal_x=[*[i for i in range(6,46,2)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            "2019/08",
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)
        
        # 必须开启add_coordinate_grid
        if reback:
            return VGroup(self.lines_x_axis, self.lines_y_axis, self.x_axis, self.y_axis,)
        else:
            self.add(self.lines_x_axis, self.lines_y_axis, self.x_axis, self.y_axis,)

class Plot31(GraphFromData):
    CONFIG = {
        "y_max" : 14000,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : 0,
        "y_tick_frequency" : 2000, 
        "x_tick_frequency" : 2, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,14001,2000),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{时间(年/月)}",
        "y_axis_label": "\\heiti{参与分摊人数(万人)}",
        "add_coordinate_grid":True
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData1")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.7).shift(LEFT*0.8+UP*0.618)
        text = Text("“相互宝”参与人数与时间的关系",size=0.4,color=ORANGE).next_to(allVG,DOWN)

        self.play(
            FadeInFromLarge(text),
            FadeInFromLarge(axes))        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)

    def setup_axes(self,reback=False):
        GraphScene.setup_axes(self)
        values_decimal_x=[*[i for i in range(6,46,2)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            "2019/08",
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)
        if reback:
            return VGroup(self.lines_x_axis, self.lines_y_axis, self.x_axis, self.y_axis)

class Plot4(GraphFromData):
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : 1,
        "y_tick_frequency" : 1000, 
        "x_tick_frequency" : 2, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,6,1),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{时间(年/月)}",
        "y_axis_label": "\\heiti{分摊金(元/期)}",
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData2")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=RED).make_smooth()
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.618).shift(LEFT*0.8+UP*0.2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”人均分摊金额变化规律"         
            )

        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)
        # self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

    def setup_axes(self,reback=False):
        GraphScene.setup_axes(self)
        values_decimal_x=[*[i for i in range(6,46,2)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            "2019/08",
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.x_axis.add(self.x_axis_labels)
        if reback:
            return VGroup(self.x_axis, self.y_axis)

class Plot5(GraphFromData):
    CONFIG = {
        "y_max" : 1800,
        "y_min" : 0,
        "x_max" : 70,
        "x_min" : 0,
        "y_tick_frequency" : 200, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,70,10),
        "y_labeled_nums": range(0,1800,200),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{年龄(岁)}",
        "y_axis_label": "\\heiti{纯保费(元)}",
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData3")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points[:40],color=RED)
        graph2 = DiscreteGraphFromSetPoints(points[40:],color=RED)
        graph3 = DiscreteGraphFromSetPoints(points[39:41],color=RED)
        graph3_dash = DashedVMobject(graph3,num_dashes=6)
        graph1.set_stroke(width=10)
        graph2.set_stroke(width=10)
        graph3_dash.set_stroke(width=10)

        allVG = VGroup(axes,graph1,graph2,graph3,graph3_dash).scale(0.618).shift(LEFT*0.8)

        allParts = ObjAnd1Text(
                        allVG,
                        "纯保费与年龄的关系图"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )
        
        self.play(ShowCreation(graph1,run_time=4))
        self.play(ShowCreation(graph3_dash,run_time=1))
        self.play(ShowCreation(graph2,run_time=4))

        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))
 
class Plot6(Scene):
    def construct(self):
        r=1.618
        circle1 = Circle(
                        radius=r,
                        stroke_color=GRAY,
                        fill_color=GRAY,
                        fill_opacity=1)
        arc1 = Sector(
                        inner_radius=0,
                        outer_radius=r,
                        angle=29.6*TAU/100,
                        start_angle=0,
                        stroke_color=ORANGE,
                        fill_color=ORANGE,
                        fill_opacity=1)
        arc2 = Sector(
                        inner_radius=0,
                        outer_radius=r,
                        angle=28.4*TAU/100,
                        start_angle=-28.4*TAU/100,
                        stroke_color=YELLOW,
                        fill_color=YELLOW,
                        fill_opacity=1)

        txt1 = Text("80's",color=BLACK,size=0.382)
        text1 = Text("29.6%",color=RED,size=0.618)
        txt2 = Text("90's",color=BLACK,size=0.382)
        text2 = Text("28.4%",color=RED,size=0.618)

        txt1.move_to(arc1)
        txt2.move_to(arc2)

        polyline1 = VMobject()
        position1 = [ORIGIN,0.236*UR,0.236*UR+2.2*RIGHT]
        polyline1.set_points_as_corners(position1)
        polyline1.set_color(RED).next_to(arc1,UR,buff=-0.6)
        text1.next_to(polyline1,UP,buff=0.2,aligned_edge=RIGHT)

        polyline2 = VMobject()
        position2 = [ORIGIN,0.236*DR,0.236*DR+2.2*RIGHT]
        polyline2.set_points_as_corners(position2)
        polyline2.set_color(RED).next_to(arc2,DR,buff=-0.6)
        text2.next_to(polyline2,UP,buff=-0.04,aligned_edge=RIGHT)

        Tx1 = Text("80后",size=0.36).next_to(text1,DOWN,buff=0.3,aligned_edge=RIGHT)
        Tx2 = Text("90后",size=0.36).next_to(text2,DOWN,buff=0.3,aligned_edge=RIGHT)

        Txt = Text("成员以80、90后社会中坚为主",font="宋体",size=0.42).next_to(polyline2.get_left(),DOWN,buff=1.2).shift(0.5*LEFT)
        Txtsrr = Underline(Txt,color=RED,stroke_width=1)
        allVG = VGroup(circle1,arc1,arc2,txt1,txt2,polyline1,text1,polyline2,text2,Tx1,Tx2,Txt,Txtsrr).move_to(ORIGIN).scale(0.8)

        group1 = VGroup(arc1,txt1,polyline1,Tx1)
        group2 = VGroup(arc2,txt2,polyline2,Tx2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”成员年龄构成"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(circle1),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )
        
        self.play(Write(group1),run_time=2)
        self.wait()
        self.play(Indicate(text1,color=RED))
        self.wait()
        self.play(Write(group2),run_time=2)
        self.wait()
        self.play(Indicate(text2,color=RED))
        self.wait()
        self.play(Write(Txt),ShowCreation(Txtsrr))

        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

class Table1(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK},   
    }
    def construct(self):
        data = get_coords_from_csvdata(r"Ag\MyCode\InsuranceData4")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        x, y, dx, dy = -column+1, 3, 2, 0.5
        dataTxt = []
        dataTxtBackground = []
        for i in range(row):
            for j in range(column):
                target_ij = Text(dataArray[i][j])
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.35)
                target_ij.shift(np.array([x+j*dx,y-i*dy,0]))
                dataTxt.append(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.236,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-int(column/2)*dx,0,0]))
                dataTxtBackground.append(target_i)
 
        allGroupHead = VGroup(
            dataTxtBackground[0],
            dataTxtBackground[0].copy(),
            *dataTxt[:column]
            )
        
        allGroup = VGroup(
            dataTxtBackground[0].copy(),
            *dataTxtBackground,
            *dataTxt,
            )

        self.play(
            FadeInFromDirections(allGroup[0]),
            FadeInFromDirections(dataTxtBackground[0]),
            FadeInFromDirections(dataTxt[:column])
            )
        self.play(
                LaggedStartMap(FadeIn,[obj for obj in dataTxt[column:]],lag_ratio=0.2),
                LaggedStartMap(FadeIn,[obj for obj in dataTxtBackground[1:]],lag_ratio=0.1),
                run_time=3
            )

        VGroupHeadForeground=VGroup(
                Rectangle(
                    width=column*dx,
                    # +2是向上增加
                    height=dy+2,
                    color=self.camera_config["background_color"],
                    fill_color=self.camera_config["background_color"],
                    fill_opacity=1,
                    ).align_to(allGroupHead,DOWN),
                *allGroupHead
                )
        
        self.play(
            allGroup.remove(*allGroupHead).shift,(row-12)*dy*UP,
            VGroupHeadForeground.shift,ORIGIN,
            rate_func=linear,
            run_time=5
            )

        self.wait(5)    

class Insurance1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/1、腓尼基希波商帆船",
                        "腓尼基“希波”商帆船"         
            )
        palyALL1(self,allParts)

class Insurance2(Scene):
    def construct(self):
        allParts = ObjAnd2Text(
                        "Insurance/2、伦敦大火",
                        "Great Fire of London",
                        "伦敦博物馆藏图：1666年伦敦大火",
                        dframe=0.24,
                        txt_height=0.28,
            )
        palyALL2(self,allParts)

class Insurance3(Scene):
    def construct(self):
        allParts = ObjAnd2Text(
                        "Insurance/3、尼古拉斯巴蓬",
                        "Nicholas Barbon",
                        "尼古拉斯·巴蓬",
                        dframe=0.2,
                        txt_height=0.24,  
            )
        palyALL2(self,allParts)

class Insurance4(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/4、某火灾保险公司的消防标志",
                        "某火灾保险公司的消防标志"         
            )
        palyALL1(self,allParts)

class Insurance5(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/5、主要国家保险市场份额变化",
                        "主要国家保险市场份额变化"         
            )
        palyALL1(self,allParts)

class Tmp1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "pic/都江堰",
                        "都江堰地图显示"         
            )
        palyALL1(self,allParts)
