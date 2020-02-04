
import tkinter as tk

# 界面类
class CalGui:

    def __init__(self, cal_logic):

        self.cal_logic = cal_logic

        self.win = tk.Tk()
        self.win.title('简单计算器')
        fm1 = tk.Frame(self.win)

        self.var_e1 = tk.StringVar()
        self.var_e2 = tk.StringVar()
        e1 = tk.Entry(fm1, textvariable=self.var_e1)
        e2 = tk.Entry(fm1, textvariable=self.var_e2)
        e1.grid(row=0, column=0, columnspan=10)
        e2.grid(row=1, column=0, columnspan=10)
        fm1.pack(side='top')

        fm2 = tk.Frame(self.win)
        tk.Button(fm2, text='C', width=8, command=self.clear).grid(row=1, column=0, columnspan=2)
        tk.Button(fm2, text='%', width = 4,command=lambda :self.getText('%')).grid(row=1, column=2)
        tk.Button(fm2, text='/', width = 4,command=lambda :self.getText('/')).grid(row=1, column=3)
        tk.Button(fm2, text='7', width = 3, command=lambda :self.getText('7')).grid(row=2, column=0)
        tk.Button(fm2, text='8', width = 3, command=lambda :self.getText('8')).grid(row=2, column=1)
        tk.Button(fm2, text='9', width = 3, command=lambda :self.getText('9')).grid(row=2, column=2)
        tk.Button(fm2, text='X', width = 3,command=lambda :self.getText('*')).grid(row=2, column=3)
        tk.Button(fm2, text='4', width = 3,command=lambda :self.getText('4')).grid(row=3, column=0)
        tk.Button(fm2, text='5', width = 3,command=lambda :self.getText('5')).grid(row=3, column=1)
        tk.Button(fm2, text='6', width = 3,command=lambda :self.getText('6')).grid(row=3, column=2)
        tk.Button(fm2, text='-', width = 3,command=lambda :self.getText('-')).grid(row=3, column=3)
        tk.Button(fm2, text='1', width = 3,command=lambda :self.getText('1')).grid(row=4, column=0)
        tk.Button(fm2, text='2', width = 3,command=lambda :self.getText('2')).grid(row=4, column=1)
        tk.Button(fm2, text='3', width = 3,command=lambda :self.getText('3')).grid(row=4, column=2)
        tk.Button(fm2, text='+', width = 3,command=lambda :self.getText('+')).grid(row=4, column=3)
        tk.Button(fm2, text='0', width=8,command=lambda :self.getText('0')).grid(row=5, column=0, columnspan=2)
        tk.Button(fm2, text='.', width=4,command=lambda :self.getText('.')).grid(row=5, column=2)
        tk.Button(fm2, text='=', width=4, command=self.getResult).grid(row=5, column=3)
        fm2.pack(side='bottom')

        self.win.mainloop()

    def getText(self, c):
        content = self.var_e1.get()
        if content == '':
            self.var_e1.set(c)
        else:
           content = content + c
           self.var_e1.set(content)

    def getResult(self):
        self.cal_logic.showText = self.var_e1.get()
        result = self.cal_logic.cal_result()
        self.var_e2.set(result)

    def clear(self):
        self.var_e1.set('')
        self.var_e2.set('')

class CalLogic:

    def __init__(self):
        self.showText = ''
        self.showResult = ''

    # 处理计算的函数
    def cal_result(self):
        self.showResult = eval(self.showText)
        return self.showResult

def main():

    cal_logic = CalLogic()
    CalGui(cal_logic)


if __name__ == '__main__':
    main()
