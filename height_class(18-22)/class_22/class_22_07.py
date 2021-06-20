# 对小说内容页进行解析
import requests
import bs4


def get_content(title, content_url):
    r = requests.get(content_url)
    bs = bs4.BeautifulSoup(r.text, 'html.parser')
    content = bs.select('.content')
    if len(content) > 0:
        list_p = content[0].find_all('p')
        for i in list_p:
            save_content(title, i.string)


def save_content(title, content):
    file = open(title, 'a+')
    file.write(content)
