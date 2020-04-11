import numpy as np
import pandas as pd
import graphviz
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
iris_data = iris.data
iris_target = iris.target
iris_target_name = iris.target_names

feature_train, feature_test, target_train, target_test = \
    train_test_split(iris_data, iris_target, test_size=0.33, random_state=42)
dt_model = DecisionTreeClassifier()
dt_model.fit(feature_train, target_train)
predict_results = dt_model.predict(feature_test)
scores = dt_model.score(feature_test, target_test)

dot_data = tree.export_graphviz(dt_model
                                ,feature_names=['item_1', 'item_2', 'item_3', 'item_4']
                                ,filled=True
                                ,rounded=True)
graph = graphviz.Source(dot_data)