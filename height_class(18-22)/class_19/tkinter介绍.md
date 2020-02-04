# tkinter介绍
tkinter是图形用户界面的库，使用这个库，可以绘制一些简单的界面。
例如在本次课程中，我们将要制作出一个计算器。
## tkinter常用的组件
* Lable：标签
* Button：按钮
* Entry：输入框
* Text：文本框
* Checkbutton: 多选框
* Menu:菜单栏
* Radiobutton: 单选框
* Scrol lbar：滚动条

tkinter简单示例1

        import tkinter # 导入thinter模块
        
        root = tkinter.Tk() # 创建窗口对象
        '''
        循环体
        '''
        root.mainloop() # 进入消息循环

![avatar](D:\JetBrains\PythonDemo\TeachPython\img\class_19\class_19_img01.jpg)

tkinter简单示例2

        import tkinter # 导入thinter模块
  
        root = tkinter.Tk() # 创建窗口对象
        
        root.title("wuya") # 设置窗口标题
        root.geometry("300x200+10+20") # 设置窗口大小，用x连接表示窗口的宽和高，用+号表示为窗口的位置，位置原点以屏幕左上角为（0，0）
        lb = tkinter.Label(wuya, text = 'hello world!') # 添加一个lable，内容显示为hello world！
        lb.pack()
        
        root.mainloop() # 进入消息循环
        
Lable控件的使用

        import tkinter
        
        root = tkinter.Tk()
        root.title("wuya")
        root.geometry("300x200+10+20")
        lb = tkinter.Label(wuya,
                           text='这是Lable控件',
                           bg='red',
                           fg='green',
                           font=("微软雅黑",14),
                           width=16,
                           height='5',
                          wraplength=60,
                           justif='left',
                           anchor='n',)
        
        """
        第一个参数，表示lb在窗口wuya中显示的内容
        text，是文本显示的内容
        bg，背景色
        fg，字体颜色
        font，字体样式，字体大小
        width，显示的宽度
        height，显示的高度
        warlength，每行显示的宽度
        justif,换行后文本对齐方式
        anchor，lable显示的位置，可选参数n，s,w,e，分别指的是东南西北
        """
        
        lb.pack()
        
        root.mainloop()

