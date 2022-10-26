from manimlib import *

if __name__ == "__main__":
    from os import system
    system("manimgl {} CoinFlips -o".format(__file__))

class CoinFlips(Scene):
    def construct(self):

        # eq = Tex(
        #     "{\\# \\text{Heads} \\over \\# \\text{Flips}} = ",
        #     "{Num \\over Den}", "=", "0.500",
        #     # isolate={"Num", "Den", "\\# \\text{Heads}"}
        # )
        # for s, rt in (slice(0, 16), 8), (slice(18, None), 20):
        #     print(s)
        #     print(rt)
            
        print(slice(0, 16))    
        # self.add(eq)
        # self.wait()