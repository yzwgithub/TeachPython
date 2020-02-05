import tkinter

# 计算器的定义


class CalGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('简单计算器')
        self.window.geometry('300x200')
        fm1 = tkinter.Frame(self.window)

        e1 = tkinter.Entry(fm1)
        e2 = tkinter.Entry(fm1)
        e1.grid(row=0, column=0)
        e2.grid(row=1, column=0)
        fm1.pack(side='top')

        fm2 = tkinter.Frame(self.window)
        button_C = tkinter.Button(fm2, width=8, text='C')
        button_C.grid(row=1, column=0, columnspan=2)
        button_Z = tkinter.Button(fm2, width=4, text='%')
        button_Z.grid(row=1, column=2)
        button_D = tkinter.Button(fm2, width=4, text='/')
        button_D.grid(row=1, column=3)
        button_7 = tkinter.Button(fm2, width=3, text='7')
        button_7.grid(row=2, column=0)
        button_8 = tkinter.Button(fm2, width=3, text='8')
        button_8.grid(row=2, column=1)
        button_9 = tkinter.Button(fm2, width=3, text='9')
        button_9.grid(row=2, column=2)
        button_matrix = tkinter.Button(fm2, width=3, text='X')
        button_matrix.grid(row=2, column=3)

        button_4 = tkinter.Button(fm2, width=3, text='4')
        button_4.grid(row=3, column=0)
        button_5 = tkinter.Button(fm2, width=3, text='5')
        button_5.grid(row=3, column=1)
        button_6 = tkinter.Button(fm2, width=3, text='6')
        button_6.grid(row=3, column=2)
        button_difference = tkinter.Button(fm2, width=3, text='-')
        button_difference.grid(row=3, column=3)

        button_1 = tkinter.Button(fm2, width=3, text='1')
        button_1.grid(row=4, column=0)
        button_2 = tkinter.Button(fm2, width=3, text='2')
        button_2.grid(row=4, column=1)
        button_3 = tkinter.Button(fm2, width=3, text='3')
        button_3.grid(row=4, column=2)
        button_add = tkinter.Button(fm2, width=3, text='+')
        button_add.grid(row=4, column=3)

        button_0 = tkinter.Button(fm2, width=8, text='0')
        button_0.grid(row=5, column=0, columnspan=2)
        button_dot = tkinter.Button(fm2, width=4, text='.')
        button_dot.grid(row=5, column=2)
        button_result = tkinter.Button(fm2, width=4, text='=')
        button_result.grid(row=5, column=3)

        fm2.pack(side='bottom')

        self.window.mainloop()


CalGUI()
