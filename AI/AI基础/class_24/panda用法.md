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
        data.fillna()    #对空值进行填充
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
        
