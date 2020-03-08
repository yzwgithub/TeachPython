# 自定义方法
# 面向对象：将一类方法放到一起，形成的
import turtle

class House:

    def angle(self, length, n):
        for i in range(n):
            turtle.forward(length)
            turtle.left(360 / n)

    def move(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    def house(self):
        self.move(-200, -300)
        self.angle(400, 4)


    def house_top(self):
        turtle.goto(-200, 100)
        turtle.goto(0, 250)
        turtle.goto(200, 100)

    def house_dor(self):
        self.move(-50, -300)
        self.angle(100, 4)


    def house_window_01(self):
        self.move(-120, -100)
        self.angle(50, 4)

    def house_window_02(self):
        self.move(120, -100)
        self.angle(50, 4)

if __name__ == '__main__':
    house = House()
    house.house()
    house.house_top()
    house.house_dor()
    house.house_window_01()
    house.house_window_02()
    turtle.done()

