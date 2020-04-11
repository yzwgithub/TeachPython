# 波士顿房价的预测
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = load_boston()
x_data = dataset.data # 导入所有特征变量
y_data = dataset.target # 导入目标值（房价）
name_data = dataset.feature_names #导入特征名
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)

lr = linear_model.LinearRegression()
train = lr.fit(X_train, y_train)

score = train.score(X_test, y_test)
print(score)
