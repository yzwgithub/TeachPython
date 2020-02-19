import requests
import bs4

response = requests.get('https://www.baidu.com')

html_str = response.content
file = open('a.txt', 'a', encoding='utf-8')
file.write(str(html_str))

