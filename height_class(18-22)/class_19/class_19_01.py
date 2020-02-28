# tkinter库
import tkinter
root = tkinter.Tk()

root.geometry('800x600')
root.title('图形用户界面')
# 文本框
label = tkinter.Label(text='昔人已乘黄鹤去， 此地空余黄鹤楼')
label.pack()
# 可输入的文本框
entry = tkinter.Entry(width=30)
entry.pack()
# 多行文本框
text = tkinter.Text(width=100, height=30)
text.pack()
# 按钮
button = tkinter.Button(text='提交')
button.pack()
# 复选框
ckeckbutton1 = tkinter.Checkbutton(text='A')
ckeckbutton1.pack()
ckeckbutton2 = tkinter.Checkbutton(text='B')
ckeckbutton2.pack()
ckeckbutton3 = tkinter.Checkbutton(text='C')
ckeckbutton3.pack()
ckeckbutton4 = tkinter.Checkbutton(text='D')
ckeckbutton4.pack()
# 单选框
radioButton = tkinter.Radiobutton(text='A')
radioButton.pack()
root.mainloop()

