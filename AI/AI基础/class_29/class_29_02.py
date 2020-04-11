from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import graphviz

wine = load_wine()

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)

# clf = tree.DecesitionTreeClassifire
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
dot_data = tree.export_graphviz(clf,
                               feature_names=wine.feature_names,
                               class_names=['琴酒', '雪莉', '贝尔摩德'],
                               filled=True,
                               rounded=True)
graph = graphviz.Source(dot_data)

