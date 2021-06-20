# 爬虫
import requests
import bs4
import class_05_02
# 小说目录页
url = 'http://book.zongheng.com/showchapter/1060407.html'
r = requests.get(url=url)
text = r.text

# 对目录页进行解析，获取小说每一个章节的网址
bs = bs4.BeautifulSoup(text, 'html.parser')
list_chapter = bs.select('.col-4')    # 返回的是一个列表

chapter = 1
for i in list_chapter:
    a = i.a       # 结果,是一个标签a
    href = a.attrs     # 获取的是标签a的属性,类型是一个字典
    link_html = href['href']
    title = "data/第"+str(chapter)+"章.txt"
    class_05_02.get_content(title=title, content_url=link_html)
    chapter += 1
    print(title)


