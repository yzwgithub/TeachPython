# 自定义一个算数运算,四舍五入
def calculate(a):
    b = a - int(a)
    if b >=0 and b <0.5:
        return a - b
    else:
        return a - b + 1


if __name__ == '__main__':
    a = calculate(2.3)
    print(a)
