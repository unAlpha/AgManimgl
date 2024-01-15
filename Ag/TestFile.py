from manimlib import *
import colorsys


def random_color(lightness):
    col = list(
        map(
            lambda x: hex(x).split("x")[1].zfill(2),
            tuple(
                round(i * 255)
                for i in colorsys.hsv_to_rgb(
                    random.random(), random.random(), lightness
                )
            ),
        )
    )
    return "#%s%s%s" % (col[0], col[1], col[2])


def get_dots(coords):
    return VGroup(*[Dot(np.array([x, y, z])) for x, y, z in coords])


def get_dot_numbers(dots):
    return VGroup(
        *[
            Text(
                f"{n}",
                font_size=10,
            ).next_to(dot, dot.get_center(), buff=0.1)
            for n, dot in zip(range(1, len(dots) + 1), dots)
        ]
    )


class RectPointsTest(Scene):
    def construct(self):
        rect = RoundedRectangle(
            height=6,
            width=2,
            corner_radius=1,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=1,
        )
        rect_points = self.get_dots(rect.data["points"])
        rect_points_anchors = self.get_dots(
            rect.get_start_anchors(), customize_color=RED
        )
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
        return VGroup(
            *[
                CubicBezier(
                    # *[RIGHT,2*LEFT,2*DOWN,UP]
                    *mob_points[i * 3 : (i + 1) * 3 + 1 :],
                    color=random_color(0.8),
                )
                for i in range(int(len(mob_points) / 4))
            ]
        )

    def get_dots(self, coords, customize_color=BLUE):
        return VGroup(
            *[
                Dot(
                    np.array([x, y, z]),
                    radius=DEFAULT_DASH_LENGTH,
                    color=customize_color,
                    fill_opacity=0.68,
                )
                for x, y, z in coords
            ]
        )

    def get_dot_numbers(self, dots):
        return VGroup(
            *[
                Text(
                    f"{n}",
                    font_size=10,
                ).next_to(dot, dot.get_center(), buff=0.1)
                for n, dot in zip(range(0, len(dots)), dots)
            ]
        )


class LinePointsTest(Scene):
    def construct(self):
        line = Line(
            LEFT * 4,
            RIGHT * 4,
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
            *[RIGHT, 2 * LEFT, 2 * DOWN, UP], color=random_color(0.8)
        )
        self.add(cubic_bezier)
        self.wait()


class ImageShift(Scene):
    def construct(self):
        us_image = ImageMobject("GNI_icon/United States", height=0.5).shift(LEFT_SIDE)
        rect = (
            Rectangle(
                height=0.6,
                color=BLUE,
                # fill_color=BLUE,
                # fill_opacity=1,
            )
            .shift(LEFT_SIDE)
            .set_opacity(0.68)
        )
        self.play(
            rect.animate.move_to(ORIGIN),
            us_image.animate.move_to(ORIGIN),
            rate_func=linear,
            run_time=5,
        )


class ValueTrackerTest(Scene):
    def construct(self):
        val = ValueTracker(1)
        Txt = DecimalNumber(val.get_value(), font_size=150).add_updater(
            lambda v: v.set_value(val.get_value())
        )
        self.add(Txt)
        # self.play(val.animate.set_value(10))
        self.play(val.set_value, 10)


class demo(Scene):
    def construct(self):
        square = Square(side_length=2.0)
        brace = BraceLabel(obj=square, text="a = 2.0", brace_direction=UP)
        self.add(square, brace)


class AxesLabelsTex(Axes):
    def add_coordinate_labels(self, **kwargs):
        x_numbers = self.get_x_axis().get_tick_range()
        y_numbers = self.get_y_axis().get_tick_range()
        self.coordinate_labels = VGroup()
        for number in x_numbers:
            axis = self.get_x_axis()
            value = number
            number_mob = axis.get_number_mobject(value, **kwargs)
            self.coordinate_labels.add(number_mob)
        for number in y_numbers:
            value = number
            axis = self.get_y_axis()
            kwargs["unit_tex"] = "\\%"
            number_mob = axis.get_number_mobject(value, **kwargs)
            self.coordinate_labels.add(number_mob)
        self.add(self.coordinate_labels)
        return self


class CustomGraph(Scene):
    def construct(self):
        axes = AxesLabelsTex(
            (0, 7, 1),
            (
                0,
                110,
                20,
            ),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 4,
                "tip_config": {
                    "width": 0.2,
                    "length": 0.36,
                },
                "include_tip": True,
            },
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 0,
                },
            },
        )

        axes.add_coordinate_labels()

        axes.lines_x_axis = VGroup()
        axes.lines_y_axis = VGroup()
        x_p = [x for x in np.arange(*axes.x_range)]
        x_p.append(axes.x_axis.x_max)
        y_p = [x for x in np.arange(*axes.y_range)]
        y_p.append(axes.y_axis.x_max)
        for x_point in list(zip(x_p, [axes.y_axis.x_max] * len(x_p), [0] * len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point), color=GREY_D))
        for x_point in list(zip(x_p, [-axes.y_axis.x_max] * len(x_p), [0] * len(x_p))):
            axes.lines_x_axis.add(axes.get_v_line(axes.c2p(*x_point), color=GREY_D))
        for y_point in list(zip([axes.x_axis.x_max] * len(y_p), y_p, [0] * len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point), color=GREY_D))
        for y_point in list(zip([-axes.x_axis.x_max] * len(y_p), y_p, [0] * len(y_p))):
            axes.lines_y_axis.add(axes.get_h_line(axes.c2p(*y_point), color=GREY_D))

        self.add(axes.scale(0.8))


class PlotBarChart3(Scene):
    def construct(self):
        y1 = [-1, 2, -5, 10, 10, 20, 25]
        y2 = [3, 5, 5, 5, 5, 6, 5]
        # 内置BarChart不适合负数
        barsin = BarChart(y1, max_value=None)
        self.add(barsin)
        self.play(barsin.animate.change_bar_values(y2))
        self.wait(2)


class CoinFlips(Scene):
    def construct(self):
        eq = TexText(
            "$${\\# \\text{一1试试下} adf \\over \\# \\text{一二三}} = $$",
            # "$$s=v_{0}\\left(t_{1}+t_{2}{ }^{\\prime}+\\frac{1}{2} t_{2}{ }^{\\prime \\prime}\\right)+\\frac{v_{0}^{2}}{2 a_{m}}-\\frac{a_{m} t_{2}^{\\prime \\prime 2}}{24}$$"
            # "{Num \\over Den}", "=", "0.500",
            # "{\\text{132}}",
            isolate={"Num", "Den", "\\# \\text{Heads}"},
            template="american_typewriter",
        )
        words = TexText("$$Vector...$$").next_to(eq, DOWN)
        self.add(eq)
        self.play(ShowCreation(words))
        self.wait()


class MyCone(Surface):
    CONFIG = {
        "resolution": (101, 51),
        "radius": 1,
        "u_range": (0, 1),
        "v_range": (0, 2 * PI),
    }

    def uv_func(self, u: float, v: float) -> np.ndarray:
        return self.radius * np.array([u * np.cos(v), u * np.sin(v), u])


class MyCone2(Surface):
    CONFIG = {
        "resolution": (101, 51),
        "radius": 1,
        "u_range": (0, 1),
        "v_range": (0, 2 * PI),
    }

    def uv_func(self, u: float, v: float) -> np.ndarray:
        return self.radius * np.array([0.25 + u * np.cos(v), u * np.sin(v), 0.5 - u])


class MySceneR(Scene):
    def construct(self):
        text = Tex(r"\fontfamily{Helvetica}\text{Some Text}")
        # title = Text(
        #         "哈哈",
        #         font_size=36,
        #         font="Source Han Sans CN Regular",
        #     )
        self.add(text)


# fill_color=["#032348","#46246d","#31580a","#852211",]


class Bg(Scene):
    def construct(self):
        bg = FullScreenRectangle()
        colors = [
            "#032348",
            "#46246d",
            "#31580a",
            "#852211",
        ]
        bg.set_color_by_gradient(*colors)
        mark = TexText(r"\color{red}{$\surd$}")
        self.add(bg)
        self.add(mark)


class demo(Scene):
    def construct(self):
        tex = TexText(
            r"LSTM神经单元数学关系：",
            r"""晃
            $\begin{aligned} f_t&=\sigma(W_{f}x_t+U_fh_{t-1}+b_f)\\ 
            i_t&=\sigma(W_ix_t+U_ih_{t-1}+b_i)\\ 
            o_t&=\sigma(W_ox_t+U_oh_{t-1}+b_o)\\ 
            g_t&=\tanh(W_gx_t+U_gh_{t-1}+b_g)\\
                \\ 
            c_t&=c_{t-1}\odot f_t+i_t\odot g_t\\ 
            h_t&=o_t\odot \tanh(c_t) \end{aligned}$\\
            """,
        )
        self.add(tex)


class demo2(Scene):
    def construct(self):
        sf = Prism()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(sf)


if __name__ == "__main__":
    from os import system

    system("manimgl {} demo2 -os".format(__file__))
