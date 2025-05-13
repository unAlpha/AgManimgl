import random

# 堆叠
pile_of_cards = []
# 计数器
counter = 0

# 生成牌堆
for i in range(15):
    for j in range(18):
        pile_of_cards.append(i)

# 循环10000次
for t in range(10000):
    # 洗牌
    random.shuffle(pile_of_cards)
    # 查看前14张牌的种类
    n = len(set(pile_of_cards[0:14]))
    # 如果小于7，让计数器加
    if n < 7:
        counter += 1

# 打印计数器值
print(counter)
