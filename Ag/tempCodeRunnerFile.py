from manimlib import *

if __name__ == "__main__":
    from os import system
    system("manimgl {} CoinFlips -o".format(__file__))

class CoinFlips(Scene):
    def construct(self):
        eq = TexText(
            "{\\# \\text{Heads} \\over \\# \\text{Flips}} = ",
            "{Num \\over Den}", "=", "0.500",
            "{\\text{132}}",
            isolate={"Num", "Den", "\\# \\text{Heads}"}
        )
        self.add(eq)
        self.wait()