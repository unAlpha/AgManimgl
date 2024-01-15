from manimlib import *


def get_coords_from_csv(file_name):
    import csv

    coords = []
    with open(f"{file_name}.csv", "r", encoding="UTF-8") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x, y = row
            coord = [float(x), float(y)]
            coords.append(coord)
    csvFile.close()
    return coords


def get_coords_from_csvdata(file_name):
    import csv

    coords = []
    with open(f"{file_name}.csv", "r", encoding="UTF-8") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords


class Table:
    def __init__(
        self,
        text,
        file_path,
        dx=2.6,
        dy=0.6,
        gap=2e-2,
        txfont="Microsoft JhengHei",
        title_font="Source Han Sans",
        txt_color=WHITE,
        title_buff=0.5,
        no_focus=False,
        all_op=0.5,
    ):
        self.dx = dx
        self.dy = dy
        self.gap = gap
        self.txfont = txfont
        self.title_font = title_font
        self.title_buff = title_buff
        self.txt_color = txt_color
        self.no_focus = no_focus
        self.all_op = all_op
        self.title = Text(text, font_size=50, font=title_font, weigth="BOLD")
        data = get_coords_from_csvdata(file_path)
        self.dataArray = np.array(data)
        self.row = self.dataArray.shape[0]
        self.column = self.dataArray.shape[1]
        # 统一设置高度
        self.dx_list = [self.dx] * self.column
        self.dy_list = [self.dy] * self.row

    def arrange_table(self):
        dataTxt = VGroup()
        dataTxtBackground = VGroup()
        for i, dyy in zip(range(self.row), self.dy_list):
            for j, dxx in zip(range(self.column), self.dx_list):
                if i == 0 and self.no_focus == False:
                    target_ij = Text(
                        str(self.dataArray[i, j]),
                        font="Sans",
                        weigth="BLOD",
                        color=YELLOW,
                        font_size=30,
                    )
                else:
                    target_ij = Text(
                        str(self.dataArray[i, j]),
                        font=self.txfont,
                        weigth="Regular",
                        color=self.txt_color,
                        font_size=22,
                    )
                target_ij.shift(
                    np.array(
                        [
                            sum(self.dx_list[0 : j + 1]) - dxx / 2,
                            -(sum(self.dy_list[0 : i + 1]) - dyy / 2),
                            0,
                        ]
                    )
                )
                dataTxt.add(target_ij)
                if (i + 1) % 2:
                    fop = 0.2 + self.all_op
                else:
                    fop = 0.1 + self.all_op
                target_i = Rectangle(
                    width=dxx - self.gap,
                    height=dyy - self.gap,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=fop,
                    stroke_opacity=0,
                    # stroke_color=WHITE,
                    # stroke_width=DEFAULT_STROKE_WIDTH/2,
                ).move_to(target_ij)
                dataTxtBackground.add(target_i)
        dataTxtBackground[0 : self.column].set_style(fill_opacity=0.618 + self.all_op)
        self.table = VGroup(dataTxtBackground, dataTxt).center()

        self.tex_column = VGroup()
        self.bg = VGroup()
        for i in range(0, len(dataTxt), self.column):
            self.tex_column.add(dataTxt[i : i + self.column])
            self.bg.add(dataTxtBackground[i : i + self.column])

        self.title.next_to(self.table, UP, buff=self.title_buff)

    def replace_part(self, locAcontent, fonsz=22):
        """
        # locAcontent = (
        #     ([1,1], "\\frac{9}{100} \\times \\frac{99}{100} ", RED),
        #     ([1,2], "\\frac{91}{100} \\times \\frac{1}{100} ", YELLOW_E),)
        """
        for x, y, z in locAcontent:
            if y == "":
                x.set_color(z)
            else:
                x.become(
                    Tex(
                        y,
                        color=z,
                        font_size=fonsz,
                    ).move_to(x)
                )

    def merger_part(self, locs, op=0):
        """
        # loc = ([0,1],[0,2])
        """
        locs_Vg = VGroup()
        for loc in locs:
            locs_Vg.add(self.bg[loc[0]][loc[1]])
        center = locs_Vg.get_center()
        center_height = locs_Vg.get_height()
        center_width = locs_Vg.get_width()

        for i, loc in enumerate(locs):
            if i == op:
                continue
            self.bg[loc[0]][loc[1]].become(VMobject())

        self.bg[locs[op][0]][locs[op][1]].stretch_to_fit_height(center_height)
        self.bg[locs[op][0]][locs[op][1]].stretch_to_fit_width(center_width)
        self.bg[locs[op][0]][locs[op][1]].move_to(center).set_style(
            fill_opacity=0.36 + self.all_op, fill_color=BLUE
        )
        self.tex_column[locs[0][0]][locs[0][1]].move_to(center).scale(1.2)


class AutoGPTvsChatGPT2(Scene):
    title = "AutoGPT VS ChatGPT"
    path = r"Z:\PengVideo\短视频\4月份\8_autoGPT实战\得分"

    def construct(self):
        ble = Table(
            self.title,
            self.path,
            dx=1.8,
            dy=0.618,
            gap=3e-2,
        )
        ble.dy_list[0] = 0.86
        ble.dx_list[0] = 1.6
        ble.dx_list[3] = 2.4
        ble.dx_list[-1] = 1.6
        ble.arrange_table()
        ble.table.scale(0.86).shift(UP * 0.2).center()
        ble.title.scale(1).next_to(ble.table, UP, buff=MED_LARGE_BUFF)
        ble.merger_part([[1, 0], [2, 0]])
        ble.merger_part([[3, 0], [4, 0]], op=1)
        ble.merger_part([[5, 0], [6, 0]])
        # ble.srdrect = SurroundingRectangle(ble.table,color=BLACK,buff=0.002)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        # frame = self.camera.frame
        # frame.scale(0.8)
        toend = 3
        self.play(
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            FlashAround(ble.bg[0:toend]),
            LaggedStartMap(FadeIn, ble.bg[0:toend], scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column[0], scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column[1][0:2], scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column[2][0:2], scale=0.9, lag_ratio=0.1),
            run_time=1,
        )

        self.wait(1)
        for i in range(2, 8):
            self.play(
                Write(ble.tex_column[1][i], scale=0.5),
                Write(ble.tex_column[2][i], scale=0.5),
            )
            self.play(
                FlashAround(ble.tex_column[1][i]),
                FlashAround(ble.tex_column[2][i]),
                run_time=2,
            )
            self.wait(3)
        self.play(
            LaggedStartMap(FadeIn, ble.bg[3:7], shift=UP, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column[3:7], shift=UP, lag_ratio=0.1),
        )
        self.wait(5)


class GPTsummary(Scene):
    title = "AutoGPT VS ChatGPT 总结"
    path = r"Z:\PengVideo\短视频\4月份\8_autoGPT实战\优缺点"

    def construct(self):
        ble = Table(
            self.title,
            self.path,
            dx=4.4,
            dy=1,
            gap=3e-2,
        )
        ble.dy_list[0] = 0.86
        ble.dx_list[0] = 1.6
        ble.arrange_table()
        ble.table.scale(1.1).shift(UP * 0.2)
        ble.title.scale(0.9).next_to(ble.table, UP, buff=MED_LARGE_BUFF)

        locAcontent = (
            (
                ble.tex_column[1][1],
                """
             \\parbox{6cm}{
             联网、自我分析、可直接输出文件
             }""",
                WHITE,
            ),
            (
                ble.tex_column[1][2],
                """
            \\parbox{6cm}{
            有技术门槛、程序容易出错、效率低、费用极高、gpt-3.5-turbo、不能直接输出中文
            }""",
                RED,
            ),
            (
                ble.tex_column[2][1],
                """
            \\parbox{6cm}{
            拿来就用、效率高、相对来说费用底、GPT4模型
            }""",
                WHITE,
            ),
            (
                ble.tex_column[2][2],
                """
            \\parbox{6cm}{
            内容知识偏旧、不能联网
            }""",
                RED,
            ),
        )
        ble.replace_part(locAcontent, fonsz=25)
        ble.tex_column[0][1].scale(1.2)
        ble.tex_column[0][2].scale(1.2)
        ble.tex_column[1][0].scale(1.2)
        ble.tex_column[2][0].scale(1.2)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.play(
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            FlashAround(ble.table, time_width=3),
            LaggedStartMap(FadeIn, ble.bg, scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column, scale=0.9, lag_ratio=0.1),
            run_time=1,
        )
        self.wait(2)


class TimeCosts(Scene):
    title = "费用计算方法"
    path = r"Z:\PengVideo\短视频\4月份\8_autoGPT实战\费用"

    def construct(self):
        ble = Table(self.title, self.path, dx=1.2, dy=0.618, no_focus=True)
        ble.dy_list[0] = 0.618
        # ble.dx_list[1] = 5.6
        ble.arrange_table()
        ble.table.scale(1.618).shift(UP)
        ble.title.scale(1).next_to(ble.table, UP, buff=MED_LARGE_BUFF)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        ble.bg[0].set_style(fill_opacity=0.5),
        ble.bg[1].set_style(fill_opacity=0.5),
        # frame = self.camera.frame
        # frame.scale(0.8)
        self.play(
            FlashAround(ble.table),
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            LaggedStartMap(FadeIn, ble.bg, scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column, scale=0.9, lag_ratio=0.1),
            run_time=1,
        )
        self.wait()

        for i in range(0, ble.row):
            if (i + 1) % 2:
                fop = 0.6
            else:
                fop = 0.6
            size = 1.25
            if i == 0:
                self.play(
                    FlashAround(ble.bg[i]),
                    ble.bg[i][0].animate.set_style(fill_opacity=0.8),
                    ble.bg[i][1].animate.set_style(fill_opacity=0.8),
                    ble.bg[i][2].animate.set_style(fill_opacity=0.8),
                    ble.bg[i][3].animate.set_style(fill_opacity=0.8),
                    ble.tex_column[i][0].animate.set_color(ORANGE).scale(size),
                    ble.tex_column[i][1].animate.set_color(ORANGE).scale(size),
                    ble.tex_column[i][2].animate.set_color(ORANGE).scale(size),
                    ble.tex_column[i][3].animate.set_color(ORANGE).scale(size),
                )
                self.wait(2)
            else:
                self.play(
                    ble.bg[i - 1].animate.set_style(fill_opacity=fop),
                    ble.tex_column[i - 1][0].animate.scale(1 / size).set_color(YELLOW),
                    ble.tex_column[i - 1][1].animate.scale(1 / size).set_color(YELLOW),
                    ble.tex_column[i - 1][2].animate.scale(1 / size).set_color(YELLOW),
                    ble.tex_column[i - 1][3].animate.scale(1 / size).set_color(YELLOW),
                    FlashAround(ble.bg[i]),
                    # frame.animate.move_to(ble.tex_column[i+1],coor_mask=np.array([0, 1, 0])),
                    ble.bg[i].animate.set_style(fill_opacity=0.8),
                    ble.tex_column[i][0].animate.scale(size).set_color(ORANGE),
                    ble.tex_column[i][1].animate.scale(size).set_color(ORANGE),
                    ble.tex_column[i][2].animate.scale(size).set_color(ORANGE),
                    ble.tex_column[i][3].animate.scale(size).set_color(ORANGE),
                )
        self.wait(2)
        self.play(
            ble.bg[ble.row - 1].animate.set_style(fill_opacity=fop),
            ble.tex_column[ble.row - 1][0].animate.scale(1 / size).set_color(WHITE),
            ble.tex_column[ble.row - 1][1].animate.scale(1 / size).set_color(WHITE),
            ble.tex_column[ble.row - 1][2].animate.scale(1 / size).set_color(WHITE),
            ble.tex_column[ble.row - 1][3].animate.scale(1 / size).set_color(WHITE),
        )
        self.wait(2)

        ptxt = [
            "$(\\frac{16:55-16:45}{8.38-8.22} +\\frac{17:05-16:55}{8.53-8.38})/2 =0.0155$美元/分钟",
            "大约$0.93$美元/小时",
        ]
        pvg = VGroup()
        for p in ptxt:
            pvg.add(
                TexText(
                    p,
                    font_size=35,
                )
            )
        pvg.arrange(DOWN)
        pvg.next_to(ble.table, DOWN * 2)

        self.play(
            LaggedStartMap(FadeIn, pvg, scale=0.9, shift=UP, lag_ratio=0.1), run_time=1
        )
        self.wait()


class ChatGPTCosts(Scene):
    def construct(self):
        ptxt = [
            "$\\frac{12}{3}\\times{25}\\times{30}=3750$条",
            "$\\frac{20}{3750}=0.005$美元/条",
        ]
        pvg = VGroup()
        for p in ptxt:
            pvg.add(
                TexText(
                    p,
                    font_size=60,
                )
            )
        pvg.arrange(DOWN)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)

        self.play(
            LaggedStartMap(FadeIn, pvg, scale=0.9, shift=UP, lag_ratio=0.1), run_time=1
        )
        self.wait()


class AutoGPTCosts(Scene):
    def construct(self):
        ptxt = [
            "OPENAI-API",
            "AutoGPT",
            "gpt-3.5-turbo",
            "tokens",
            "Costs",
        ]
        pvg = VGroup()
        for p in ptxt:
            pvg.add(
                Text(
                    p,
                    font_size=45,
                )
            )
        pvg.arrange(RIGHT, buff=0.8)

        Arrvg = VGroup()
        for i in range(len(pvg) - 1):
            Arr = Arrow(pvg[i], pvg[i + 1], color=RED, buff=0.1)
            Arrvg.add(Arr)
        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.play(
            FadeIn(pvg[0], scale=0.5, shift=RIGHT),
        )
        self.wait()
        for i in range(len(pvg) - 1):
            self.play(GrowArrow(Arrvg[i]), FadeIn(pvg[i + 1], scale=0.5))
            self.wait()
        self.wait()


# 生成贝塞尔曲线
class BezierGenate(Scene):
    def construct(self) -> None:
        # 给定控制点
        p1 = np.array([-3, 0, 0])
        p2 = np.array([-1, 2, 0])
        p3 = np.array([1, -2, 0])

        return super().construct()


class Xigao(Scene):
    title = "洗稿内容与原创链接"
    path = r"Z:\PengVideo\短视频\7月份\洗稿赚钱\表格2"

    def construct(self):
        ble = Table(self.title, self.path, dx=2, dy=0.45, all_op=0.2)
        ble.dy_list[0] = 0.6
        ble.dx_list[0] = 1
        ble.dx_list[2] = 6
        # ble.dx_list[1] = 5.6
        ble.arrange_table()
        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(
            FlashAround(ble.table),
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            LaggedStartMap(FadeIn, ble.bg, scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column, scale=0.9, lag_ratio=0.1),
            run_time=1,
        )
        self.wait()


class Superconductivity(Scene):
    title = "高温超导与低温超导对比表"
    path = r"Z:\PengVideo\短视频\8月份\素材\对比表"

    def construct(self):
        ble = Table(self.title, self.path, dx=5, dy=0.45, all_op=0.2, title_buff=0.5)
        ble.dy_list[0] = 0.6
        ble.dx_list[0] = 2
        ble.dx_list[2] = 5
        # ble.dx_list[1] = 5.6
        ble.arrange_table()
        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(
            FlashAround(ble.table),
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            LaggedStartMap(FadeIn, ble.bg, scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column, scale=0.9, lag_ratio=0.1),
            run_time=1,
        )
        self.wait()
        for i in range(1, len(ble.bg)):
            self.play(FlashAround(ble.bg[i]), run_time=3)
            self.wait()


class AIg(Scene):
    title = "AI供应链接上中下游"
    path = r"Z:\PengVideo\短视频\9月份\AI已死\上中下游"

    def construct(self):
        ble = Table(self.title, self.path, dx=2, dy=0.6, all_op=0.2, title_buff=0.5)
        ble.dy_list[0] = 0.72
        ble.dx_list[1] = 4
        ble.dx_list[2] = 4
        # ble.dx_list[1] = 5.6
        ble.arrange_table()
        ble.table.scale(1.1)
        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(
            FlashAround(ble.table),
            FadeIn(ble.title, scale=0.5, shift=DOWN),
            LaggedStartMap(FadeIn, ble.bg, scale=0.9, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ble.tex_column, scale=0.9, lag_ratio=0.1),
            run_time=1,
        )
        self.wait()
        for i in range(1, len(ble.bg)):
            self.play(FlashAround(ble.bg[i]), run_time=3)
            self.wait()


if __name__ == "__main__":
    from os import system

    system("manimgl {} AIg -o".format(__file__))
