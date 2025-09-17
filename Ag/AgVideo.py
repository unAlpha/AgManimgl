# -*- coding: utf-8 -*-
from manimlib import *


# 关键词
class Time1(Scene):
    Q = """
        \\parbox{6cm}{
            Phalaenopsis orchids, three petals unfolded, super clear --v 5 --q 2
            }
        """
    Ans = """
        \\parbox{6cm}{
            蝴蝶兰，三片花瓣展开，超清晰
            }
        """
    Pos = 0
    f = 28

    def construct(self):
        prompt = Text(
            "关键词",
            color=RED,
            font="阿里巴巴普惠体 2.0",
            font_size=40,
        )
        question = TexText(self.Q, font_size=self.f, alignment="\\raggedright")
        pq = VGroup(prompt, question).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        answer = TexText(
            self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright"
        )
        translate = Text(
            "翻译",
            color=GREY,
            font="阿里巴巴普惠体 2.0",
            font_size=40,
        )
        at = VGroup(translate, answer).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        VGroup(pq, at).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center().to_edge(
            LEFT
        ).shift(UP * 0.2)

        # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        # self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(pq, shift=RIGHT),
        )
        self.wait(2)
        self.play(
            FadeIn(translate),
            ShowIncreasingSubsets(*answer),
            run_time=3,
        )
        self.wait(3)


# 关键词连续变换 无图
class Time2(Scene):
    Q = [
        """
        \\parbox{6cm}{
            Roses, three petals fully expanded, plan view, super clear --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose, only three petals, fully unfolded, flat spread, super clear --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose petal --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose petal, flat unfolded, specific --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            A rose petal, flat unfolded onto a plain white tabletop, top view --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            Three rose petals, flat unfolded onto a plain white table, petals not overlapping each other, top view --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            Two rose petals, flat unfolded onto a plain white table, petals do not overlap each other, symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            There are and only two rose petals unfolded to a pure white tabletop, the same size between each petal, the same color, the petals do not overlap each other, no folds in the petals, no bending of the petals, 360 degrees symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,
        """
        \\parbox{6cm}{
            There are and only two rose petals unfolded to a pure white tabletop, petals do not overlap each other, petals are not folded, petals are not bent, 360 degrees symmetrically placed, top view, close-up --stop 50 --v 5 --q 2
            }
        """,
    ]
    Ans = [
        """
        \\parbox{6cm}{
            玫瑰花，三片花瓣完全展开，平面图，超级清晰
            }
        """,
        """
        \\parbox{6cm}{
            一朵玫瑰，只有三片花瓣，完全展开，平铺，超级清晰
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣，平铺，特写
            }
        """,
        """
        \\parbox{6cm}{
            一片玫瑰花瓣，平铺在白色的桌面上，俯视图
            }
        """,
        """
        \\parbox{6cm}{
            三片玫瑰花瓣，平铺在白色的桌子上，花瓣之间没有重叠，俯视图
            }
        """,
        """
        \\parbox{6cm}{
            两片玫瑰花瓣，平铺在白色的桌子上，花瓣没有相互重叠，对称放置，俯视，特写
            }
        """,
        """
        \\parbox{6cm}{
            有且仅有两片玫瑰花瓣展开在纯白的桌面上，每片花瓣之间大小相同，颜色相同，花瓣之间没有重叠，花瓣没有褶皱，花瓣没有弯曲，360度对称放置，俯视，特写
            }
        """,
        """
        \\parbox{6cm}{
            有且仅有两片玫瑰花瓣展开在纯白的桌面上，花瓣没有相互重叠，花瓣没有折叠，花瓣没有弯曲，360度对称放置，俯视，特写
            }
        """,
    ]
    Pos = 0
    f = 28

    def construct(self):
        VGpqat = VGroup()
        for i in range(9):
            prompt = Text(
                "关键词",
                color=RED,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            question = TexText(self.Q[i], font_size=self.f, alignment="\\raggedright")
            pq = VGroup(prompt, question).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            answer = TexText(
                self.Ans[i], color=YELLOW, font_size=self.f, alignment="\\raggedright"
            )
            translate = Text(
                "翻译",
                color=GREY,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            at = VGroup(translate, answer).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            VGpqat.add(
                VGroup(pq, at)
                .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
                .center()
                .to_edge(LEFT)
                .shift(UP * 0.2)
            )

            # bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
            # self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(VGpqat[0][0], shift=RIGHT),
        )
        self.wait(2)
        self.play(
            FadeIn(VGpqat[0][1][0]),
            ShowIncreasingSubsets(*VGpqat[0][1][1]),
            run_time=3,
        )
        self.wait(3)
        for j in range(1, 9):
            print(j)
            self.play(ReplacementTransform(VGpqat[j - 1], VGpqat[j]))
            self.wait(3)


# 直接列图 上方无文字
class PictureShow(Scene):
    def construct(self):
        pics_list1 = [
            "AgPics/f0",
            "AgPics/f1",
            "AgPics/f2",
            "AgPics/f3",
            "AgPics/f4",
            "AgPics/f5",
        ]
        pics_vg = Group()
        for i in range(len(pics_list1)):
            pic_vg = Group()
            pic = ImageMobject(pics_list1[i]).scale(0.5)
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0.00, buff=0)
            pic_vg.add(pic, border)
            pics_vg.add(pic_vg)
            pics_vg[i].shift(UP * 0.2)
        pics_vg.arrange(RIGHT, aligned_edge=LEFT, buff=1.236)
        self.play(
            LaggedStartMap(FadeIn, pics_vg, shift=LEFT, scale=1, lag_ratio=0.5),
        )
        self.wait(2)


class WordsChange1(Scene):
    def construct(self):
        Q = [
            """
                full body portrait of a beautiful woman \\par
                25 years old, wearing in a black coat, \\par
                black short hair, green eyes, walkink on \\par
                the street, professional photography \\par
                --ar 2:3 --s 1000 --q 2 --v 5
            """,
            """
                full body portrait of a beautiful woman \\par
                25 years old, wearing in a white coat, \\par
                black short hair, green eyes, walkink on \\par
                the street, professional photography \\par
                --ar 2:3 --s 1000 --q 2 --v 5 --seed 4015514435
            """,
        ]

        Q_words = ["black", "white", "--v 5"]

        Vg_q = VGroup()
        for i in range(len(Q)):
            question = TexText(
                Q[i], isolate=Q_words, font_size=28, alignment="\\raggedright"
            )
            Vg_q.add(question)
        self.add(Vg_q[0])

        # Replace only the black to white part
        black_to_white_transform = TransformMatchingShapes(
            Vg_q[0].get_part_by_tex("black"),
            Vg_q[1].get_part_by_tex("white").move_to(Vg_q[0].get_part_by_tex("black")),
        )

        seed_part = TexText("--seed 4015514435", font_size=28)
        seed_part.next_to(Vg_q[0].get_part_by_tex("--v 5"), RIGHT, buff=0.13)

        self.play(black_to_white_transform, FadeIn(seed_part))


# 关键词部分替换
class WordsChange2(Scene):
    def construct(self):
        Q = [
            """
             \\parbox{7cm}{
                full body portrait of a beautiful woman 
                25 years old, wearing in a black coat, 
                black short hair, green eyes, walkink on
                the street, professional photography
                --ar 2:3 --s 1000 --q 2 --v 5
                }
            """,
            """
            \\parbox{7cm}{
                full body portrait of a beautiful woman 
                25 years old, wearing in a white coat, 
                black short hair, green eyes, walkink on
                the street, professional photography 
                --ar 2:3 --s 1000 --q 2 --v 5 --seed 4015514435
                }
            """,
        ]

        Q_words = ["black", "white", "--v 5"]

        Vg_q = VGroup()
        for i in range(len(Q)):
            question = TexText(
                Q[i], isolate=Q_words, font_size=28, alignment="\\raggedright"
            )
            Vg_q.add(question)
        self.add(Vg_q[0])

        # Replace only the black to white part
        black_to_white_transform = TransformMatchingShapes(
            Vg_q[0].get_part_by_tex("black"),
            Vg_q[1].get_part_by_tex("white").move_to(Vg_q[0].get_part_by_tex("black")),
        )

        seed_part = TexText("--seed 4015514435", font_size=28)
        seed_part.next_to(Vg_q[0].get_part_by_tex("--v 5"), RIGHT, buff=0.13)

        self.play(black_to_white_transform, FadeIn(seed_part))


# 替代变换 有图
class PictureShow1(Scene):
    Q = [
        """
        \\parbox{7cm}{
            full body portrait of a beautiful woman 25 years old, wearing in a black coat, 
            black short hair, green eyes, walkink on the street, professional photography, \\par
            --ar 2:3 --s 1000 --q 2 --v 5
            }
        """,
        """
        \\parbox{7cm}{
            full body portrait of a beautiful woman 25 years old, wearing in a white coat, 
            black short hair, green eyes, walkink on the street, professional photography, \\par
            --ar 2:3 --s 1000 --q 2 --v 5 --seed 4015514435
            }
        """,
    ]
    Ans = [
        """
        \\parbox{7cm}{
            全身肖像的一个美丽的女人25岁，穿着黑色的外套，黑色的短发，绿色的眼睛，
            在街上走着，专业摄影，\\par
            --ar 2:3 --s 1000 --q 2 --v 5
            }
        """,
        """
        \\parbox{7cm}{
            全身肖像的一个美丽的女人25岁，穿着白色的外套，黑色的短发，绿色的眼睛，
            在街上走着，专业摄影，\\par
            --ar 2:3 --s 1000 --q 2 --v 5 --seed 4015514435
            }
        """,
    ]
    Anim_words = [
        ["black", "white", "--v 5"],
        ["黑", "白", "--v 5"],
        ["--seed 4015514435"],
    ]
    Coat = [
        [
            "黑色外套",
            "AgPics/外国人黑外套",
        ],
        [
            "白色外套",
            "AgPics/外国人白外套",
        ],
    ]

    Pos = 0
    f = 28

    def construct(self):
        VGpqat = VGroup()
        VGcg = Group()

        for i in range(2):
            prompt = Text(
                "关键词",
                color=RED,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            question = TexText(
                self.Q[i],
                isolate=self.Anim_words[0],
                font_size=self.f,
                alignment="\\raggedright",
            )
            pq = VGroup(prompt, question).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

            translate = Text(
                "翻译",
                color=GREY,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            answer = TexText(
                self.Ans[i],
                isolate=self.Anim_words[1],
                color=YELLOW,
                font_size=self.f,
                alignment="\\raggedright",
            )
            at = VGroup(translate, answer).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

            VGpqat.add(
                VGroup(pq, at)
                .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
                .center()
                .to_edge(LEFT, buff=1)
                .shift(UP * 0.2)
            )

        for i in range(len(self.Coat)):
            coattxt = Text(
                self.Coat[i][0],
                color=WHITE,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            pic_vg = Group()
            pic = ImageMobject(self.Coat[i][1], height=6)
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
            pic_vg.add(pic, border)
            cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
            cg_vg.to_edge(RIGHT, buff=2.2).shift(UP * 0.2)
            VGcg.add(cg_vg)

        black_to_white_transform1 = ReplacementTransform(
            VGpqat[0][0][1].get_part_by_tex(self.Anim_words[0][0]),
            VGpqat[1][0][1]
            .get_part_by_tex(self.Anim_words[0][1])
            .move_to(VGpqat[0][0][1].get_part_by_tex(self.Anim_words[0][0])),
        )
        seed_part1 = TexText(self.Anim_words[2][0], font_size=self.f)
        seed_part1.next_to(
            VGpqat[0][0][1].get_part_by_tex(self.Anim_words[0][2]), RIGHT, buff=0.13
        )

        black_to_white_transform2 = ReplacementTransform(
            VGpqat[0][1][1].get_part_by_tex(self.Anim_words[1][0]),
            VGpqat[1][1][1]
            .get_part_by_tex(self.Anim_words[1][1])
            .move_to(VGpqat[0][1][1].get_part_by_tex(self.Anim_words[1][0])),
        )
        seed_part2 = TexText(self.Anim_words[2][0], color=YELLOW, font_size=self.f)
        seed_part2.next_to(
            VGpqat[0][1][1].get_part_by_tex(self.Anim_words[1][2]), RIGHT, buff=0.13
        )
        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(VGpqat[0][0], shift=RIGHT),
        )
        self.wait(0.2)
        self.play(
            FadeIn(
                VGcg[0],
                shift=RIGHT,
            )
        )
        self.play(
            FadeIn(VGpqat[0][1][0]),
            ShowIncreasingSubsets(VGpqat[0][1][1]),
            run_time=3,
        )

        self.wait(3)
        vgjcopy = VGcg[1].copy()
        for j in range(1, len(self.Q)):
            self.play(
                ReplacementTransform(VGpqat[j - 1][0][0], VGpqat[j][0][0]),
                black_to_white_transform1,
                ReplacementTransform(VGpqat[j - 1][1][0], VGpqat[j][1][0]),
                black_to_white_transform2,
                FadeIn(seed_part1),
                FadeIn(seed_part2),
                FadeOut(
                    VGcg[j - 1],
                    shift=LEFT,
                ),
                FadeIn(
                    vgjcopy,
                    shift=RIGHT,
                ),
            )
            self.wait(3)
        VGcg.arrange(RIGHT, buff=0.23, aligned_edge=UP).shift(UP * 0.236).scale(0.8)
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(VGpqat[1][0][0]),
                    FadeOut(VGpqat[1][1][0]),
                    FadeOut(VGpqat[1][0][1].get_part_by_tex(self.Anim_words[0][1])),
                    FadeOut(VGpqat[1][1][1].get_part_by_tex(self.Anim_words[1][1])),
                    FadeOut(VGpqat[0]),
                    FadeOut(seed_part1),
                    FadeOut(seed_part2),
                    FadeOut(vgjcopy),
                ),
                LaggedStartMap(FadeIn, VGcg, shift=LEFT, scale=1, lag_ratio=0.5),
                lag_ratio=0.2,
                run_time=1,
            )
        )
        self.wait(3)


class PictureShow2(PictureShow1):
    Q = [
        """
        \\parbox{7cm}{
            full body portrait of a asia beautiful woman 25 years old, wearing in a black coat, 
            black short hair, green eyes, walkink on the street, professional photography, \\par
            --ar 2:3 --s 1000 --q 2 --v 5
            }
        """,
        """
        \\parbox{7cm}{
            full body portrait of a asia beautiful woman 25 years old, wearing in a white coat, 
            black short hair, green eyes, walkink on the street, professional photography, \\par
            --ar 2:3 --s 1000 --q 2 --v 5 --seed 322570267
            }
        """,
    ]
    Ans = [
        """
        \\parbox{7cm}{
            全身肖像的一个美丽的亚洲女孩25岁，穿着黑色的外套，黑色的短发，绿色的眼睛，
            在街上走着，专业摄影，\\par
            --ar 2:3 --s 1000 --q 2 --v 5
            }
        """,
        """
        \\parbox{7cm}{
            全身肖像的一个美丽的亚洲女孩25岁，穿着白色的外套，黑色的短发，绿色的眼睛，
            在街上走着，专业摄影，\\par
            --ar 2:3 --s 1000 --q 2 --v 5 --seed 322570267
            }
        """,
    ]
    Anim_words = [
        ["black", "white", "--v 5"],
        ["黑", "白", "--v 5"],
        ["--seed 322570267"],
    ]

    Coat = [
        [
            "黑色外套",
            "AgPics/国人黑外套",
        ],
        [
            "白色外套",
            "AgPics/国人白外套",
        ],
        [
            "红色外套",
            "AgPics/国人红外套",
        ],
        [
            "黄色外套",
            "AgPics/国人黄外套",
        ],
    ]


# 展示第一张后，列图-有文字
class Picture1Show(Scene):
    Coat = [["人物", "AgPics/国人黑外套", 6], ["衣服", "AgPics/米色衣服", 5]]
    show = 1
    bf = 1.6
    lag_r = 0.5
    ali_edge = ORIGIN

    def construct(self):
        VGcg = Group()
        ss_vg = Group()
        for i in range(len(self.Coat)):
            coattxt = Text(
                self.Coat[i][0],
                color=WHITE,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            pic_vg = Group()
            pic = ImageMobject(self.Coat[i][1], height=self.Coat[i][2])
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
            pic_vg.add(pic, border)
            cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
            VGcg.add(cg_vg)

        VGcg.arrange(RIGHT, aligned_edge=self.ali_edge, buff=self.bf).shift(UP * 0.236)
        ss_vg.add(VGcg[0 : self.show]).save_state()

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)

        self.play(
            FadeIn(
                ss_vg.center().shift(UP * 0.236),
                shift=LEFT,
                scale=0.618,
            )
        )
        self.wait(1)
        self.play(
            ss_vg.animate.restore(),
            FadeIn(VGcg[self.show :], shift=LEFT, scale=1, lag_ratio=self.lag_r),
        )
        self.wait(2)


# 有色关键词变换
class WordsChange4(Scene):
    Q = [
        """
        \\parbox{13cm}{
            full body portrait of a asia beautiful woman 25 years old,\\par
            wearing in a black coat,\\par
            black short hair, green eyes, walkink on the street, professional photography,\\par
            --ar 2:3 --s 1000 --q 2 --v 5
        }
        """,
        """
        \\parbox{13cm}{
            https://s.mj.run/RpAaYjJjlZs \\par
            full body portrait of a asia beautiful woman 25 years old,\\par
            Wearing calvin klein cropped gilet cream, in the style of minimalist: spare simplicity, soft, muted color palette, serene minimalism, light magenta and dark gray, elongated forms, precisionist style, dark beige and sky-blue,\\par
            black short hair, green eyes, walkink on the street, professional photography,\\par
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
        }
        """,
    ]

    Q_words = [
        ["https://s.mj.run/RpAaYjJjlZs", YELLOW],
        ["wearing in a black coat,", BLUE],
        [
            "Wearing calvin klein cropped gilet cream, in the style of minimalist: spare simplicity, soft, muted color palette, serene minimalism, light magenta and dark gray, elongated forms, precisionist style, dark beige and sky-blue,",
            BLUE,
        ],
        ["-iw 2 --seed 322570267", RED],
    ]
    title1 = "原始提示词"

    def construct(self):
        Vg_q = VGroup()
        title1 = Text(
            self.title1,
            color=WHITE,
            font="阿里巴巴普惠体 2.0",
            font_size=36,
        )
        for i in range(len(self.Q)):
            questions = TexText(
                self.Q[i],
                isolate=[qw[0] for qw in self.Q_words],
                font_size=28,
                alignment="\\raggedright",
            )
            Vg_q.add(questions)

            for i in range(len(self.Q_words)):
                questions.set_color_by_tex(self.Q_words[i][0], self.Q_words[i][1])

        Vg_q.arrange(DOWN, aligned_edge=LEFT, buff=0.86).shift(UP * 0.3)
        Vg_q[0].save_state()
        always(title1.next_to, Vg_q[0], UP, buff=0.236)
        arr = CurvedArrow(Vg_q[0].get_left(), Vg_q[1].get_left(), buff=1).shift(
            LEFT * 0.25
        )

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)

        self.play(
            FadeIn(
                title1,
                scale=0.618,
            ),
            FadeIn(
                Vg_q[0].center(),
                shift=LEFT,
                scale=0.618,
            ),
        )
        self.wait(1)
        self.play(
            Vg_q[0].animate.restore(),
            GrowArrow(arr),
            TransformFromCopy(Vg_q[0], Vg_q[1]),
        )
        self.wait(2)


# 直接变换
class PictureShow3(Scene):
    Q = [
        """
        \\parbox{8cm}{
            https://s.mj.run/RpAaYjJjlZs 
            full body portrait of a asia beautiful woman 25 years old, 
            Wearing calvin klein cropped gilet cream, in the style of minimalist: spare simplicity, soft, muted color palette, serene minimalism, light magenta and dark gray, elongated forms, precisionist style, dark beige and sky-blue, 
            black short hair, green eyes, walkink on the street, professional photography, 
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
        """
        \\parbox{8cm}{
            https://s.mj.run/RpAaYjJjlZs  
            full body portrait of a asia beautiful woman 25 years old, 
            sleeveless vest in ivory, in the style of lilla cabot perry, fake vertical bags are sewn, --no buttons, 
            black short hair, green eyes, walkink on the street, professional photography, 
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]
    Ans = [
        """
        \\parbox{8cm}{
            全身肖像的一个美丽的亚洲女孩25岁，
            穿着Calvin klein裁剪的奶油色马甲，极简主义风格：闲暇的简约，柔和的色调，宁静的极简主义，浅洋红色和深灰色，拉长的形式，精确主义风格，深米色和天蓝色， 
            黑色短发，绿色眼睛，在街上行走，专业摄影，
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
        """
        \\parbox{8cm}{
            全身肖像的一个美丽的亚洲女孩25岁，
            象牙色无袖马甲，采用Lilla Cabot Perry的风格，缝制了假的垂直袋，--没有纽扣，
            黑色短发，绿色眼睛，在街上行走，专业摄影，
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]

    Coat = [
        [
            "外套样式A",
            "AgPics/米1",
        ],
        [
            "外套样式B",
            "AgPics/米2",
        ],
        [
            "外套样式C",
            "AgPics/米3",
        ],
    ]
    f = 26

    def construct(self):
        VGpqat = VGroup()
        VGcg = Group()

        for i in range(2):
            prompt = Text(
                "关键词",
                color=RED,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            question = TexText(self.Q[i], font_size=self.f, alignment="\\raggedright")
            pq = VGroup(prompt, question).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

            translate = Text(
                "翻译",
                color=GREY,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            answer = TexText(
                self.Ans[i], color=YELLOW, font_size=self.f, alignment="\\raggedright"
            )
            at = VGroup(translate, answer).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

            VGpqat.add(
                VGroup(pq, at)
                .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
                .center()
                .to_edge(LEFT, buff=1)
                .shift(UP * 0.2)
            )

        for i in range(len(self.Coat)):
            coattxt = Text(
                self.Coat[i][0],
                color=WHITE,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            pic_vg = Group()
            pic = ImageMobject(self.Coat[i][1], height=6)
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
            pic_vg.add(pic, border)
            cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
            cg_vg.to_edge(RIGHT, buff=1.68).shift(UP * 0.2)
            VGcg.add(cg_vg)

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(VGpqat[0][0], shift=RIGHT),
        )
        self.wait(0.2)
        self.play(
            FadeIn(
                VGcg[0],
                shift=RIGHT,
            )
        )
        self.play(
            FadeIn(VGpqat[0][1][0]),
            ShowIncreasingSubsets(*VGpqat[0][1][1]),
            run_time=3,
        )

        self.wait(3)
        vgjcopy = VGcg[1].copy()
        for j in range(1, len(self.Q)):
            self.play(
                ReplacementTransform(VGpqat[j - 1], VGpqat[j]),
                FadeOut(
                    VGcg[j - 1],
                    shift=LEFT,
                ),
                FadeIn(
                    vgjcopy,
                    shift=RIGHT,
                ),
            )
            self.wait(3)
        VGcg.arrange(RIGHT, buff=0.23, aligned_edge=UP).shift(UP * 0.236)
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(VGpqat[1]),
                    FadeOut(vgjcopy),
                ),
                LaggedStartMap(FadeIn, VGcg, shift=LEFT, scale=1, lag_ratio=1),
                lag_ratio=0.2,
                run_time=1,
            )
        )
        self.wait(3)


# 直接列图-有文字
class Picture2Show(Scene):
    Coat = [
        ["人物", "AgPics/内衣1", 6.2],
        ["需求衣服", "AgPics/内衣2", 6.2],
        ["结合体", "AgPics/内衣3", 6.2],
    ]
    ar_buf = 0.5
    ar_scl = 0.96
    shi_up = 0.236

    def construct(self):
        VGcg = Group()
        for i in range(len(self.Coat)):
            coattxt = Text(
                self.Coat[i][0],
                color=WHITE,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            pic_vg = Group()
            pic = ImageMobject(self.Coat[i][1], height=self.Coat[i][2])
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
            pic_vg.add(pic, border)
            cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
            VGcg.add(cg_vg)

        VGcg.arrange(RIGHT, buff=self.ar_buf, aligned_edge=UP).shift(
            UP * self.shi_up
        ).scale(self.ar_scl)

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(
            LaggedStartMap(FadeIn, VGcg, shift=LEFT, scale=1, lag_ratio=0.5),
        )
        self.wait(2)


# 关键词 列图
class PictureShow4(Scene):
    Q = [
        """
        \\parbox{8cm}{
            https://s.mj.run/RpAaYjJjlZs 
            full body portrait of a asia beautiful woman 25 years old, 
            big chest, plump body, Wearing in grey sports tights and pure white yoga pants, 
            black short hair, green eyes, walkink on the street, professional photography, 
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]
    Ans = [
        """
        \\parbox{8cm}{
            全身肖像的一个美丽的亚洲女孩25岁，
            大胸，丰满的身体，穿着灰色运动紧身衣和纯白色瑜伽裤,
            黑色短发，绿色眼睛，在街上行走，专业摄影，
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]

    Coat = [
        [
            "手工合并图",
            "AgPics/内衣3",
        ],
        [
            "Midjourney生成图2",
            "AgPics/内衣4",
        ],
        [
            "Midjourney生成图1",
            "AgPics/内衣5",
        ],
    ]
    ar_buf = 0.5
    ar_scl = 0.96
    fshow = 2
    lag_r = 0.5
    f = 26

    def construct(self):
        VGpqat = VGroup()
        VGcg = Group()

        prompt = Text(
            "关键词",
            color=RED,
            font="阿里巴巴普惠体 2.0",
            font_size=40,
        )
        question = TexText(self.Q[0], font_size=self.f, alignment="\\raggedright")
        pq = VGroup(prompt, question).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        translate = Text(
            "翻译",
            color=GREY,
            font="阿里巴巴普惠体 2.0",
            font_size=40,
        )
        answer = TexText(
            self.Ans[0], color=YELLOW, font_size=self.f, alignment="\\raggedright"
        )
        at = VGroup(translate, answer).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        VGpqat.add(
            VGroup(pq, at)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            .center()
            .to_edge(LEFT, buff=1)
            .shift(UP * 0.2)
        )

        for i in range(len(self.Coat)):
            coattxt = Text(
                self.Coat[i][0],
                color=WHITE,
                font="阿里巴巴普惠体 2.0",
                font_size=40,
            )
            pic_vg = Group()
            pic = ImageMobject(self.Coat[i][1], height=6.2)
            border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
            pic_vg.add(pic, border)
            cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
            cg_vg.to_edge(RIGHT, buff=1.68).shift(UP * 0.2)
            VGcg.add(cg_vg)

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.wait(1)
        self.play(
            FadeIn(VGpqat[0][0], shift=RIGHT),
        )
        self.wait(0.2)
        vgjcopy = VGcg[self.fshow].copy()
        self.play(
            FadeIn(
                vgjcopy,
                shift=RIGHT,
            )
        )
        self.play(
            FadeIn(VGpqat[0][1][0]),
            ShowIncreasingSubsets(*VGpqat[0][1][1]),
            run_time=3,
        )

        self.wait(3)

        VGcg.arrange(RIGHT, buff=self.ar_buf, aligned_edge=UP).shift(UP * 0.236).scale(
            self.ar_scl
        )
        self.play(
            LaggedStart(
                AnimationGroup(
                    FadeOut(vgjcopy),
                    FadeOut(VGpqat),
                ),
                LaggedStartMap(FadeIn, VGcg, shift=LEFT, scale=1, lag_ratio=self.lag_r),
                lag_ratio=0.2,
                run_time=1,
            )
        )
        self.wait(3)


class Picture3Show(Picture1Show):
    Coat = [
        ["人物", "AgPics/内衣1", 6.2],
        ["需求衣服", "AgPics/过不了1", 6.2],
        ["结合体", "AgPics/过不了2", 6.2],
    ]
    show = 2
    bf = 0.5
    ali_edge = UP


class WordsChange5(WordsChange4):
    Q = [
        """
        \\parbox{13cm}{
        full body portrait of a asia beautiful woman 25 years old,\\par
        wearing in a black coat,\\par
        black short hair, green eyes, walkink on the street, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5
        }
        """,
        """
        \\parbox{13cm}{
        https://s.mj.run/KPWQrtp02rU \\par
        full body portrait of a asia beautiful woman 25 years old,\\par
        posing in black super short tights, super short sleeves, soft and rounded forms, solapunk, clear edge definition,\\par
        black short hair, green eyes, walkink on the street, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
        }
        """,
    ]

    Q_words = [
        ["https://s.mj.run/KPWQrtp02rU", YELLOW],
        ["wearing in a black coat,", BLUE],
        [
            "posing in black super short tights, super short sleeves, soft and rounded forms, solapunk, clear edge definition,",
            BLUE,
        ],
        ["--iw 2 --seed 322570267", RED],
    ]


class PictureShow5(PictureShow4):
    Q = [
        """
        \\parbox{8cm}{
            https://s.mj.run/KPWQrtp02rU 
            full body portrait of a asia beautiful woman 25 years old, 
            posing in black super short tights, super short sleeves, soft and rounded forms, solapunk, clear edge definition,  
            black short hair, green eyes, walkink on the street, professional photography, 
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]
    Ans = [
        """
        \\parbox{8cm}{
            全身肖像的一个美丽的亚洲女孩25岁，
            摆出黑色超短紧身衣、超短袖的姿势，柔软而圆润的形式，孤独派，清晰的边缘,
            黑色短发，绿色眼睛，在街上行走，专业摄影，
            --ar 2:3 --s 1000 --q 2 --v 5 --iw 2 --seed 322570267
            }
        """,
    ]

    Coat = [
        [
            "效果图1",
            "AgPics/隆胸1",
        ],
        [
            "效果图2",
            "AgPics/隆胸2",
        ],
        [
            "效果图3",
            "AgPics/隆胸3",
        ],
        [
            "效果图4",
            "AgPics/隆胸4",
        ],
    ]
    ar_buf = 0.236
    ar_scl = 0.8
    fshow = 0
    lag_r = 0.5


class Picture4Show(Picture2Show):
    Coat = [
        ["垫图1", "AgPics/美1", 6.2],
        ["垫图2", "AgPics/美2", 6.2],
        ["垫图3", "AgPics/美3", 6.2],
    ]


class WordsChange6(Scene):
    Q = """
        \\parbox{12cm}{
        https://s.mj.run/fne5AtRlmSw \\par
        https://s.mj.run/JeWk45qTnd4 \\par
        https://s.mj.run/24a86cE2ygk \\par
        full body, Wearing a swimsuit, by the beach，black short hair, green eyes, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5
        }
        """
    Q_words = [
        ["https://s.mj.run/fne5AtRlmSw", YELLOW],
        ["https://s.mj.run/JeWk45qTnd4", YELLOW],
        ["https://s.mj.run/24a86cE2ygk", YELLOW],
        ["--ar 2:3 --s 1000 --q 2 --v 5", RED],
    ]
    title1 = "提示词："

    def construct(self):
        title1 = Text(
            self.title1,
            color=WHITE,
            font="阿里巴巴普惠体 2.0",
            font_size=36,
        )
        questions = TexText(
            self.Q,
            isolate=[qw[0] for qw in self.Q_words],
            font_size=32,
            alignment="\\raggedright",
        ).shift(UP * 0.618)
        for i in range(len(self.Q_words)):
            questions.set_color_by_tex(self.Q_words[i][0], self.Q_words[i][1])

        title1.next_to(questions, UP, aligned_edge=LEFT, buff=0.236).shift(RIGHT * 0.1)

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)

        self.play(
            FadeIn(
                title1,
                shift=DOWN,
                scale=0.618,
            ),
            FadeIn(
                questions,
                shift=LEFT,
                scale=0.618,
            ),
        )
        self.play(FlashAround(questions))
        self.wait(1)


class Picture5Show(Picture2Show):
    Coat = [
        ["效果图1", "AgPics/3-1", 6.2],
        ["效果图2", "AgPics/3-2", 6.2],
        ["效果图3", "AgPics/3-3", 6.2],
        ["效果图4", "AgPics/3-4", 6.2],
    ]
    ar_buf = 0.236
    ar_scl = 0.8
    shi_up = 0.382


class Picture6Show(Picture2Show):
    Coat = [
        ["Remix效果1", "AgPics/fw1", 6.2],
        ["Remix效果2", "AgPics/fw2", 6.2],
    ]
    ar_buf = 0.618
    ar_scl = 1
    shi_up = 0.23


class Picture7Show(Picture2Show):
    Coat = [
        ["风衣1", "AgPics/fy1", 6.2],
        ["风衣2", "AgPics/fy2", 6.2],
    ]
    ar_buf = 0.618
    ar_scl = 1
    shi_up = 0.23


class WordsChange7(WordsChange4):
    Q = [
        """
        \\parbox{12cm}{
        https://s.mj.run/fne5AtRlmSw \\par
        https://s.mj.run/JeWk45qTnd4 \\par
        https://s.mj.run/24a86cE2ygk \\par
        full body, Wearing a swimsuit, by the beach，black short hair, green eyes, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5
        }
        """,
        """
        \\parbox{12cm}{
        https://s.mj.run/fne5AtRlmSw \\par
        https://s.mj.run/JeWk45qTnd4 \\par
        https://s.mj.run/24a86cE2ygk \\par
        full body, Wearing a windbreaker, by the beach，black short hair, green eyes, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5
        }
        """,
    ]

    Q_words = [
        ["https://s.mj.run/fne5AtRlmSw", YELLOW],
        ["https://s.mj.run/JeWk45qTnd4", YELLOW],
        ["https://s.mj.run/24a86cE2ygk", YELLOW],
        ["swimsuit", RED],
        ["windbreaker", RED],
    ]


class Picture8Show(Picture2Show):
    Coat = [
        ["Windbreaker1", "AgPics/fyy1", 6.2],
        ["Windbreaker2", "AgPics/fyy2", 6.2],
        ["Windbreaker3", "AgPics/fyy3", 6.2],
        ["Windbreaker4", "AgPics/fyy4", 6.2],
    ]
    ar_buf = 0.236
    ar_scl = 0.8
    shi_up = 0.382


class Picture9Show(Picture2Show):
    Coat = [
        ["原生成图", "AgPics/fyy3", 6.2],
        ["Remix加长头发等", "AgPics/tf1", 6.2],
    ]
    ar_buf = 0.618
    ar_scl = 1
    shi_up = 0.23


class WordsChange8(WordsChange4):
    Q = [
        """
        \\parbox{12cm}{
        https://s.mj.run/fne5AtRlmSw \\par
        https://s.mj.run/JeWk45qTnd4 \\par
        https://s.mj.run/24a86cE2ygk \\par
        full body, Wearing a windbreaker, by the beach，black short hair, green eyes, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5
        }
        """,
        """
        \\parbox{12cm}{
        https://s.mj.run/fne5AtRlmSw \\par
        https://s.mj.run/JeWk45qTnd4 \\par
        https://s.mj.run/24a86cE2ygk \\par
        full body, Wearing a [\\qquad\\qquad\\qquad], by the beach，black short hair, green eyes, professional photography,\\par
        --ar 2:3 --s 1000 --q 2 --v 5 --seed 4128857600
        }
        """,
    ]

    Q_words = [
        ["https://s.mj.run/fne5AtRlmSw", YELLOW],
        ["https://s.mj.run/JeWk45qTnd4", YELLOW],
        ["https://s.mj.run/24a86cE2ygk", YELLOW],
        ["windbreaker", RED],
        ["[\\qquad\\qquad\\qquad]", RED],
        ["--seed 4128857600", BLUE],
    ]


class Picture10Show(Scene):
    Coat = [
        ["Windbreaker 风衣", "AgPics/31-1", 6.2],
        ["Windbreaker 风衣", "AgPics/31-2", 6.2],
        ["White dress 白裙", "AgPics/32-1", 6.2],
        ["White dress 白裙", "AgPics/32-2", 6.2],
        ["Jacket 夹克", "AgPics/33-1", 6.2],
        ["Jacket 夹克", "AgPics/33-2", 6.2],
        ["Blouse 衬衫", "AgPics/34-1", 6.2],
        ["Blouse 衬衫", "AgPics/34-2", 6.2],
        ["T-shirt T恤", "AgPics/35-1", 6.2],
        ["Sweater 毛衣", "AgPics/35-2", 6.2],
        ["Shorts 短裤", "AgPics/36-1", 6.2],
        ["Hoodie 连帽衫", "AgPics/36-2", 6.2],
    ]
    ar_buf = 0.618
    ar_scl = 1
    shi_up = 0.23
    npps = 2

    def construct(self):
        num_pics_per_scene = self.npps
        previous_VGcg = Group()

        for j in range(0, len(self.Coat), num_pics_per_scene):
            current_pics = self.Coat[j : j + num_pics_per_scene]

            VGcg = Group()
            for i in range(len(current_pics)):
                coattxt = Text(
                    current_pics[i][0],
                    color=WHITE,
                    font="阿里巴巴普惠体 2.0",
                    font_size=40,
                )
                pic_vg = Group()
                pic = ImageMobject(current_pics[i][1], height=current_pics[i][2])
                border = SurroundingRectangle(pic, color=WHITE, stroke_width=0, buff=0)
                pic_vg.add(pic, border)
                cg_vg = Group(coattxt, pic_vg).arrange(DOWN, buff=0.25)
                VGcg.add(cg_vg)

            VGcg.arrange(RIGHT, buff=self.ar_buf, aligned_edge=UP).shift(
                UP * self.shi_up
            ).scale(self.ar_scl)
            bg = FullScreenRectangle(
                fill_color=["#032348", "#46246d", "#31580a", "#852211"]
            )
            self.add(bg)

            if previous_VGcg:
                self.play(
                    LaggedStart(
                        FadeOut(previous_VGcg, shift=LEFT),
                        LaggedStartMap(
                            FadeIn,
                            VGcg,
                            shift=LEFT,
                            lag_ratio=0.2,
                        ),
                        lag_ratio=0.1,
                        run_time=2,
                    )
                )
                previous_VGcg.remove(*previous_VGcg)
            else:
                self.play(
                    LaggedStartMap(FadeIn, VGcg, shift=LEFT, scale=1, lag_ratio=0.5),
                    run_time=2,
                )
            self.wait(2)
            if j + num_pics_per_scene >= len(self.Coat):
                self.play(FadeOut(VGcg))
            previous_VGcg.add(VGcg)


class Picture11Show(Picture10Show):
    Coat = [
        ["黑色外套", "AgPics/国人黑外套", 6.2],
        ["白色外套", "AgPics/国人白外套", 6.2],
        ["红色外套", "AgPics/国人红外套", 6.2],
        ["黄色外套", "AgPics/国人黄外套", 6.2],
        ["隆胸效果1", "AgPics/2-2", 6.2],
        ["隆胸效果1", "AgPics/4-2", 6.2],
        ["隆胸效果1", "AgPics/隆胸3", 6.2],
        ["隆胸效果1", "AgPics/隆胸4", 6.2],
        ["姿态效果1", "AgPics/3-1", 6.2],
        ["姿态效果2", "AgPics/3-2", 6.2],
        ["姿态效果3", "AgPics/3-3", 6.2],
        ["姿态效果4", "AgPics/3-4", 6.2],
        ["Windbreaker 风衣", "AgPics/31-1", 6.2],
        ["Windbreaker 风衣", "AgPics/31-2", 6.2],
        ["White dress 白裙", "AgPics/32-1", 6.2],
        ["White dress 白裙", "AgPics/32-2", 6.2],
        ["Jacket 夹克", "AgPics/33-1", 6.2],
        ["Jacket 夹克", "AgPics/33-2", 6.2],
        ["Blouse 衬衫", "AgPics/34-1", 6.2],
        ["Blouse 衬衫", "AgPics/34-2", 6.2],
        ["T-shirt T恤", "AgPics/35-1", 6.2],
        ["Sweater 毛衣", "AgPics/35-2", 6.2],
        ["Shorts 短裤", "AgPics/36-1", 6.2],
        ["Hoodie 连帽衫", "AgPics/36-2", 6.2],
    ]
    ar_buf = 0.236
    ar_scl = 0.8
    shi_up = 0.382
    npps = 4


class AdobePS(Scene):
    def construct(self):
        func_list = [
            "1、从无到有",
            "2、无中生有",
            "3、凭空消失",
            "4、起死回生",
            "5、无限扩展",
            "6、神形百变",
            "7、瞬间移动",
            "8、融为一体",
            "9、柳暗花明",
            "10、乘风破浪",
        ]
        pvg = VGroup()
        for p in func_list:
            pvg.add(
                Text(
                    p,
                    font="Source Han Sans",
                    font_size=50,
                )
            )
        pvg.shift(RIGHT * 6)

        title = Text(
            "Generative Fill",
            weight=BOLD,
            font_size=120,
        )
        title.set_color_by_gradient(BLUE, YELLOW, RED)

        Arrvg = VGroup()
        for i in range(len(pvg)):
            Arr = always_redraw(
                lambda i=i: Arrow(
                    title.get_right(), pvg[i].get_left(), color=RED, buff=0.25
                )
            )
            Arrvg.add(Arr)

        self.play(
            FadeIn(title, scale=0.5, shift=RIGHT),
        )
        self.wait()

        self.add(Arrvg[:8])
        self.play(
            title.animate.shift(LEFT * 3).scale(0.618),
            *[FadeIn(p, rate_func=linear) for p in pvg[:8]],
            pvg[:8].animate.arrange(DOWN, buff=0.3).shift(RIGHT * 3),
        )
        self.wait()
        self.add(Arrvg[8:])
        pvg[8:].next_to(pvg[7], DOWN, buff=0)
        pvg[8:].set_color(BLUE)
        self.play(
            *[FadeIn(p, rate_func=linear) for p in pvg[8:]],
            pvg.animate.arrange(DOWN, buff=0.2).shift(RIGHT * 3),
        )
        self.wait()
        pvg_BOLD = VGroup()
        for p in func_list:
            pvg_BOLD.add(Text(p, font="Source Han Sans", font_size=120, weight=BOLD))
        pvg_BOLD[8:].set_color(BLUE)

        for i in range(len(func_list)):
            self.play(
                FadeOut(title),
                FadeOut(pvg),
                FadeOut(Arrvg),
                TransformFromCopy(pvg[i], pvg_BOLD[i]),
            )
            self.wait(2)
            self.play(
                FadeIn(title),
                FadeIn(pvg),
                FadeIn(Arrvg),
                FadeOut(pvg_BOLD[i]),
            )
            self.wait(2)


class CreatePhysicsAnimation(Scene):
    def construct(self):
        # 创建一个包含所需文本的列表
        text_list = [
            "电子 (Electron)",
            "原子 (Atom)",
            "晶格 (Lattice)",
            "格波 (Lattice Wave)",
            "声子 (Phonon)",
            "自旋 (Spin)",
            "费米子 (Fermion)",
            "玻色子 (Boson)",
            "玻色–爱因斯坦凝聚态 (BEC)",
            "库珀对 (Cooper Pair)",
        ]

        # 使用VGroup来垂直排列文本，并设置对齐方式
        texts = VGroup(*[Text(txt, font="思源黑体") for txt in text_list])

        texts.arrange(DOWN, buff=0.35, aligned_edge=LEFT).scale(0.8).shift(UP * 0.2)

        # Play the FadeIn animation for each text
        self.play(
            LaggedStartMap(FadeIn, texts, scale=0.9, lag_ratio=0.1),
        )
        self.wait()

        # 将文本组移动到屏幕的左侧
        self.play(
            texts.animate.scale(0.618)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .to_edge(LEFT)
        )

        self.wait()

        # 将文本组添加到场景中
        self.add(texts)

        # 轮流逐个放大文本
        for i in range(len(texts)):
            target_scale = 1.5
            self.play(
                texts[i].animate.scale(target_scale, about_edge=LEFT).set_color(YELLOW),
                # 为了保持间隙，调整其他文本的位置
                *[
                    texts[j].animate.shift(
                        texts[0].get_height() * (target_scale - 1) * UP
                        if j < i
                        else texts[0].get_height() * (target_scale - 1) * DOWN
                    )
                    for j in range(len(texts))
                    if j != i
                ],
            )
            self.play(
                texts[i]
                .animate.scale(1 / target_scale, about_edge=LEFT)
                .set_color(WHITE),
                # 为了恢复间隙，调整其他文本的位置
                *[
                    texts[j].animate.shift(
                        texts[0].get_height() * (target_scale - 1) * DOWN
                        if j < i
                        else texts[0].get_height() * (target_scale - 1) * UP
                    )
                    for j in range(len(texts))
                    if j != i
                ],
            )


class TexTextTransform3(Scene):
    def construct(self):
        tex = TexText(
            "$$\\text{锂电池容量计算法之一}$$",
            "$$\\text{电流} \\times \\text{时间}$$",
            "$$mA \\times h$$",
            "$$1mAh=0.001\\text{安培} \\times 3600\\text{秒}$$",
            "$$=3.6\\text{安培秒}$$",
            "$$=3.6\\text{库仑}$$",
            font="SimSun",
        )
        tex[0].scale(0.7)
        tex[1].scale(1.1)
        tex[2].scale(1.1)

        tex[:3].arrange(DOWN, buff=0.4, aligned_edge=ORIGIN).shift(UP * 0.4)

        tex[3:].scale(0.6)

        tex[3:].arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN * 0.2)
        tex[4:].shift(0.8 * RIGHT)
        tex.center()

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(Write(tex[:3]))
        self.wait()
        self.play(FlashAround(tex[1]))
        self.wait()
        self.play(FlashAround(tex[2]))
        self.wait()
        self.play(tex[:3].animate.shift(UP * 2))
        self.wait()
        self.play(Write(tex[3]))
        self.wait()
        self.play(Write(tex[4]))
        self.wait()
        self.play(Write(tex[5]))
        self.wait()


class TexTextTransform4(Scene):
    def construct(self):
        tex = TexText(
            "$$W_\\text{功} = P_\\text{功率} \\times t_\\text{时间}$$",
            "$$=U_\\text{电压} $$",
            "$$\\times I_\\text{电流} \\times t_\\text{时间}$$",
            font="SimSun",
        )
        tex.scale(0.9)
        tex[1:3].arrange(RIGHT, buff=0.1).scale(0.7)

        tex[0].next_to(tex[1:3], 2 * UP)
        tex[1:3].shift(RIGHT * 0.5)

        bg = FullScreenRectangle(
            fill_color=["#032348", "#46246d", "#31580a", "#852211"]
        )
        self.add(bg)
        self.play(Write(tex))
        self.wait()
        self.play(
            FlashAround(tex[0][3:6]),
            time_width=2.0,
        )
        self.wait()
        self.play(FlashAround(tex[1:3]))
        self.wait()


if __name__ == "__main__":
    from os import system

    # system("manimgl {} Picture1Show -o -r 1080x1920".format(__file__))
    system("manimgl {} Picture1Show -o".format(__file__))
