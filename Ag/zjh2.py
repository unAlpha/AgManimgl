import random

def choise_one(*args):
    """随机生成一张牌"""
    color = ["黑桃", "梅花", "方块", "红心"]
    pai_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    choise_result = random.sample(color,1) + random.sample(pai_value,1)
    return choise_result

def how_many(num):
    """发牌器，"""
    pai_baners = []
    pai_baners.append(choise_one())
    #列表的数量必须是3的倍数
    while len(pai_baners) % (num*3) != 0:
        result = choise_one()
        #判断重复，如果重复就重新再发一张牌
        if result not in pai_baners:
            pai_baners.append(result)
        else:
            continue
    return pai_baners

if __name__ == '__main__':
#多少人玩游戏，直接加个名字
    people = {
        "叶某":[],
        "建华":[],
        "小马":[],
        "坤哥":[],
        "走召":[],
    }
    #发牌
    result = how_many(len(people))
    #把发出来的牌分到玩家手上
    a = 0
    for i in people.keys():
        people[f'{i}'] = result[a:a+3]
        a += 3
    #把最终结果打出来，按照倒序排列
    for k,i in people.items():
    #把所有的顺子做成一个表
        shun = ['234','243','423','432','324','342,',
                '345','354','453','435','543','534',
                '456','465','564','546','654','645',
                '567','576','675','657','765','756',
                '678','687','786','768','876','867',
                '789','798','897','879','987','978',
                '8910','8109','9108','9810','1098','1089',
                '910J','9J10','10J9','109J','J910','J109',
                '10JQ','10QJ','J10Q','JQ10','QJ10','Q10J',
                'JQK','JKQ','QKJ','QJK','KJQ','KQJ',
                'QKA','QAK','KAQ','KQA','AKQ','AQK']
        result = sorted(i, key=lambda x: x[1], reverse=True)
        shun_res = result[0][1] + result[1][1] + result[2][1]
        if result[0][1] == result[1][1] == result [2][1]:
            print(f"{k} 豹子：",result)
            continue
        if result[0][0] == result[1][0] == result [2][0]:
            print(f"{k} 金花：",result)
            continue
        if result[0][1] == result[1][1] or result [0][1] == result[2][1] or result[1][1] == result[2][1]:
            print(f"{k} 对子：",result)
            continue
        if shun_res in shun and result[0][0] == result[1][0] == result [2][0]:
            print(f"{k} 同花顺：", result)
            continue
        if shun_res in shun:
            print(f"{k} 顺子：", result)
            continue
        else:
            print(k,result)