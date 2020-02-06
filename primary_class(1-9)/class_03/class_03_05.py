# 使用for循环绘制一些复杂图形
# 案例一
# import turtle
#
# turtle.speed(15)
# for i in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# turtle.done()


# 案例二
import turtle

turtle.speed(15)
for j in range(36):
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.left(10)
turtle.done()
