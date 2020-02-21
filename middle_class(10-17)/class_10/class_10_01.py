# 自定义函数
# 是python中极具创造性的一部分内容

import turtle


def rect(x, y):         # 画正方形
    for i in range(x):
        turtle.forward(y)
        turtle.left(360 / x)


def move(x, y):         # 移动画笔
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def house():            # 绘制正屋
    move(-200, -300)
    rect(4, 400)


def house_top():        # 绘制屋顶
    turtle.goto(-200, 100)
    turtle.goto(0, 200)
    turtle.goto(200, 100)


def house_dor():        # 绘制门
    move(-50, -300)
    rect(4, 100)


if __name__ == '__main__':
    house()
    house_top()
    house_dor()
    turtle.done()
