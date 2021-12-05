import random
import turtle as t

 # 树的主体
def tree(branchLen):
    if branchLen > 3:
        if branchLen < 8:     # 最短的树枝部分
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')   # 珊瑚色
            t.pensize(branchLen / 2)
        elif 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 3)
        else:  # 表示树干部分 >12
            t.color('sienna')  # 赭色
            t.pensize(branchLen / 10)

        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20*a)
        b = 1.5 * random.random()
        tree(branchLen-10*b)  # 递归 树枝变细
        t.left(40*a)
        tree(branchLen-10*b)
        t.right(20*a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m):  # 树下花瓣
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color("lightcoral")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def main():
    t.getscreen().tracer(5, 0)
    t.screensize(bg='wheat')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60)
    petal(100)
    t.ht()
    t.exitonclick()


main()
