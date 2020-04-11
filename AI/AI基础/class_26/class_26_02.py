#coding:utf-8
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#x轴数据
x_data = np.arange(20)
#y轴数据
y_data = np.array([0.4, 0.8, 1.1, 2.1, 2.8, 2.7, 3.5, 4.6, 5.1, 4.5, 6.0, 5.5, 6.9, 6.8, 7.6, 8.0, 8.8, 8.5, 9.5, 9.3])
print(x_data)
print(y_data)

plt.scatter(x_data,y_data)
plt.xlabel("x_data")
plt.ylabel("y_data")
# plt.show()

#转一下维度，sklearn框架才能识别
x_data = x_data[:,np.newaxis]

y_data = y_data[:,np.newaxis]
print("*"*100)
print(x_data)
print(y_data)
#建立模型
model = LinearRegression()

#开始训练
model.fit(x_data,y_data)

#斜率
print("coefficients : ",model.coef_)
w = model.coef_[0]

#截距
print("intercept: ",model.intercept_)
b = model.intercept_

#测试
x_test = np.array([[7]])
predict = model.predict(x_test)
print("predict: ",predict)

#回归最终结果
plt.plot(x_data,(w*x_data + b),"b-")
plt.scatter(x_test,predict,color= 'r',marker = 'o')

plt.show()
