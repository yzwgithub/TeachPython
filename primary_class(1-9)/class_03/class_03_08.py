# 关于颜色填充的

import turtle

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(200)
turtle.goto(150, 100)
turtle.goto(-50, 100)
turtle.goto(0, 150)
turtle.end_fill()


turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()

turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(-50, 100)
turtle.goto(-50, -100)
turtle.goto(150, -100)
turtle.goto(150, 100)
turtle.end_fill()

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.goto(150, -100)
turtle.goto(200, -50)
turtle.goto(200, 150)
turtle.end_fill()

turtle.penup()
turtle.goto()
turtle.done()
