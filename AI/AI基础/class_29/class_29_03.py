from sklearn import tree
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import graphviz

data = load_boston()

boston_data = data.data
boston_target = data.target

feature_train, feature_test, target_train, target_test = train_test_split(boston_data, boston_target, test_size=0.31, random_state=50)

model = tree.DecisionTreeRegressor()

model.fit(feature_train, target_train)

score = model.score(feature_test, target_test)

print(score)
