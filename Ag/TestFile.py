from manimlib import *
import colorsys

def random_color(lightness):
    col = list(map(
            lambda x: hex(x).split('x')[1].zfill(2), 
            tuple(round(i * 255) for i in colorsys.hsv_to_rgb(
                        random.random(),
                        random.random(),
                        lightness
        ))))
    return "#%s%s%s"%(col[0],col[1],col[2])

def get_dots(coords):
    return VGroup(*[Dot(np.array([x,y,z])) for x,y,z in coords])

def get_dot_numbers(dots):
    return VGroup(*[
                Text(f"{n}",font_size=10,).next_to(dot,dot.get_center(),buff=0.1)
                for n,dot in zip(range(1,len(dots)+1),dots)
            ]
        )

class RectPointsTest(Scene):
    def construct(self):
        rect = RoundedRectangle(
                height = 6,
                width = 2,
                corner_radius= 1,
                fill_color = RED,
                fill_opacity = 1,
                stroke_width = 1,
            )
        rect_points = self.get_dots(rect.data["points"])
        rect_points_anchors = self.get_dots(rect.get_start_anchors(), customize_color = RED)
        rect_cubic_ezier = self.cubic_ezier(rect)
        rect_points_nums = self.get_dot_numbers(rect_points)
        self.add(
                rect, 
                rect_points, 
                rect_points_nums, 
                rect_points_anchors,
                rect_cubic_ezier,
            )
        points = rect.data["points"]
        print(points)
        self.wait()

    def cubic_ezier(self, mob):
        mob_points = mob.get_points()
        return VGroup(*[
                CubicBezier(
                        # *[RIGHT,2*LEFT,2*DOWN,UP]
                        *mob_points[i*3:(i+1)*3+1:],
                        color = random_color(0.8)
                    ) for i in range(int(len(mob_points)/4)
            )])

    def get_dots(self, coords, customize_color = BLUE):
        return VGroup(*[Dot(
                    np.array([x,y,z]),
                    radius = DEFAULT_DASH_LENGTH,
                    color = customize_color, 
                    fill_opacity = 0.68
                ) for x,y,z in coords]
            )

    def get_dot_numbers(self, dots):
        return VGroup(*[
                    Text(f"{n}",font_size=10,).next_to(dot,dot.get_center(),buff=0.1)
                    for n,dot in zip(range(0,len(dots)),dots)
            ])

class LinePointsTest(Scene):
    def construct(self):
        line = Line(
                LEFT*4,RIGHT*4,
            )
        line_points = get_dots(line.data["points"])
        line_points_nums = get_dot_numbers(line_points)
        self.add(line, line_points, line_points_nums)
        points = line.data["points"]
        print(len(points))
        self.wait()

# 这个CubicBezier类是多阶的
class CubicBezierTest(Scene):
    def construct(self):
        cubic_bezier = CubicBezier(
                *[RIGHT,2*LEFT,2*DOWN,UP],
                color=random_color(0.8)
            )
        self.add(cubic_bezier)
        self.wait()

