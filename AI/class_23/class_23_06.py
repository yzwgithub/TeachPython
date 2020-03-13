import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ['2014', '2015', '2016', '2017']
num_list1 = [20, 30, 15, 35]
num_list2 = [15, 30, 40, 20]
x = range(len(num_list1))
rects1 = plt.bar(x=x, height=num_list1, width=0.45, alpha=0.8, color='red', label="一部门")
rects2 = plt.bar(x=x, height=num_list2, width=0.45, color='green', label="二部门", bottom=num_list1)
plt.ylim(0, 80)
plt.ylabel("数量")
plt.xticks(x, label_list)
plt.xlabel("年份")
plt.title("银海公司")
plt.legend()
plt.show()
