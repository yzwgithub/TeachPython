import matplotlib.pyplot as plt
import matplotlib

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

label_list = ['2014', '2015', '2016', '2017']  # 横坐标刻度显示值
num_list1 = [26, 37, 13, 38]  # 纵坐标值1
num_list2 = [12, 30, 40, 20]  # 纵坐标值2
x = range(len(num_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
rects1 = plt.bar(x=x, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
rects2 = plt.bar(x=[i + 0.4 for i in x], height=num_list2, width=0.4, color='green', label="二部门")
plt.ylim(0, 50)  # y轴取值范围
plt.ylabel("数量")
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("年份")
plt.title("银海公司")
plt.legend()  # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height), ha="center", va="bottom")
plt.show()
