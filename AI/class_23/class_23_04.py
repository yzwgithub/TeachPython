# 导入绘图模块
import matplotlib.pyplot as plt

# 构建数据
GDP = [12406.8, 13908.57, 9386.87, 9143.64]
# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.barh(range(4), GDP, align='center', color='orange', alpha=0.5)
# 添加轴标签
plt.xlabel('GDP')
# 添加标题
plt.title('直辖市GDP对比')
# 添加刻度标签
plt.yticks(range(4), ['北京市', '上海市', '天津市', '重庆市'])
# 设置Y轴的刻度范围
plt.xlim([5000, 17000])
# 为每个条形图添加数值标签
for x, y in enumerate(GDP):
    plt.text(y + 100, x, '%s' % y, va='center')
# 显示图形
plt.show()