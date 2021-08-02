# 面向对象实例：对学生信息进行增、删、改
class Student:

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setSex(self,sex):
        self.sex = sex

    def setClass(self, class_num):
        self.class_num = class_num

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getClass(self):
        return self.class_num
