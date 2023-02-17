from random import sample
from collections import Counter


def get_pk_lst(pls, pks):  # 发牌
    result = []
    for p in pls:
        pk = sample(pks, 3)
        for _pk in pk:
            pks.remove(_pk)
        result.append({"name": p, "poker": pk})
    return result

def calculate(_score_map, pk_lst):  # 返回得分和牌型
    n_lst = list(map(lambda x: _score_map[x], pk_lst))  # 点数映射
    same_suit = len(set([pk[:2] for pk in pk_lst])) == 1  # 是否同花色
    continuity = sorted(n_lst) == [i for i in range(min(n_lst), max(n_lst) + 1)] or set(n_lst) == {14, 2, 3}  # 是否连续
    check = len(set(n_lst))  # 重复情况
    if not same_suit and not continuity and check == 3:
        return sum(n_lst), "单张"
    if not same_suit and check == 2:
        w = [i for i in n_lst if n_lst.count(i) == 2][0]
        single = [i for i in n_lst if i != w][0]
        return w*2*2 + single, "对子"
    if same_suit and not continuity:
        return sum(n_lst)*9, "金花"
    if continuity and not same_suit:
        return sum(n_lst)*81, "顺子"
    if check == 1:
        return sum(n_lst)*666, "豹子"
    if continuity and same_suit:
        return sum(n_lst)*999, "同花顺"

def compare(_score_map, pk_grp, show_f=False):  # 比大小
    if show_f:
        for p in pk_grp:
            p["score"], p["type"] = calculate(_score_map, p["poker"])
        print("开牌结果------")
        for p in pk_grp:
            print(p)
        print("赢家是------")
        best = max(pk_grp, key=lambda x: x["score"])["name"]
        print(best)
        return pk_grp
    else:
        for p in pk_grp:
            p["score"], p["type"] = calculate(_score_map, p["poker"])
        return pk_grp

def show(_score_map, _players):   # 开局
    pokers = list(_score_map.keys())
    poker_grp = get_pk_lst(_players, pokers)
    return compare(_score_map, poker_grp)

def start_game(_score_map, _players, freq=1, count_f=1):   # 游戏和统计
    type_lst = []
    if count_f==1:
        for i in range(freq):
            grp = show(_score_map, _players)
            type_lst = type_lst + [t["type"] for t in grp]
        c = Counter(type_lst)
        print(c)
        total = sum(c.values())
        for item in c.items():
            print(f"{item[0]}频率：{item[1]/total:.2%}")
            
    if count_f==2 :
        c = {'单张': 0, '对子': 0, '金花': 0, '顺子': 0, '同花顺': 0, '豹子': 0}
        for i in range(freq):
            grp = show(_score_map, _players)
            type_lst = [t["type"] for t in grp]
            for key in c.keys():
                if key in type_lst:
                    c[key]+=1
        print(c)
        total = len(_players)*freq
        for item in c.items():
            print(f"{item[0]}频率：{item[1]/total:.2%}")

if __name__ == '__main__':
    # 准备扑克牌
    suit = ["黑桃", "红心", "方块", "梅花"]
    num = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    score_map = {}  # 单张点数映射表
    for s in suit:
        count = 2
        for n in num:
            score_map[f"{s}{n}"] = count
            count += 1
    # 6个玩家入场
    players = [f"p{i}" for i in range(1, 5)]
    # 开始游戏
    start_game(score_map, players, freq=10000, count_f=2)