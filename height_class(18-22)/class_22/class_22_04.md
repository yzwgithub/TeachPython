    # 如何获取标签中的属性:attrs
    # string，标签的值
    # <a href='http://book.zongheng.com/chapter/1060407/62723509.html'>第一章</a>
    import requests
    import bs4

    url = 'http://book.zongheng.com/showchapter/1060407.html'

    r = requests.get(url=url)
    list = r.text
    bs=bs4.BeautifulSoup(list, "html.parser")
    all_chapter = bs.select(".col-4")


    def request_html(url):    # 解析网页内容
        r = requests.get(url=url)
        text = r.text
        bs = bs4.BeautifulSoup(text, "html.parser")
        content = bs.select('.content')
        if len(content) > 0:     # 仅仅只有在这样的情况下，才能够进行存储
            list_p = content[0].find_all('p')
            for j in list_p:
                file = open('text/第' + str(chapter) + '章.txt', 'a+', encoding='utf-8')
                file.write(j.string)


    chapter = 1
    for i in all_chapter:
        url_capture = i.a.attrs['href']
        request_html(url_capture)
        chapter += 1
        print('第'+str(chapter)+'章已经下载')
