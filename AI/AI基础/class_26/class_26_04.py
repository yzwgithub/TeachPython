        # scikit-learn
        # 它是一个机器学习工具包
        import pandas as pd
        import matplotlib.pyplot as plt
        from sklearn import datasets
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        # 预测波士顿的房价
        # 房价与那些因素有关
        # 第一步，获取数据集
        data = datasets.load_boston()     # 美国波士顿地区的房价

        data_df = pd.DataFrame(data['data'], columns=data['feature_names'])

        # 第二步，对数据进行简单的分析，进行数据可视化：目的是找出与问题相关的特征
        # 找出与房价有关系的特征：大小， 地理位置，
        # count = 1
        # for i in data['feature_names']:
        #     plt.subplot(2, 7, count)
        #     plt.plot(data_df[i])
        #     count += 1
        # plt.show()

        # 第三步，提取相关的特征
        data_df_feature = pd.DataFrame()
        data_df_feature['CRIM'] = data_df['CRIM']
        data_df_feature['INDUS'] = data_df['INDUS']

        # 第四步，划分数据集，训练集，测试集
        # print(data_df_feature)
        X_train, X_test, y_train, y_test = train_test_split(data_df_feature, data.target, test_size=0.2)

        # 第五步，构建机器学习模型
        model = LinearRegression()      # 最简单的线性回归模型

        # 第六步，对模型进行训练
        model.fit(X_train, y_train)    # 喂

        # 第七步模型测试
        score = model.score(X_test, y_test)
        print(score)
