from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
import time
import numpy as np

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print('data sgape:{0}, no. positive:{1}, no. negative:{2}'.format(X.shape,
                                                                  y[y==1].shape[0],
                                                                  y[y==0].shape[0]))
print(cancer.data[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=3)

model = LogisticRegression()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)

print('train_score:{0:.6f}, cv_score:{1:.6f}'.format(train_score, cv_score))

y_pre = model.predict(X_test)
y_pre_proba = model.predict_proba(X_test)

print('matchs:{0}/{1}'.format(np.equal(y_pre, y_test).shape[0], y_test.shape[0]))
print('y_pre:{}, \ny_pre_proba:{}'.format(y_pre, y_pre_proba))