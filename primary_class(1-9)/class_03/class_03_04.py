# 绘制任意正多边形
import turtle
n = 3
length = 100

for i in range(n):
    turtle.forward(length)
    turtle.left(360 / n)
turtle.done()
