# numpy有哪些特点

# shape   形状
# dtype   类型(整数、浮点数、字符串)
# ndim    维数

# reshape()  调整np的shape
# astype()   调整np的类型

import numpy as np
a = np.arange(0, 100)
b = np.arange(0, 100) * 3
# 数乘
# print(a * 3)
# 加法
# print(a + b)

# 索引和切片
print(a[1: 10])
