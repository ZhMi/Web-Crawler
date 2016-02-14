# -*- coding: utf-8 -*-

# file description : test beautiful soup4 part
# author : zhmi
# mail : zhmi120@sina.com

from __future__ import unicode_literals
from bs4 import BeautifulSoup

import re
# 根据HTML网页字符串创建BeautifulSoup对象
html_doc = """
           '<html><head><title>Page title</title></head>',
           '<a href = "http://example.com/lacie" class="sister" id="link2">Lacie</a>',
           '<a href = "http://example.com/title" class="sister" id="link3">title</a>',
           '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
           '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
           '</html>'
           """
soup = BeautifulSoup(
                    html_doc,                   # HTML文档字符串
                    "html.parser",              # HTML解析器
                    from_encoding = 'utf-8'     # HTML文档的编码
                    )

print '获取所有的链接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print "获取lacie的链接"
link_node = soup.find('a',href='http://example.com/lacie')
print link_node,link_node['href'],link_node.get_text()

print "正则匹配"
link_node = soup.find('a',href=re.compile(r"ac"))
print link_node.name,link_node['href'],link_node.get_text()

print "获取P段落文字"
p_node = soup.find('p',id="firstpara")
print p_node.name,p_node.get_text()
'''
# 搜索节点（find_all,find）

# 查找所有标签为a的节点
soup.find_all('a')

# 查找所有标签为a,连接符合/view/123.htm形式的节点
soup.find_all('a',href = '/view/123.htm')
soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))

# 查找所有标签为div,class为abc,文字为Python的节点
soup.find_all('div',class_ = 'abc',string = 'python')

# 访问节点信息
# 得到节点：<a href = '1.html'>Python</a>
# 获取查找到的节点的标签名称
node.name
# 获取查找到的a节点的href属性
node['href']
# 获取查找到的a节点的连接文字
node.get_text()
'''

