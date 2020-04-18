# 支持向量机
# 支持向量机它既可以通过直线来对数据进行划分，也可以通过曲线对数据进行划分
import matplotlib.pyplot as plt

# 构造一个圆形数据集
from sklearn.datasets.samples_generator import make_circles

# 导入模型
from sklearn import svm

# 构造一个数据集，其中有100个数据
data_X, data_y = make_circles(100, factor=.1, noise=.1)

# 将上面构造的数据绘制出来
plt.scatter(data_X[:, 0], data_X[:, 1], c=data_y, cmap='autumn')
plt.show()

# 构造模型
model = svm.SVC(kernel='linear')

# 对模型进行训练
model.fit(data_X, data_y)

# 对模型进行测试
score = model.score(data_X, data_y)
print(score)
