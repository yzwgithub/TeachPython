# 向文件中写入内容，从文件读取内容
# 文件的复制
# a.txt, a文件中是一首诗，要将这首诗，复制到b中
# b.txt


def read(file_name):
    file = open(file_name + '.txt', 'r', encoding='utf-8')
    text = file.read()
    return text


def write(file_name, content):
    file = open(file_name+'.txt', 'a+')
    file.write(content)
    file.close()
