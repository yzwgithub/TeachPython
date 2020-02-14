import requests
import bs4

# 向服务器发送get请求
response = requests.get('http://seputu.com/biji1/1.html')

# 获取HTML文档
html_str = response.content

# 将HTML文档转换成BeautifulSoup对象
soup = bs4.BeautifulSoup(html_str, 'html.parser')

# 获取小说标题
title = soup.title.string
# 获取第一章的题目
title_01 = soup.strong.string

# 获取小说正文
content = soup.select('.content-body')
content = content[0]
content = content.find_all(name='p')

for i in content:
    if i.string != None:
        print(i.string)
