
from manimlib import *

class TimeFormatCountdown(Scene):
    def construct(self):
        # hours, minutes, seconds = 23, 56, 4
        hours, minutes, seconds = 24, 39, 35
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        # 创建倒计时器（隐藏的数据源）
        countdown_number = DecimalNumber(
            total_seconds,
            num_decimal_places=0,
            font_size=48
        )
        countdown_number.set_opacity(0)  # 隐藏数字
        
        # 分别创建时、分、秒的显示和固定的冒号
        hour_text = Text(f"{hours:02d}", font_size=72)
        colon1 = Text(":", font_size=72)
        minute_text = Text(f"{minutes:02d}", font_size=72)
        colon2 = Text(":", font_size=72)
        second_text = Text(f"{seconds:02d}", font_size=72)
        
        # 排列位置
        time_group = VGroup(hour_text, colon1, minute_text, colon2, second_text)
        time_group.arrange(RIGHT, buff=0.15)
        time_group.move_to(ORIGIN)
        
        # 添加更新器，只更新数字部分
        def update_time_parts(mob):
            current_seconds = int(countdown_number.get_value())
            h = current_seconds // 3600
            m = (current_seconds % 3600) // 60
            s = current_seconds % 60
            
            # 只更新数字，保持位置不变
            new_hour = Text(f"{h:02d}", font_size=72)
            new_minute = Text(f"{m:02d}", font_size=72)
            new_second = Text(f"{s:02d}", font_size=72)
            
            # 保持原来的位置
            new_hour.move_to(hour_text.get_center())
            new_minute.move_to(minute_text.get_center())
            new_second.move_to(second_text.get_center())
            
            hour_text.become(new_hour)
            minute_text.become(new_minute)
            second_text.become(new_second)
        
        time_group.add_updater(update_time_parts)
        
        # 添加到场景
        self.add(time_group, countdown_number)
        self.wait(1)
        # 执行倒计时动画
        self.play(
            ChangeDecimalToValue(countdown_number, 0),
            run_time=10,
            rate_func=linear
        )
        self.wait(1)


class 齐奥尔科夫斯基火箭方程(Scene):
    def construct(self):
        tex1 = TexText(
            "$$ \\Delta v=v_{e} \\ln \\frac{m_{0}}{m_{f}} $$",
            font="SimSun",
            color=YELLOW,
        )
        tex2 = TexText(
            "$$ v_{e}:\\text{是火箭排气速度} $$",\
            "$$ m_{0}:\\text{是火箭加速前的纯质量总和} $$",
            "$$ m_{f}:\\text{是火箭加速后的纯质量的总和} $$",
            "$$ \\Delta v:\\text{是火箭加速后速度与加速前速度的差值} $$",
            font="SimSun",
            color=GREY,
        )
        tex2.scale(0.4)
        tex2.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        VGroup(tex1, tex2).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(
            1.5
        ).shift(UP * 0.22)

        self.play(ShowCreation(tex1),run_time=3)
        self.wait()
        
        self.play(LaggedStartMap(FadeIn, tex2, shift=UP))
        self.wait()

        self.play(FlashAround(tex1,color=WHITE))
        self.wait()
        
        for i in range(4):
            self.play(tex2[i].animate.set_color(WHITE))
            self.play(FlashAround(tex2[i]))
            self.wait()

        self.wait()

if __name__ == "__main__":
    from os import system
    system("manimgl {} 齐奥尔科夫斯基火箭方程 -o".format(__file__))