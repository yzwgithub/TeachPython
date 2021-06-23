# pandas
# 有很多的功能与excel是一样的
# 如何创建一个pandas数据
# Series        一列
# DataFrame     多列
# 当创建Series或者DataFrame时，默认自动创建index
# 也可以自己指定index

# 通过元组或列表来创建
import pandas as pd
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 第二种， 通过字典创建
dict_s = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict_df = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
           'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
           'c': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
           'd': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, }
s = pd.Series(dict_s)
df = pd.DataFrame(dict_df)

# 第三种，从外部文件中读取：csv, txt
data = pd.read_csv('data.csv')
# print(data.info)      # information
print(data.values)

# pandas数据有哪些特性
# numpy：shape, dtype, ndim
# pandas:dtype, column, row, info
