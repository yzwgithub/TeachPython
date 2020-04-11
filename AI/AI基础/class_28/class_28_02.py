from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def nb_20newsgroups():
    """
    Naive bayes demo
    :return:
    """
    #1 获取数据
    news = fetch_20newsgroups(subset="all")

    #2 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size=0.2,random_state=21)

    #3 特征工程，文本特征抽取-TF-IDF
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    #4 朴素贝叶斯算法预估器
    estimator = MultinomialNB()
    estimator.fit(x_train,y_train)

    #5 模型评估
    y_predict = estimator.predict(x_test)
    print("y_predict:",y_predict)
    print("预测值是否正确：",y_test == y_predict)

    score = estimator.score(x_test,y_test)
    print("准确率：",score)

    return None


if __name__ == "__main__":
    nb_20newsgroups()
