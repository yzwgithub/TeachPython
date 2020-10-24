import requests
import bs4

# 小说的目录页
link_url = 'http://book.zongheng.com/showchapter/1060407.html'

link = requests.get(link_url)

text = link.text

bs =bs4.BeautifulSoup(text, 'html.parser')

ul = bs.find_all('ul')          # 找出所有的’ul‘标签
a = ul[-1].find_all('a')        # 找出所有的’a‘标签
count = 0
for i in a:

    captures = i.attrs['href']     # 得到每一个章节的链接
    link = requests.get(captures)
    text = link.text
    bs = bs4.BeautifulSoup(text, 'html.parser')
    p = bs.find_all('p')
    file = open(str(count) + '.txt', 'w+', encoding='utf-8')
    for j in p:
        file.write(j.string + '\n')
    count = count + 1
