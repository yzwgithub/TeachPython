import turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.left(180)
for i in range(10):
    turtle.left(5)
    turtle.forward(3)

for i in range(10):
    turtle.left(4)
    turtle.forward(3)

turtle.forward(100)

turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

turtle.left(90)
for i in range(10):
    turtle.right(5)
    turtle.forward(3)

for i in range(10):
    turtle.right(4)
    turtle.forward(3)

turtle.forward(100)
turtle.done()
