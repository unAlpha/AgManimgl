import random
import numpy as np
import matplotlib.pyplot as plt

"""
下方代码应用于:
2022-09-22_史上最难小游戏“羊了个羊”深度剖析！过不了关是智商有问题吗？
"""

l = []
peak_array = []


def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


for i in range(15):
    for j in range(18):
        l.append(i)

for i in range(100):
    c = 0
    for t in range(1000):
        random.shuffle(l)
        n = len(set(l[0:14]))
        if n < 7:
            c += 1
    peak_array.append(c)
result = np.array(peak_array)
x = np.arange(min(result), max(result), 0.1)
print(result.mean(), result.std())
y = normfun(x, result.mean(), result.std())
plt.plot(x, y)
plt.hist(result, bins=len(set(result)), rwidth=1, density=True)
plt.xlabel("frequency")
plt.ylabel("probalility")
plt.show()
