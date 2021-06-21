# 关于数据清洗
# 科学计算
# numpy，pandas
# matplotlib   数据可视化

import numpy as np

# numpy与列表非常相似，但是它功能上要比列表要强大得多

# 创建一个numpy数据
# 既可以传入一个列表，也可以是一个元组
# 方式一
a = np.array([1, 2, 3, 4])
b = np.array(('a', 'b', 'c', 'd'))
# 方式二
a = np.linspace(1, 100, 100)
b = np.logspace(1, 100, 5)    # 不是很常用

# 第三种方式
a = np.ones((100, )) * 100
b = np.zeros((100, ))

# 第四种
a = np.arange(1, 100, 2)     # 开始， 结束， 步长step

for i in range(1, 100, 2):
    print(i, end=' ')



