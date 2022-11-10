from manimlib import *

if __name__ == "__main__":
    from os import system
    system("manimgl {} CoinFlips -om".format(__file__))

class CoinFlips(Scene):
    def construct(self):
        eq = TexText(
            "$${\\# \\text{试下} adf \\over \\# \\text{一二三}} = $$",
            # "{Num \\over Den}", "=", "0.500",
            # "{\\text{132}}",
            # isolate={"Num", "Den", "\\# \\text{Heads}"}
        )
        words = TexText("$$Vector...$$").next_to(eq,DOWN)
        self.add(eq)
        self.play(ShowCreation(words))
        self.wait()
        