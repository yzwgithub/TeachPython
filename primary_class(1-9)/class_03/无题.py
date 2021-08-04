import turtle


def a():
    turtle.dot(500)


def b():
    turtle.pencolor('white')
    turtle.penup()
    turtle.goto(-50,-50)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.goto(0, -5)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(250)
    turtle.end_fill()
