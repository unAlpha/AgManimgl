# -*- coding: utf-8 -*-
from manimlib import *

class Physics1(Scene):
    Q = """
        \\parbox{11cm}{
        1. 氢原子从某激发态跃迁到基态，则该氢原子（\\quad）
        }
        """
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B. 放出光子，能量减少。当氢原子从激发态跃迁到基态时，
            它会放出光子，同时能量也会减少。这是因为在激发态时，
            氢原子的电子受到了额外的能量激发，而跃迁到基态时，
            电子会释放掉这些额外的能量，通常以光子的形式放出。
            }
        }
        """
    A = "A. 放出光子，能量增加"
    B = "B. 放出光子，能量减少"
    C = "C. 吸收光子，能量增加"
    D = "D. 吸收光子，能量减少"
    Pos = 0
    f = 28
    n_r = 2
    n_c = 2
    h_b = 1.6
    v_b = 0.22
    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        abcd = VGroup()
        for a in [self.A,self.B,self.C,self.D]:
            abcd.add(TexText(a,font_size=self.f,alignment="\\raggedright"))
        abcd.arrange_in_grid(
            self.n_r,
            self.n_c,
            h_buff=self.h_b,
            v_buff=self.v_b,
            aligned_edge=LEFT
            )
        question.to_edge(UL,buff=1)
        abcd.next_to(question,DOWN,buff=0.5,aligned_edge=LEFT)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            FadeIn(question,scale=0.618),
            AnimationGroup(*[FadeIn(obj,scale=0.8,shift=UP) for obj in abcd],lag_ratio=0.1)
            )
        self.wait(2)
        if self.Pos==0:
            answer.next_to(abcd, DOWN, aligned_edge=LEFT, buff=0.5)
        if self.Pos==1:
            self.play(FadeOut(question,shift=UP),
                      abcd.animate.to_edge(UP,buff=1),
                    )
            answer.next_to(abcd, DOWN, aligned_edge=LEFT, buff=0.5)
        if self.Pos==2:
            self.play(FadeOut(question,shift=UP),
                      FadeOut(abcd,shift=UP)
                    )
            answer.next_to(abcd, DOWN, aligned_edge=LEFT, buff=0.5)
            answer.to_edge(UL,buff=1)
        self.play(ShowIncreasingSubsets(*answer),run_time=3)
        self.wait(5)

class Physics2(Physics1):
    Q = """
        \\parbox{11cm}{
        2. 下列现象能说明光是横波是（\\quad）
        }
        """
    A = "A. 光的衍射现象"
    B = "B. 光的折射现象"
    C = "C. 光的偏振现象"
    D = "D. 光的干涉现象"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：C. 光的偏振现象。偏振是指波在传播方向上振动方向的特定取向，
            如果光是横波，则它的振动方向应该垂直于传播方向，因此只有横波才
            能表现出偏振现象。而光的衍射、折射和干涉现象并不能直接说明光是
            横波或纵波。
            }
        }
        """
        
class Physics3(Physics1):
    Q = """
        \\parbox{11cm}{
        3. 某理想变压器的原线圈接在220V的正弦交流电源上，
        副线圈输出电压为22000V，输出电流为300mA。该变压器（\\quad）
        }
        """
    A = "A. 原、副线圈的匝数之比为100:1"
    B = "B. 输入电流为30A"
    C = "$$\\text{C. 输入电流的最大值为15}\\sqrt{2}\\text{A}$$"
    D = "D. 原、副线圈交流电的频率之比为1:100"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A。原线圈的电流为$I_1 = \\frac{V_2}{V_1}I_2$，
            其中，$V_1$ 和$V_2$分别是原线圈和副线圈的电压，$I_1$和 $I_2$
            分别是原线圈和副线圈的电流。
            将给定的数值代入上式，得到：$I_1= \\frac{2200V}{220V}0.3A=30A$因此，
            输入电流为30A，答案B不正确。...
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1
        
class Physics4(Physics1):
    Q = """
        \\parbox{11cm}{
        4. “雪如意”是我国首座国际标准跳台滑雪场地。
        跳台滑雪运动中，裁判员主要根据运动员在空中的飞行距离和动作姿态评分。
        运动员在进行跳台滑雪时大致经过四个阶段：...（\\quad）
        }
        """
    A = "A. 助滑阶段，运动员深蹲是为了减小与滑道之间的摩擦力"
    B = "B. 起跳阶段，运动员猛蹬滑道主要是为了增加向上的速度"
    C = "C. 飞行阶段，运动员所采取的姿态是为了增加水平方向速度"
    D = "D. 着陆阶段，运动员两腿屈膝是为了减少与地面的作用时间"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B. 起跳阶段，运动员猛蹬滑道主要是为了增加向上的速度，是正确的。
            在跳台滑雪起跳区，运动员通过猛蹬滑道将滑行能量转化为向上的速度，
            并且尽可能快地使自己脱离滑道，...
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class Physics5(Physics1):
    Q = """
        \\parbox{11cm}{
        5. 2021年5月，中国科学院全超导托卡马克核聚变实验装置取得新突破，
        成功实现了可重复的1.2亿摄氏度101秒和1.6亿摄氏度20秒等离子体运行，
        ... ...
        下列说法不正确的是（\\quad）
        }
        """
    A = "A. 核聚变释放的能量源于等离子体中离子的动能"
    B = "B. 可以用磁场来约束等离子体"
    C = "C. 尽管等离子体整体是电中性的，但它是电的良导体"
    D = "D. 提高托卡马克运行温度有利于克服等离子体中正离子间的库仑斥力"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答案：D. 提高托卡马克实验装置的运行温度
            可以增加正离子的动能，以克服正离子之间的库仑斥力，从而使等离子体保持稳定，
            选项D是不正确的。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class Biology1(Physics1):
    Q = """
        \\parbox{11cm}{
        1. 鱼腥蓝细菌分布广泛，它不仅可以进行光合作用，还具有固氮能力。
        关于该蓝细菌的叙述，不正确的是（\\quad）
        }
        """
    A = "A. 属于自养生物"
    B = "B. 可以进行细胞呼吸"
    C = "C. DNA位于细胞核中"
    D = "D. 在物质循环中发挥作用"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：C. DNA位于细胞核中是不正确的。鱼腥蓝细菌是原核生物，其细胞结构简单，
            没有真核细胞的特征，包括细胞核，其DNA位于质粒中。其它选项均正确，
            鱼腥蓝细菌属于自养生物，可以进行光合作用和细胞呼吸，
            并且在物质循环中发挥着重要作用，如固氮。
            }
        }
        """
    Pos = 0

class Biology2(Physics1):
    Q = """
        \\parbox{11cm}{
        2. 蜜蜂的雌蜂（蜂王和工蜂）为二倍体，由受精卵发育而来；
        雄蜂是单倍体，由未受精卵发育而来。由此不能得出（\\quad）
        }
        """
    A = "A. 雄蜂体细胞中无同源染色体"
    B = "B. 雄蜂精子中染色体数目是其体细胞的一半"
    C = "C. 蜂王减数分裂时非同源染色体自由组合"
    D = "D. 蜜蜂的性别决定方式与果蝇不同"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B。由于蜜蜂的雄蜂是由未受精卵发育而来，所以它的染色体组成是单倍体的，
            只有一套染色体。因此，选项B是正确选项。选项A、C、D都是正确的，
            因此不能由此得出选项A、C、D不正确。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1
    
class Biology3(Physics1):
    Q = r"""
        \parbox{11cm}{
        3. 人与黑猩猩是从大约700万年前的共同祖先进化而来，两个物种成体的血红蛋白均由
        $\alpha$和$\beta$两种肽链组成，但$\alpha$链的相同位置上有一个氨基酸不同，
        据此不能得出（\quad）
        }
        """
    A = "A. 这种差异是由基因中碱基替换造成的"
    B = r"B. 两者共同祖先的血红蛋白也有$\alpha$链"
    C = "C. 两者的血红蛋白都能行使正常的生理功能"
    D = "D. 导致差别的变异发生在黑猩猩这一物种形成的过程中"
    Ans = r"""
        \textbf{
            \parbox{11cm}{
            答案为D。根据题目描述，人与黑猩猩是从大约700万年前的共同祖先进化而来，
            两个物种成体的血红蛋白均由α和β两种肽链组成，但$\alpha$链的相同位置上有一个氨基酸不同...   
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1      

class Biology4(Physics1):
    Q = """
        \\parbox{11cm}{
        4. 2022年2月下旬，天安门广场各种盆栽花卉凌寒怒放，喜迎冬残奥会的胜利召开。
        为使植物在特定时间开花，园艺工作者需对植株进行处理，常用措施不包括（\\quad）
        }
        """
    A = "A. 置于微重力场"
    B = "B. 改变温度"
    C = "C. 改变光照时间"
    D = "D. 施用植物生长调节剂"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A. 置于微重力场是指在太空等微重力环境下进行的实验处理，
            对地球上的植物生长没有直接的应用价值，因此常用的园艺措施中
            不包括置于微重力场。其他选项中，改变温度、改变光照时间和施
            用植物生长调节剂都是常用的园艺处理方法，以控制植物的生长和
            开花时间。
            }
        }
        """
    Pos = 0

class Biology5(Physics1):
    Q = """
        \\parbox{11cm}{
        5. 某患者，54岁，因病切除右侧肾上腺。术后检查发现，患者血浆中肾上腺皮
        质激素水平仍处于正常范围。对于出现这种现象的原因，错误的解释是（\\quad）
        }
        """
    A = "A. 切除手术后，对侧肾上腺提高了肾上腺皮质激素的分泌量"
    B = "B. 下丘脑可感受到肾上腺皮质激素水平的变化，发挥调节作用"
    C = "C. 下丘脑可分泌促肾上腺皮质激素，促进肾上腺皮质激素的分泌"
    D = "D. 垂体可接受下丘脑分泌的激素信号，促进肾上腺皮质的分泌功能"
    n_r = 4
    n_c = 1
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：错误的解释是A. 切除手术后，对侧肾上腺提高了肾上腺皮质激素的分泌量。
            因为肾上腺皮质激素的分泌主要是由下丘脑-垂体-肾上腺皮质轴向调节的，
            而非另一侧肾上腺的作用。...
            }
        }
        """
    Pos = 0

class Biology6(Physics1):
    Q = """
        \\parbox{11cm}{
        6. 人体皮肤损伤时，金黄色葡萄球菌容易侵入伤口并引起感染。
        清除金黄色葡萄球菌的过程中，免疫系统发挥的基本功能属于（\\quad）
        }
        """
    A = "A. 免疫防御"
    B = "B. 免疫自稳"
    C = "C. 免疫监视、免疫自稳"
    D = "D. 免疫防御、免疫监视" 
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答案：A. 免疫防御.金黄色葡萄球菌是一种常见的细菌，易在人体皮肤损伤时侵入伤口并引起感染。
            在人体免疫系统中，免疫防御是指通过免疫细胞、抗体等免疫因子对病原体进行消灭和清除，
            保护机体免受病原体侵害。在清除金黄色葡萄球菌的过程中，免疫系统发挥的基本功能是免疫防御。
            }
        }
        """
    Pos = 0

class Biology7(Physics1):
    Q = """
        \\parbox{11cm}{
        7. 将黑色小鼠囊胚的内细胞团部分细胞注射到白色小鼠囊胚腔中，
        接受注射的囊胚发育为黑白相间的小鼠（Mc）。据此分析，下列叙述错误的是（\\quad）
        }
        """
    A = "A. 获得Mc的生物技术属于核移植"
    B = "B. Mc表皮中有两种基因型的细胞"
    C = "C. 注射入的细胞会分化成Mc的多种组织"
    D = "D. 将接受注射的囊胚均分为二，可发育成两只幼鼠"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：D. 将接受注射的囊胚均分为二，可发育成两只幼鼠是错误的。
            将接受注射的囊胚均分为两部分无法发育成两只幼鼠，
            因为内细胞团细胞的注射只会在一个囊胚中发育，...
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class Biology8(Physics1):
    Q = """
        \\parbox{11cm}{
        8. 实验操作顺序直接影响实验结果。下列实验操作顺序有误的是（\\quad）
        }
        """
    A = "\\parbox{10cm}{A. 检测生物组织中的蛋白质时向待测样液中先加双缩脲试剂A液，再加B液}"
    B = "\\parbox{10cm}{B. 观察细胞质流动时先用低倍镜找到特定区域的黑藻叶肉细胞，再换高倍镜观察}"
    C = "\\parbox{10cm}{C. 探究温度对酶活性的影响时室温下将淀粉溶液与淀粉酶溶液混匀后，在设定温度下保温}"
    D = "\\parbox{10cm}{D. 观察根尖分生区组织细胞的有丝分裂时将解离后的根尖用清水漂洗后，再用甲紫溶液染色}"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答案是A。加双缩脲试剂B液会与A液中的蛋白质结合产生沉淀，因此应该先加B液再加A液。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1 

class Biology9(Physics1):
    Q = """
        \\parbox{11cm}{
        9. 下列高中生物学实验中，对实验结果不要求精确定量的是（\\quad）
        }
        """
    A = "A. 探究光照强度对光合作用强度的影响"
    B = "B. DNA的粗提取与鉴定"
    C = "C. 探索生长素类调节剂促进插条生根的最适浓度"
    D = "D. 模拟生物体维持pH的稳定"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            回答：D. 模拟生物体维持pH的稳定是一个定性实验，
            不需要对实验结果进行精确定量。选项A、C需要对光照强度和生长素类
            调节剂浓度进行精确的定量测量，选项B需要准确地确定DNA的含量和纯度。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class Biology10(Physics1):
    Q = """
        \\parbox{11cm}{
        10. 2022年4月，国家植物园依托中科院植物所和北京市植物园建立，
        以植物易地保护为重点开展工作。这些工作不应包括（\\quad）
        }
        """
    A = "A. 模拟建立濒危植物 原生生境"
    B = "B. 从多地移植濒危植物"
    C = "C. 研究濒危植物的繁育"
    D = "D. 将濒危植物与其近缘种杂交培育观赏植物"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：D. 将濒危植物与其近缘种杂交培育观赏植物。这一项工作不符合植物易地保护的宗旨，
            易地保护的目标是保护植物物种多样性、维护生态系统稳定和保障人类福利，
            而不是杂交培育观赏植物。...
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1
    
class History1(Physics1):
    Q = """
        \\parbox{11cm}{
        1. 近年，考古工作者在江西国字山发现了战国中期的大型墓葬。
        该墓葬具有突出的越文化特征，同时又有楚文化和江淮文化等文化因素，
        墓葬形制也与中原墓葬有相似之处。此考古发现（\\quad）
        }
        """
    A = "A. 印证了“春秋五霸”的政治格局"
    B = "B. 反映了中华文明多元一体的特点"
    C = "C. 证明中原率先成为中华文明核心"
    D = "D. 说明了统一多民族国家已经建立"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B，考古发现具有多元文化特征，反映了中华文明的多元一体性。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class History2(Physics1):
    Q = """
        \\parbox{11cm}{
        2. 北宋中期，各地知州积极修建亭台馆榭以供民众游玩，
        甚至将其作为一项重要政务。欧阳修《丰乐亭记》载：“夫宣上恩德，
        以与民共乐，刺史之事也。”范仲淹曾在名胜“严子陵钓台”边修建先
        贤祠堂以“咏其风”，认为这样“有大功于名教”。上述材料佐证了北宋（\\quad）
        """
    A = "A. 注重推行社会教化"
    B = "B. 放松了对经济的控制"
    C = "C. 鼓励文学艺术创作"
    D = "D. 实行崇文抑武 方针" 
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，北宋注重推行社会教化，修建亭台馆榭供民众游玩，并将其作为政务之一。
            }
        }
        """
    Pos = 0

class History3(Physics1):
    Q = """
        \\parbox{11cm}{
        3. 西方有“条条大路通罗马”的说法，中国古代也有“处处有路透长安”的谚语。
        这两句话蕴含的历史信息是（\\quad）
        }
        """
    A = "A. 长安城的设计借鉴了罗马城市布局"
    B = "B. 长安和罗马两地之间的交通网络密集"
    C = "C. 古代商路便利了东西方之间的文化交流"
    D = "D. 长安和罗马都曾经是帝国交通网络的中心"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答. C，上古丝绸之路和中世纪东西方交流等历史事件反映了古代商路便利了东西方之间的文化交流。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1 

class History4(Physics1):
    Q = """
        \\parbox{11cm}{
        4. 《海国图志》问世不久即传入日本，当时著名学者佐久间象山
        感叹自己与魏源“所见亦有暗合者”“真可谓海外同志”，另一日本
        学者感慨道：“使海内尽得观之，庶乎其为我边防之一助矣！”
        这表明此时中日两国的有识之士（\\quad）
        }
        """
    A = "A. 有了“开眼看世界”的意识"
    B = "B. 主张中日结盟以反对西方的侵略"
    C = "C. 产生了反对封建专制的思想"
    D = "D. 掀起了“师夷长技”的社会运动"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，有了“开眼看世界”的意识，表明中日两国的有识之士认识到需要学习西方的先进技术和制度，提高中华民族的综合素质。
            }
        }
        """
    Pos = 0
    h_b = -0.2

class History5(Physics1):
    Q = """
        \\parbox{11cm}{
        5. 1898年，英国发出照会，要求清政府“确切保证不将扬子江（注：长江）
        沿岸各省租押或以其他名义让予他国”。清政府答复称：“查扬子江沿岸地方
        均属中国要地，中国断不让予或租给他国。”这意味着（\\quad）
        }
        """
    A = "A. 英国将长江流域辟为殖民地"
    B = "B. 长江流域成为英国势力范围"
    C = "C. “门户开放”政策宣告失败"
    D = "D. 清政府成功维护了主权完整"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：D，英国要求清政府保证长江沿岸各省不被租押或让予他国，清政府则成功维护了主权完整。
                }
            }
        """
    Pos = 0
    h_b = 0.3

class History6(Physics1):
    Q = """
        \\parbox{11cm}{
        6. 1946年4月8日，中共代表王若飞、博古等人参加政治协商会议后，
        从重庆返回延安途中因飞机失事遇难，民主人士、国民党要员等社会各
        界纷纷表示哀悼。有悼文指出：“他们的事业，就是中国人民大众的事业，
        就是全人类的事业。”这反映出当时中国社会各界（\\quad）
        }
        """
    A = "A. 拥护抗日民族统一战线"
    B = "B. 反对国民党政权的统治"
    C = "C. 希望建立无产阶级政权"
    D = "D. 企盼国家实现和平民主"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：D，王若飞等人的逝世引起了中国社会各界的广泛关注，表明当时中国社会各界企盼国家实现和平民主。
            }
        }
        """
    Pos = 0
    h_b = 0.3

class History7(Physics1):
    Q = """
        \\parbox{11cm}{
        7. 1950年，教育部要求各高校“废除政治上的反动课程”，
        开设“辩证唯物论与历史唯物论”等课程；1956年，“马列主义
        基础”和“中国革命史”被列入高校必修课。这些高校课程的调整（\\quad）
        """
    A = "A. 贯彻了新民主主义和社会主义教育方针"
    B = "B. 标志着国家“科教兴国”发展战略形成"
    C = "C. 成为社会主义“三大改造”的思想基础"
    D = "D. 推行了“百花齐放”“百家争鸣”的方针"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，高校课程的调整贯彻了新民主主义和社会主义教育方针。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class History8(Physics1):
    Q = """
        \\parbox{11cm}{
        8. 2004年7月，“为中国和非洲喝彩——中华文化非洲行”活动在南非开幕。
        在一个月 时间里，中国组派多个艺术团赴11个非洲国家访问演出。
        这是中国在非洲大陆首次举办的大规模、综合性中国文化活动，
        是中非合作论坛框架内的重要举措。这一活动（\\quad）
        }
        """
    A = "A. 是中国重视发展周边关系的具体实践"
    B = "B. 掀起了中国与非洲国家的建交高潮"
    C = "C. 是中国全方位对外开放战略 一部分"
    D = "D. 有利于“金砖国家”合作机制的深化"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，此次活动是中国重视发展周边关系的具体实践。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class History9(Physics1):
    Q = r"""
        \parbox{11cm}{
        9. 英国学者马丁·贝尔纳在其著作《黑色雅典娜：古典文明的亚非之根》中，
        批判了关于希腊文明起源的传统观点，提出希腊文明的源头在西亚和北非。
        下列希腊文明成果，能印证这一观点的是（\quad）$\newline$
        $\textcircled{1}$字母文字 \qquad
        $\textcircled{2}$雕刻艺术 \qquad
        $\textcircled{3}$民主政治 \qquad
        $\textcircled{4}$冶铁技术 \qquad
        }
        """
    A = r"A. $\textcircled{1}$$\textcircled{2}$$\textcircled{3}$"
    B = r"B. $\textcircled{1}$$\textcircled{2}$$\textcircled{4}$"
    C = r"C. $\textcircled{1}$$\textcircled{3}$$\textcircled{4}$"
    D = r"D. $\textcircled{2}$$\textcircled{3}$$\textcircled{4}$"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B，马丁·贝尔纳的观点是希腊文明的源头在西亚和北非，而字母文字、雕刻艺术、冶铁技术均来自该地区。
            }
        }
        """
    Pos = 0 
    n_r = 1
    n_c = 4
    h_b = 1.2

class History10(Physics1):
    Q = """
        \\parbox{11cm}{
        10. 英国议会最初由封建教俗贵族组成，旨在协助国王解决财政困难。
        1265年骑士和城市市民代表首次参加议会，并于1341年起单独议事，
        最终组成议会下院。通过议会，国王在一定程度上获得了金钱和人力的支持，
        而议会亦可向国王提出请愿。关于中世纪英国议会，下列说法正确的是（\\quad）
        }
        """
    A = "A. 国王可不经议会同意而加征新税"
    B = "B. 下院形成标志着君主立宪制建立"
    C = "C. 城市市民是国王联合的重要对象"
    D = "D. 贵族通过议会掌握了国家行政权"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：B，下院形成标志着君主立宪制建立。
            }
        }
        """
    Pos = 0
    n_r = 4
    n_c = 1

class History11(Physics1):
    Q = r"""
        \parbox{11cm}{
        11. 1625年，格劳秀斯在《战争与和平法》中提出，国际法是主权者之间确定
        并相互认可的一套规则，此书奠定了国际法的基础。下列选项属于国际法的是（\quad）$\newline$
        $\textcircled{1}$《威斯特伐利亚和约》   $\newline$
        $\textcircled{2}$《拿破仑法典》        $\newline$
        $\textcircled{3}$《解放黑人奴隶宣言》   $\newline$
        $\textcircled{4}$《联合国宪章》        $\newline$
        }
        """
    A = r"A. $\textcircled{1}$$\textcircled{2}$"
    B = r"B. $\textcircled{3}$$\textcircled{4}$"
    C = r"C. $\textcircled{2}$$\textcircled{3}$"
    D = r"D. $\textcircled{1}$$\textcircled{4}$"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：D，国际法包括联合国宪章在内的一套国际规则和准则。
                }
            }
        """
    Pos = 0
    n_r = 1
    n_c = 4 

class History12(Physics1):
    Q = r"""
        \parbox{11cm}{
        12. 19世纪70—80年代，美国商人斯威夫特创办了肉类加工厂，
        把屠宰和包装分成几道独立工序，利用传送带进行流水作业，
        并雇佣工程师设计冷冻车厢，以便长途运输鲜肉。他还陆续开办工厂，
        利用肉类加工厂的下脚料生产肥料、肥皂和甘油等。斯威夫特的经营模式（\quad）$\newline$
        $\textcircled{1}$体现了产业分工不断细化   
        \quad $\textcircled{2}$得益于铁路交通业的发展   $\newline$
        $\textcircled{3}$成为近代机械生产的开端   
        \quad $\textcircled{4}$为农业现代化提供了范本
        }
        """
    A = r"A. $\textcircled{1}$$\textcircled{2}$"
    B = r"B. $\textcircled{3}$$\textcircled{4}$"
    C = r"C. $\textcircled{2}$$\textcircled{3}$"
    D = r"D. $\textcircled{1}$$\textcircled{4}$"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，斯威夫特的经营模式体现了产业分工不断细化，得益于铁路交通业的发展。
                }
            }
        """
    Pos = 0
    n_r = 1
    n_c = 4 

class History13(Physics1):
    Q = r"""
        \parbox{11cm}{
        13. 下列史料涉及的历史事件，按时序排列正确的是（\quad）$\newline$
        $\textcircled{1}$“三国之宗旨，在剥夺日本自从1914年第一次世界大战开始后...”   $\newline$
        $\textcircled{2}$“（八日）彼得格勒戍军与劳动社会己推翻克伦斯基政府...”   $\newline$
        $\textcircled{3}$“（中美）两国人民之间的来往中断了二十多年。...”   $\newline$
        $\textcircled{4}$“捷克斯洛伐克政府将被责成履行撤退...”   $\newline$
        }
        """
    A = r"A. $\textcircled{1}$$\textcircled{2}$$\textcircled{3}$$\textcircled{4}$"
    B = r"B. $\textcircled{2}$$\textcircled{4}$$\textcircled{1}$$\textcircled{3}$"
    C = r"C. $\textcircled{2}$$\textcircled{1}$$\textcircled{4}$$\textcircled{3}$"
    D = r"D. $\textcircled{4}$$\textcircled{2}$$\textcircled{3}$$\textcircled{1}$"
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            答：A，$\\textcircled{1}$“三国之宗旨……归还中华民国。”是《开罗宣言》中关于归还中国领土主权的承诺；
            $\\textcircled{2}$是俄国十月革命后苏维埃政权的建立；$\\textcircled{3}$是1972年尼克松访华之后的一句话；
            $\\textcircled{4}$是《慕尼黑协定》签订后，纳粹占领捷克斯洛伐克的声明。
            因此，答案为C，$\\textcircled{2}$$\\textcircled{1}$$\\textcircled{4}$$\\textcircled{3}$。
                }
            }
        """
    Pos = 0
    n_r = 1
    n_c = 4 
    h_b = 0.8

class English1(Scene):   
    Q = """
        \\qquad One Monday morning, while the children were enjoying “free play”,
        I stepped to the doorway of the classroom to take a break. Suddenly, 
        I (1) a movement of the heavy wooden door. 
        This was the very door I (2) guided the children through to ensure 
        their safety from the bitter cold. I felt a chill (寒意) go through my body. \\par
        \\qquad My legs carried me to that door, and I pushed it open. 
        It was one of my kindergarteners who I thought was (3) that day. 
        He had been dropped off at school late and was (4) to open the door.\\par
        \\qquad He must have been waiting there for quite a while! Without a word, I rushed him to 
        the hospital. He was treated for frostbite on his hands. 
        He’d need time to (5) , and wouldn’t come for class the next day, 
        I thought.\\par
        \\qquad The next morning, one of the first to (6) was my little frostbitten boy. 
        Not only did he run in with energy, but his (7) could be heard as loud as ever! 
        I gave him a warm hug and told him how (8) I was to see him. His words 
        have stayed with me all these years, 
        “I knew you would open the door.”\\par
        \\qquad That cold Monday morning, he waited a long, long while for adults to (9). 
        To a child, every minute feels like forever. 
        He didn’t attempt to walk back home; he waited and trusted. 
        This five-year-old taught me a powerful lesson in (10) .

        """
    A = [["1. A. caused","B. spotted","C. checked","D. imagined"],
         ["2. A. hesitantly","B. randomly","C. dizzily","D. carefully"],
         ["3. A. angry","B. absent","C. special","D. noisy"],
         ["4. A. courageous","B. content","C. unable","D. unwilling"],
         ["5. A. recover","B. play","C. change","D. wait"],
         ["6. A. settle","B. gather","C. arrive","D. react"],
         ["7. A. sneeze","B. weep","C. complaint","D. laughter"],
         ["8. A. lucky","B. happy","C. curious","D. nervous"],
         ["9. A. show up","B. pull up","C. hold up","D. line up"],
         ["10. A. gratitude","B. forgiveness","C. faith","D. kindness"]]
    Ans = """
        \\textbf{
            \\parbox{10cm}{
            答：
            1. B.spotted \\quad
            2. D.carefully \\quad
            3. B.absent \\quad
            4. C.unable \\quad
            5. A.recover \\quad
            6. C.arrive \\quad
            7. D.laughter \\quad
            8. B.happy \\quad
            9. A.show up \\quad
            10. C.faith
            }
        }
        """
    f = 20
    
    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        abcd = VGroup()
        abcd_ = VGroup()
        kb = 4
        for a in self.A:
            for b in a:
                abcd.add(TexText(b,font_size=self.f,alignment="\\raggedright"))
        for words in [abcd[i:i+kb] for i in range(0, len(abcd), kb)]:
            VgWds = VGroup()
            for word in words:
                VgWds.add(word)
            abcd_.add(VgWds)

        abcd.arrange_in_grid(4,4,h_buff=0.1,v_buff=0.2,aligned_edge=LEFT)
        abcd.next_to(question,RIGHT,buff=0.5)
        qa = VGroup(question,abcd).center().to_edge(UP)
        abcd.to_edge(UP)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        answer.next_to(abcd, DOWN, aligned_edge=LEFT, buff=0.5)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            FadeIn(question,scale=0.618),
            AnimationGroup(*[FadeIn(obj,scale=0.8,shift=UP+LEFT*0.618) for obj in abcd_],lag_ratio=0.1)
            )
        self.wait(2)
    
        self.play(ShowIncreasingSubsets(*answer),run_time=3)
        self.wait(5)

class English2(English1): 
    Q = """
        \\parbox{16cm}{
        \\qquad Tom, a 15-year-old inventor and entrepreneur (创业者), 
        witnessed at his own school the widespread consumption of sugary drinks by kids. 
        He knew there had to be a better portable drink solution and decided to innovate 
        from something he saw in his own home: fruit infused (浸泡) water.\\par
        \\qquad Tom watched his mum make healthy fruit infusions but then struggle for 
        a take-along option. From observing his mum and from his desire to give 
        kids better drink options, he came up with his original model for the Fun Bottle.
        “I wanted to come up with a healthy, natural way for people to drink 
        when on the go. A big part of my mission is to get people of all ages off sugary
        drinks,” Tom explains.\\par
        \\qquad The bottle is made with a strainer (滤网) that 
        allows the great tastes and natural sugars of the various fruits and vegetables 
        you choose to come through the water, without any of the seeds or 
        skins flowing through.\\par
        \\qquad Tom is proud of his design and excited to be selling the Fun Bottle 
        on his website and in stores  but this 15-year-old is most proud of the 
        opportunities that Fun Bottle presents to others. 
        It helps to provide healthy alternatives to sugary drinks; and also 
        Tom donates part of the profits to the Organisation for a Healthier 
        Generation (OHG).Tom has been awarded several prizes, but this 
        teenage innovator remains humble. When asked what advice he’d give 
        other entrepreneurial youth, he says, “Prepare and have your family’s 
        support. It is important to know from the beginning that there are a 
        lot of highs and lows, and there is no such thing as overnight success.”\\par
        \\qquad 40. What did Tom witness at his own school? \\par
        \\qquad 41. Where did Tom get the idea for the original model 
        for the Fun Bottle? \\par
        \\qquad 42. Please decide which part is false in the following statement, 
        then underline it and explain why. 
        Tom is most proud of the opportunities that Fun Bottle presents to 
        others because he not only provides healthy alternatives to sugary 
        drinks but also donates all the profits to the OHG.\\par
        \\qquad 43. Among Tom’s qualities, which one(s) do you think 
        will be important for us? Why?(In about 40 words)
        }
        """  
    Ans = """
        \\parbox{11.5cm}{
        答：\\par
        40.	Tom witnessed the widespread consumption of sugary drinks by 
        kids at his own school.\\par
        41.	Where did Tom get the idea for the original model 
        for the Fun Bottle? Tom got the idea for the original 
        model for the Fun Bottle from observing his mum make 
        healthy fruit infusions but then struggle for a take-along 
        option.\\par
        42.	Please decide which part is false in the following statement, 
        then underline it and explain why. Tom is most proud of the opportunities 
        that Fun Bottle presents to others because he not only provides healthy 
        alternatives to sugary drinks but also donates all the profits to 
        the OHG. The false part of the statement is "donates all the profits 
        to the OHG." The passage states that Tom donates part of the profits to 
        the Organisation for a Healthier Generation (OHG), not all of the 
        profits.\\par
        43.	Among Tom’s qualities, which one(s) do you think will be important 
        for us? Why?(In about 40 words) One of Tom's qualities that will be 
        important for us is his perseverance. He advises other entrepreneurial 
        youth to prepare for a lot of highs and lows, and that there is no such 
        thing as overnight success. This quality is important because it 
        emphasizes the importance of hard work and determination in achieving 
        one's goals.
            }
        """
    f = 16

    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        question.center().to_edge(UL)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        answer.next_to(question, RIGHT, buff=0.5)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            FadeIn(question,scale=0.618),
            )
        self.wait(2)
        self.play(ShowIncreasingSubsets(*answer),run_time=3)
        self.wait(5)

class English3(Scene):
    Q = """
        \\parbox{14cm}{
            \\qquad 假设你是红星中学高三学生李华。你打算邀请英国好友Jim为你们班做一次关于
            英语写作的线上经验交流。请你用英文给他写一封电子邮件，内容包括：\\par 
            \\qquad 1．建议交流的具体内容及其原因；\\par 
            \\qquad 2．交流时间和其他相关事项。
        }
        """
    Ans = """
        \\parbox{14cm}{
            Dear Jim, \\par 
            \\qquad How are you? I hope you are doing well. I am writing to invite you to 
            give an online talk to my classmates and me about English writing.\\par 
            \\qquad As you know, we are high school seniors in China and we need to take 
            the English exam for college admission. Writing is one of the most 
            challenging parts of the exam for us. We would like to learn from your 
            writing experience and skills so that we can improve our writing.\\par 
            \\qquad We plan to have the online talk on the coming Saturday at 10 a.m. 
            Beijing time. We will use Zoom for the meeting. Please let me know if 
            the time is suitable for you. Also, please tell us the specific topic 
            you will talk about and the duration of your talk.\\par 
            \\qquad I am looking forward to your reply.\\par 
            \\qquad Yours,\\par 
            \\qquad Li Hua
            }
        """
    Pos = 0
    f = 28
    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        question.to_edge(UP,buff=0.5)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            FadeIn(question,scale=0.618),
            )
        self.wait(2)
        if self.Pos==0:
            answer.next_to(question, DOWN, buff=0.5) 
        if self.Pos==1:
            self.play(FadeOut(question,shift=UP))
            answer.to_edge(UP,buff=0.5)
        self.play(ShowIncreasingSubsets(*answer),run_time=1) 
        self.wait(2)

class Math(Scene):
    Ans = """
        \\textbf{
            \\parbox{11cm}{
            \\color{yellow}{答：}
            \\color{yellow}{1.D} \\quad
            \\color{yellow}{2.B} \\quad
            \\color{yellow}{3.A} \\quad
            \\color{yellow}{4.C} \\quad
            \\color{red}{5.D} \\quad
            \\color{red}{6.B} \\quad
            \\color{yellow}{7.B} \\quad
            \\color{red}{8.D} \\quad
            \\color{yellow}{9.D} \\quad
            }
        }
        """
    def construct(self):     
        configs1 ={
            "Q" : """
                \\parbox{11cm}{
                1、已知全集$U=\{\left. x|-3<x<3\}$，
                集合$A=\{\left. x|-2<x\le 1\}$，
                则$\complement_{U}A=$（\\quad）
                }
                """,
            "A" : "A. $(-2,1]$",
            "B" : r"B. $(-3,-2)\bigcup [1,3)$",
            "C" : "C. $[-2,1)$",
            "D" : r"D. $(-3,-2]\bigcup (1,3)$",
            "f" : 28,
            "n_r" : 2,
            "n_c" : 2,
            "h_b" : 1.6,
            "v_b" : 0.22,
        }
        configs2 ={
            "Q" : """
                \\parbox{11cm}{
                2. 若某个复数满足$i \cdot z$等于$3-4i$，则这个复数的模等于（\\quad）
                }
                """,
            "A" : "A. 1",
            "B" : "B. 5",
            "C" : "C. 1",
            "D" : "D. -1",
            "n_r" : 1,
            "n_c" : 4,
        }
        configs3 ={
            "Q" : """
                \\parbox{11cm}{
                3. 若直线$2x+y-1=0$是圆${{(x-a)}^{2}}+{{y}^{2}}=1$的一条对称轴，则a=（\\quad）
                }
                """,
            "A" : r"A. $\frac{1}{2}$",
            "B" : r"B. $-\frac{1}{2}$",
            "C" : "C. 7",
            "D" : "D. 25",
            "n_r" : 1,
            "n_c" : 4,
        }
        configs4 ={
            "Q" : """
                \\parbox{11cm}{
                4. 己知函数$f(x)=\\frac{1}{1+2^x}$，则对任意实数x，有（\\quad）
                }
                """,
            "A" : r"A. $f(-x)+f(x)=0$",
            "B" : r"B. $f(-x)-f(x)=0$",
            "C" : r"C. $f(-x)+f(x)=1$",
            "D" : r"D. $f(-x)-f(x)=\frac{1}{3}$",
            "n_r" : 2,
            "n_c" : 2,
        }
        configs5 ={
            "Q" : """
                \\parbox{11cm}{
                5.已知函数$f(x)={{\cos }^{2}}x-{{\sin }^{2}}x$，则（\\quad）
                }
                """,
            "A" : r"A. $f(x)$在$\left( -\frac{\pi }{2},-\frac{\pi }{6} \right)$上单调递减",
            "B" : r"B. $f(x)$在上单调递增$\left( -\frac{\pi }{4},\frac{\pi }{12} \right)$",
            "C" : r"C. $f(x)$在$\left( 0,\frac{\pi }{3} \right)$上单调递减",
            "D" : r"D. $f(x)$在$\left( \frac{\pi }{4},\frac{7\pi }{12} \right)$上单调递增",
            "n_r" : 2,
            "n_c" : 2,
            "h_b" : 0.2,
        }
        configs6 ={
            "Q" : """
                \\parbox{11cm}{
                6. 设$\left\{ {{a}_{n}}\}$是公差不为0的无穷等差数列，
                则“$\left\{ {{a}_{n}}\}$为递增数列”是“存在正整数${N}_{0}$，
                当$n>{{N}_{0}}$时，${{a}_{n}}>0$”的（\\quad）
                }
                """,
            "A" : "A. 充分而不必要条件",
            "B" : "B. 必要而不充分条件",
            "C" : "C. 充分必要条件",
            "D" : "D. 既不充分也不必要条件",
            "n_r" : 2,
            "n_c" : 2,
            "h_b" : 1.6,
        }
        configs7 ={
            "Q" : """
                \\parbox{11cm}{
                7. 若${{(2x-1)}^{4}}={{a}_{4}}{{x}^{4}}+{{a}_{3}}{{x}^{3}}+{{a}_{2}}{{x}^{2}}+{{a}_{1}}x+{{a}_{0}}$，
                则${{a}_{0}}+{{a}_{2}}+{{a}_{4}}$=（\\quad）
                }
                """,
            "A" : "A. 40",
            "B" : "B. 41",
            "C" : "C. -40",
            "D" : "D. -41",
            "n_r" : 1,
            "n_c" : 4,
        }
        configs8 ={
            "Q" : """
                \\parbox{11cm}{
                8. 已知正三棱锥$P-ABC$ 六条棱长均为6，$S$是$\\vartriangle ABC$
                及其内部的点构成的集合．设集合$T=\left\{ \left. Q\in S |PQ\le 5 \}$，
                则T表示的区域的面积为（\\quad）
                }
                """,
            "A" : r"A. $\frac{3\pi }{4}$",
            "B" : "B. $ \pi $",
            "C" : "C. $2 \pi $",
            "D" : "D. $3 \pi $",
        }
        configs9 ={
            "Q" : """
                \\parbox{11cm}{
                9. 在$\\vartriangle ABC$中，$AC=3,BC=4,\\angle C=90{}^\circ $．$P$为
                $\\vartriangle ABC$所在平面内的动点，且$PC=1$，则$\\overrightarrow{PA}
                \\cdot \\overrightarrow{PB}$的取值范围是（\\quad）
                }
                """,
            "A" : "A. $[-5,3]$",
            "B" : "B. $[-3,5]$",
            "C" : "C. $[-6,4]$",
            "D" : "D. $[-4,6]$",
            "h_b" : 1.2,
        }
        qas = VGroup()
        for configtmp in [
                configs1,
                configs2,
                configs3,
                configs4,
                configs5,
                configs6,
                configs7,
                configs8,
                configs9,
            ]:
            qas.add(self.config(**configtmp))
            if len(qas)>1:
                qas[-1].next_to(qas[-2],DOWN,buff=0.3,aligned_edge=LEFT)
        answer= TexText(self.Ans, font_size=self.f, alignment="\\raggedright")
        
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        
        self.play(
            AnimationGroup(*[FadeIn(obj,scale=0.8,shift=UP) for obj in qas],lag_ratio=0.1)
            )
        self.wait()
        
        # 正常使用
        # self.play(qas.animate.to_edge(DOWN,buff=2.8),run_time=8,rate_func=linear)
        # answer.next_to(qas, DOWN, buff=0.5)
        
        # 截图使用
        answer.next_to(qas, DOWN, buff=0.3)
        VGroup(answer,qas).center().scale(0.5)
        # system("manimgl {} Math -os -r 1200x1900".format(__file__))
           
        self.wait()
        self.play(ShowIncreasingSubsets(*answer),run_time=1) 
        self.wait(2)
        
    def config(self,**configs):
        digest_config(self,configs)
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        abcd = VGroup()
        for a in [self.A,self.B,self.C,self.D]:
            abcd.add(TexText(a,font_size=self.f,alignment="\\raggedright"))
        abcd.arrange_in_grid(
            self.n_r,
            self.n_c,
            h_buff=self.h_b,
            v_buff=self.v_b,
            aligned_edge=LEFT
            )
        question.to_edge(UL,buff=1)
        abcd.next_to(question,DOWN,buff=0.2,aligned_edge=LEFT)
        return VGroup(question,abcd)

class Language1(Scene):
    Q = """
        \\parbox{14cm}{
        \\qquad 微写作，按要求作答。不超过150字。校学生会成立新社团“悦读会”，要拟一则招新启事。 
        请你围绕“阅读带来审美愉悦”这一宗旨，为启事写一段话。
        要求：语言简练，有吸引力。（10分）
        }
        """
    Ans = """
    \\textbf{
        \\parbox{14cm}{
        \\qquad 欢迎加入“悦读会”\\:！我们相信，阅读是一种美好的享受，
        它可以带给我们深度的思考、丰富的想象和无穷的乐趣。在这里，
        你可以和志同道合的朋友们分享你的阅读心得，一起探索文学、艺术、哲学等各领域的美好，
        一起感受阅读带来的审美愉悦。无论你是文艺青年还是对知识充满渴望的学子，
        无论你是想要提高阅读素养还是寻找阅读的共鸣，
        我们都欢迎你的加入！让我们一起在阅读中寻找美好，
        一起度过一个充满激情的学期！
            }
        }
        """
    f = 28
    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        question.to_edge(UP,buff=1)
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        
        # 正常使用
        # answer.next_to(question, DOWN, buff=0.5)
        
        # 截图使用
        bg.scale(1.5)
        answer.next_to(question, DOWN, buff=0.3)
        VGroup(answer,question).center().scale(1.6)
        # system("manimgl {} Language1 -os -r 1100x450".format(__file__))
    
        self.play(
            FadeIn(question,scale=0.618),
            )
        self.wait(2)
        self.play(ShowIncreasingSubsets(*answer),run_time=1) 
        self.wait(2)
               
class Language2(Scene):
    Q = """
        \\parbox{13cm}{
        大作文有50分：按要求作答。不少于700字。\\par 
        {\\kaishu \\qquad 古人说，“学不可以已”，重视学习是中华民族的优良传统。在当代中国，
        人们对学习的理解与古人有相同之处，也有不一样的地方。}\\par
        \\qquad 请以“学习今说”为题目，写一篇议论文。
        可以从学习 目的、价值、内容、方法、途径、评价标准等方面，任选角度谈你的思考。\\par
        \\qquad 要求：论点明确，论据充实，论证合理；语言流畅，书写清晰。
        }
        """
    f = 28
    def construct(self):
        question = TexText(self.Q, font_size=self.f,alignment="\\raggedright")
        question.to_edge(UP,buff=1)
        bg = FullScreenRectangle(fill_color=["#032348","#46246d","#31580a","#852211"])
        self.add(bg)
        self.play(
            FadeIn(question,scale=0.618),
            )
        self.wait(2)
        # self.play(FadeOut(question,shift=UP))
        # self.wait(2)
    
class Language2Ans(Scene):
    Ans = """
        \\parbox{13cm}{
            \\qquad 随着时代的发展，学习在现代社会中的地位和作用越来越重要。
            在中国这个历史悠久的国家，重视学习的传统始终流传至今。
            然而，现代人们对学习的理解已经与古人有所不同，学习不再仅仅是一种自我修养，
            更是获取知识、提高素质的必要手段，具有广泛而深远的价值。\\par
            \\qquad 首先，学习的目的是提高个人素质、拓展视野和增长知识。在当今时代，
            知识更新换代的速度日益加快，个人素质和专业技能的要求也越来越高。因此，
            人们需要通过学习来适应社会发展的需要，不断提升自己的素质和能力，
            从而适应社会竞争的压力。\\par
            \\qquad 其次，学习的价值在于促进人的全面发展。学习不仅仅是为了获得技能和知识，
            更是为了拓宽视野、增强思维能力和提高人的综合素质。通过学习，人们可以学到更多的知识和技能，
            同时也可以提高自己的人文素质和道德修养，让自己成为一个更全面和更完整的人。\\par
            \\qquad 学习的内容和方法也在不断地变化和更新。现代人们需要学习的知识和技能不仅仅是传统的
            文化和理论，也包括信息技术、管理、创新等方面的知识。同时，学习的方式也在不断创新和拓展，
            不再仅仅局限于传统的课堂教学，也包括网络教育、远程教育等多种方式。\\par
            \\qquad 对于学习的评价标准也在不断变化。传统的考试评价方式已经无法满足当今社会的需求，
            现代人们更加重视综合素质和实际能力的评价。因此，学校和社会需要开展多种形式的评价方式，
            如综合素质评价和能力测试，以更好地反映学生的真实水平和能力。\\par
            \\qquad 在当代中国，学习的途径也日益丰富多彩。除了传统的学校教育，
            人们还可以通过自学、网络教育等多种途径获取知识。无论是在校学生还是社会人群，
            都可以通过这些渠道获得知识和技能，实现自我价值的最大化。\\par
            \\qquad 总之，学习是一个不断进步的过程。当代人对学习的理解和态度已经发生了很大的变化，
            但始终没有改变的是学习的重要性。我们应该坚持不懈地学习，不断完善自己的知识结构，
            提高自己的素质能力，为自己和社会做出更大的贡献。
        }
        """
    f = 28
    def construct(self):
        answer= TexText(self.Ans, color=YELLOW, font_size=self.f, alignment="\\raggedright")
        answer.to_edge(UP,buff=1)
        self.play(ShowIncreasingSubsets(*answer[0:6]),run_time=3)
        self.play(answer.animate.to_edge(DOWN,buff=1),run_time=7)
        self.wait(2)

if __name__ == "__main__":
    from os import system
    system("manimgl {} Math -os -r 1200x1900".format(__file__))