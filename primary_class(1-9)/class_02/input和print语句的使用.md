# input和print语句的使用
## input语句的使用

input语句，意思是从键盘输入。

    a = input()
    b = input('请从键盘输入：')

## print语句的使用
print语句，意思是将内容打印在控制台上。

    print('hello word!')       # 普通输出
    print(1, 2, 3)             # 同时输出多个值
    print(1, 2, 3, sep=':')    # 输出多个值，并改变分隔符，常用的分隔符有

print格式化输出
    
    print("%d" % (10))                   # 输出数字
    print("%.4f" % (3.1415926))          # 输出数字，保留四位小数
    print("%s" % ('Hello World!'))       # 输出字符串
    print("%50s" % ('Hello World!'))     # 输出字符串，取50个字符的空位
    
print常见的输出格式
1. %s 字符串

2. %r 字符串

3. %c 单个字符

4. %b 二进制整数

5. %d 十进制整数

6. %i 十进制整数

7. %o 八进制整数

8. %x 十六进制整数

9. %e 指数 (基底为小写e)

10. %E 指数 (基底写为大写E)

11. %f 浮点数

12. %F 浮点数，与上相同

13. %g 指数(e)或浮点数 (根据显示长度)

14. %G 指数(E)或浮点数 (根据显示长度)

format()方法的使用<br>
该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’
    
1. 不带编号，“{}”
2. 带数字编号，可调换顺序，“{1}”、“{2}”
3. 带关键字，即“{a}”、“{b}”


    print('{} {}'.format('deuterium', 'suika'))
    print('{0} {1}'.format('deuterium', 'suika'))  # 带数字编号
    print('{0} {1} {0}'.format('deuterium', 'suika'))  # 打乱顺序
    print('{1} {1} {0}'.format('deuterium', 'suika'))
    print('{a} {b} {a}'.format(a='deuterium', b='suika'))  # 带关键字
    