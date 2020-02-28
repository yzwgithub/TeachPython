# 登陆注册页面

import tkinter
root = tkinter.Tk()
root.geometry('300x200')
fm = tkinter.Frame(root)
label1 = tkinter.Label(fm, text='用户名')
label1.grid(row=0, column=0)

entry1 = tkinter.Entry(fm, width=20)
entry1.grid(row=0, column=1)

label2 = tkinter.Label(fm, text='密  码')
label2.grid(row=1, column=0)

entry2 = tkinter.Entry(fm, width=20)
entry2.grid(row=1, column=1)

button = tkinter.Button(fm, text='登 陆', width=15)
button.grid(row=2, column=0, columnspan=2)

fm.pack()
root.mainloop()
