# 写一个方法，打印出九九乘法表


def matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print("%d * %d = %d" % (i, j, (i * j)), end='   ')
        print("\n")


if __name__ == "__main__":
    matrix()

