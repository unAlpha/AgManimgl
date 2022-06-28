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

class ImageShift(Scene):
    def construct(self):
        us_image = ImageMobject("GNI_icon/United States", height=0.5).shift(LEFT_SIDE)
        rect = Rectangle(
                height=0.6,
                color=BLUE,
                # fill_color=BLUE,
                # fill_opacity=1,
            ).shift(LEFT_SIDE).set_opacity(0.68)
        self.play(
                rect.animate.move_to(ORIGIN),
                us_image.animate.move_to(ORIGIN), 
                rate_func = linear, 
                run_time=5
            )

class ValueTrackerTest(Scene):
    def construct(self):
        val = ValueTracker(1)
        Txt = DecimalNumber(val.get_value(),font_size=150).add_updater(lambda v: v.set_value(val.get_value()))
        self.add(Txt)
        # self.play(val.animate.set_value(10))
        self.play(val.set_value,10)
        
class demo(Scene):
    def construct(self):
        square = Square(side_length=2.0)
        brace = BraceLabel(
            obj=square,
            text="a = 2.0",
            brace_direction=UP
        )
        self.add(square, brace)

if __name__ == "__main__":
    from os import system
    system("manimgl {} demo -os".format(__file__))