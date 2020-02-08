# turtle库的使用
## turtle常用函数
1. 画笔属性函数
- turtle.speed(speed)   # 设置画笔运动速度
- turtle.pensize(width) # 设置画笔粗细
- turtle.pencolor()     # 设置画笔颜色
- turtle.hideturtle()   # 隐藏箭头显示
- turtle.showturtle()   # 显示箭头  

2. 画笔控制函数
- turtle.forward(distance)          # 前进
- turtle.backward(distance)         # 后退
- turtle.right(degree)              # 顺时针旋转
- turtle.left(degree)               # 逆时针旋转
- turtle.seth(to_angle)             # 设置画笔的方向
- turtle.pendown()                  # 将画笔落到画纸上
- turtle.goto(x,y)                  # 移动画笔
- turtle.penup()                    # 抬起画笔
- turtle.circle(raduis, extent，steps)            # 绘制一个圆

3. 颜色填充函数
- turtle.fillcolor(colorstring)              # 填充颜色
- turtle.begin_fill()                        # 开始填充
- turtle.end_fill()                          # 结束填充
- turtle.filling()                           # 判断是否为填充状态

4. 全局控制函数
- turtle.clear()	     # 清空turtle窗口，但是turtle的位置和状态不会改变
- turtle.reset()	     # 清空窗口，重置turtle状态为起始状态
- turtle.undo()	       # 撤销上一个turtle动作
- turtle.isvisible()	 # 返回当前turtle是否可见
- turtle.write(s[,font=(“font-name”,font_size,“font_type”)])	        # 显示文字
## 代码示例
1. [绘制一个三角形](../class_03/class_03_01.py)
2. [绘制一个正方形](../class_03/class_03_02.py)
3. [绘制任意多边形](../class_03/class_03_04.py)
4. [小猪佩奇](../class_03/class_03_06.py)
5. [绘制一个小房子](../class_03/class_03_07.py)
