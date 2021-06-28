# pandas 用法总结
## 1.基础操作
### 1.1 创建
##### 1.1.1 通过列表或者元组创建
        pd.Series([1, 2, 3])  ## 列表
        pd.Series((1, 2, 3))  # 元组
##### 1.1.2 通过字典创建
        dictionary = {'a':[1, 2, 3], 'b':[4, 5, 6]}
        pd.DataFramr(dictionary)
##### 1.1.3 从文件（csv,txt）
        pd.read_csv()   # 读取
        data.to_csv()     # 保存
### 1.2 查看数据
#### 1.2.1 查看前n行
        data.head()    # 查看data的前n行
####1.2.2 查看后n行
        data.tail()    # 查看data的后n行
####1.2.3 检测是否有空值
        data.isnan()
        data.isnull()
#### 1.2.4  对空值进行处理
        data.fillna()               #对空值进行填充
        data = data.dropna()        # 删除空值
### 1.3 索引和切片
#### 1.3.1 索引
        ## 作用是获取指定的行或列
        data[0]             # 获取第0行
        data['column_1']    # 获取列名为‘column_1’的列
####1.3.2 切片
        ## 作用是获取指定的多行
        data[:100]          # 获取data的前100行
## 2比较重要的操作

### 2.1 loc和iloc
        data = data.loc[:10, ['a', 'b']]      # 第二个参数是列的名称
        data = data.loc[:10, ['a', 'b']]      # 第二个参数是列的名称
### 2.2 boolean 索引
        data = data[data <= 100]              # 获取所有data<=100的值
### 2.3 计数
        data.value_counts()          # 统计每一个值出现的频率

## 3高级用法
### 3.1 where的使用
        data = data.where(data < 3, 4)       # 按照所给条件的反面进行替换
        data = data.mask(data < 3, 4)        # 根据所给条件进行替换
###3.2 apply的使用
        # 它可以用lambda表达式对data中的每一个元素进行操作
        data = data.apply(lambda x: x + 5 if x > 3 else x * 6)
        data = data.apply(lambda x: x**2 if x < 3 else np.sqrt(x))
### 3.3 多个Series和DataFrame的合并
        # concat
        data = pd.concat([data, data_01], axis=1)    # 按列合并
        data = pd.concat([data, data_01], axis=0)    # 按行合并
### 3.4 groupby
####3.4.1 agg的用法
        # 求平均成绩
        # class_num  , stu_id, score
        import numpy as np
        import pandas as pd
        data = {'class_num': [1, 1, 1, 2, 2, 2, 3, 3, 3],
                'stu_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'score': [80, 76, 54, 92, 86, 75, 83, 91, 46]}

        data = pd.DataFrame(data)
        # 分组
        data_group = data.groupby('class_num').agg({'score': 'max'})
        # 求平均值
        # max, min, mean, sun
        # data_mean = data_group.agg({'score': 'max'})
        print(data_group)
####3.4.2 transform的用法
        # transform
        import numpy as np

        import pandas as pd
        data = {'class_num': [1, 1, 1, 2, 2, 2, 3, 3, 3],
                'stu_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'score': [80, 76, 54, 92, 86, 75, 83, 91, 46]}

        data = pd.DataFrame(data)
        # 分组
        data_group = data.groupby('class_num')
        data['mean'] = data_group['score'].transform('mean')
        print(data)
