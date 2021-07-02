# 使用skleaen拟合一个函数
# y = x **2
import numpy as np
import random
import matplotlib.pyplot as plt
# 构造数据集
x = np.arange(1, 1000)
noise = x / 1000
y = x**2 + noise

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x[:800], y[:800])
# y_p = model.predict(x[800:])     # 预测

score = model.score(x[800:].reshape((-1, 1)), y[800:].reshape((-1, 1)))

print(score)

