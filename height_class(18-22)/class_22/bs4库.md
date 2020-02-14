# bs4库介绍
# 简介

BeautifulSoup 是一个从HTML或XML文件中提取数据的Python解析库，
使用方式简单方便，借助网页的结构和属性等特性来解析网页。
## 4个对象

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,
每个节点都是Python对象,所有对象可以归纳为4种: Tag , 
NavigableString , BeautifulSoup , Comment。
1. Tag对象

tag中最重要的属性: name和attributes。

2. NavigableString对象

3. BeautifulSoup对象

4. Comment对象

## 四种解析器

<table>
    <tr>
        <th>解析器</th>
        <th>使用方法</th>
        <th>优势</th>
        <th>劣势</th>
    </tr>
    <tr>
       <td>Python标准库</td> 
       <td>BeautifulSoup(markup, "html.parser")</td> 
       <td>
            *Python的内置标准库
            *执行速度适中
            *文档容错能力强
       </td> 
       <td>&emsp;&emsp; Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差</td> 
    </tr>
    <tr>
       <td>lxml HTML 解析器</td> 
       <td>BeautifulSoup(markup, "lxml")</td> 
       <td>
            *速度快
            *文档容错能力强
       </td> 
       <td>&emsp;&emsp; 需要安装C语言库</td> 
    </tr>
    <tr>
       <td>lxml XML 解析器</td> 
       <td>BeautifulSoup(markup, "xml")</td> 
       <td>
            *速度快
            *唯一支持XML的解析器
       </td> 
       <td>&emsp;&emsp; 需要安装C语言库</td> 
    </tr>
    <tr>
       <td>html5lib</td> 
       <td>BeautifulSoup(markup, "html5lib")</td> 
       <td>
            *最好的容错性
            *以浏览器的方式解析文档
            *生成HTML5格式的文档
       </td> 
       <td>
            *速度慢
            *不依赖外部扩展
       </td> 
    </tr>
</table>

## 常用方法



# [中文参考文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#)
