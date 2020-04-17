# 决策树
# 分类树，回归树
# 分类：逻辑回归、朴素贝叶斯分类器、决策树
# 回归：线性回归、决策树
# 支持向量机，用来做分类任务的一种机器学习方法

# 用来进行数据处理的库
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 导入模型(支持向量机)
from sklearn import svm

# 数据可视化的库
import matplotlib.pyplot as plt

# 加载数据(鸢尾花)
data = load_iris()

# 对数据进行处理
data_feature = data.data
data_target = data.target

feature_train, feature_test, target_train, target_test = train_test_split(
    data_feature, data_target, test_size=0.32)

# 散点图
np_feature = np.array(data_feature)
np_target = np.array(data_target)
plt.scatter(np_feature[:, :1], np_target)
plt.show()

# 构建模型
model = svm.SVC()

# 训练模型
model.fit(feature_train, target_train)

# 模型评价
score = model.score(feature_test, target_test)
print(score)
