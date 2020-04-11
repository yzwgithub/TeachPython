#coding=utf-8
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#原始数据
news = datasets.fetch_20newsgroups(subset="all")
X = news.data
y = news.target
print(X[:5])
print(y[:5])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25)
#使用tf
tf = TfidfVectorizer()
X_train =tf.fit_transform(X_train)
X_test = tf.transform(X_test)

print(X_train[0:5])
print(tf.get_feature_names()[8000:8020])#打印部分分词特征名

#构建朴素贝叶斯模型
mlt = MultinomialNB(alpha=1.0)#alpha拉普拉斯平滑系数，防止概率为0出现
mlt.fit(X_train,y_train)

#结果预测与评分
y_predict = mlt.predict(X_test)
print("预测结果：",y_predict[0:10])
print("实际结果：",y_test[0:10])

#评分
print("准确度：",mlt.score(X_test,y_test))
