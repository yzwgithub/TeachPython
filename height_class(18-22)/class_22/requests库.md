# requests库介绍
## 简介

requests是python中用来模拟网络请求的库，常用作网络爬虫，爬取网络中的各种数据。
例如，通过get()方法，获取到百度首页。

    import requests
    response = requests.get('https://www.baidu.com')
    print(response)
 
## HTTP请求介绍


## 常用方法
1. request()

构造一个请求，支持以下2-7各种方法的基础方法。返回的是一个Response对象

2. get()

获得HTML网页的主要信息，对应于HTTP的GET。返回的是一个Response对象
3. head()

获取HTML网页的头信息，对应于HTTP的HEAD。返回的是一个Response对象
4. post()

向HTML网页提交POST请求，对应于HTTP的POST。返回的是一个Response对象
5. put()

向HTML网页提交PUT请求，对应于HTTP的PUT。返回的是一个Response对象
6. patch()

向HTML网页提交局部修改请求，对应于HTTP的PATCH。返回的是一个Response对象
7. delete()

向HTML网页提交删除请求，对应于HTTP的DELETE。返回的是一个Response对象
## 常用属性
1. status_code

HTTP请求的返回状态，200表示连接成功，404表示 失败

2. text

HTTP响应内容的字符串形式
3. encoding

从HTTP  header中猜测的响应内容编码方式
4. apparent_encoding

从内容中分析出的响应内容编码方式（备选编码方式）
5. content

HTTP响应内容的二进制形式

## [requests库中文参考文档](http://2.python-requests.org/zh_CN/latest/user/quickstart.html)