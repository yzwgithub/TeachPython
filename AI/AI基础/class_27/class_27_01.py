# -*- coding: utf-8 -*-

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False

iris=load_iris()
iris_data=iris.data
iris_target=iris.target

print(iris_data.shape)

pca=PCA(n_components=2)

X=pca.fit_transform(iris_data)
print(X.shape)

f=plt.figure()
ax=f.add_subplot(111)
ax.plot(X[:,0][iris_target==0],X[:,1][iris_target==0],'bo')
ax.scatter(X[:,0][iris_target==1],X[:,1][iris_target==1],c='r')
ax.scatter(X[:,0][iris_target==2],X[:,1][iris_target==2],c='y')
ax.set_title('数据分布图')
plt.show()

clf=LogisticRegression(multi_class='ovr',solver='lbfgs',class_weight={0:1,1:1,2:1})
clf.fit(X,iris_target)
score=clf.score(X,iris_target)

x0min,x0max=X[:,0].min(),X[:,0].max()
x1min,x1max=X[:,1].min(),X[:,1].max()
h=0.05
xx,yy=np.meshgrid(np.arange(x0min-1,x0max+1,h),np.arange(x1min-1,x1max+1,h))
x_=xx.reshape([xx.shape[0]*xx.shape[1],1])
y_=yy.reshape([yy.shape[0]*yy.shape[1],1])
test_x=np.c_[x_,y_]

test_predict=clf.predict(test_x)
z=test_predict.reshape(xx.shape)
plt.contourf(xx,yy,z, cmap=plt.cm.Paired)
plt.axis('tight')
colors='bry'
for i,color in zip(clf.classes_,colors):
    idx=np.where(iris_target==i)
    plt.scatter(X[idx,0],X[idx,1],c=color,cmap=plt.cm.Paired)

xmin,xmax=plt.xlim()
coef=clf.coef_
intercept=clf.intercept_
def line(c,x0):
    return (-coef[c,0]*x0-intercept[c])/coef[c,1]
for i,color in zip(clf.classes_,colors):
    plt.plot([xmin,xmax],[line(i,xmin),line(i,xmax)],color=color,linestyle='--')
plt.title("score:{0}".format(score))