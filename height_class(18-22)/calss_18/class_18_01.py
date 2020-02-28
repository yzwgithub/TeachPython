# 使用类的方式，绘制一个房子
import turtle


# 类的定义
class House:

    def move(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    def angle(self, length):
        for i in range(4):
            turtle.forward(length)
            turtle.left(90)

    def house(self):
        self.move(-200, -300)
        self.angle(400)

    def houseTop(self):
        self.move(-200, 100)
        turtle.goto(0, 300)
        turtle.goto(200, 100)

    def houseDor(self):
        self.move(-50, -300)
        self.angle(100)


if __name__ == '__main__':
    house = House()       # 初始化对象
    house.house()
    house.houseTop()
    house.houseDor()
    turtle.done()


