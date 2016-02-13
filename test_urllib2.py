# -*- coding:utf8 -*-

from __future__ import unicode_literals # 解决控制台输出中文乱码问题

import urllib2
import cookielib
import sys

url = "http://www.baidu.com"

print "第一种方法"
response1 = urllib2.urlopen(url) # 发送请求
print response1.getcode() # 状态码
print len(response1.read()) # 内容的长度

print "第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0") # 将爬虫伪装成浏览器
response2 = urllib2.urlopen(url) # 发送请求
print response2.getcode()
print len(response2.read())

print "第三种方法"
# 增加cookie的处理
cj = cookielib.CookieJar()# 创建cookie的容器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener) # 此时urllib2 具有了cookie处理的增强能力

response3 = urllib2.urlopen(url) # 发送请求
print response3.getcode()
print cj # 打印cookie内容
web_content = response3.read() # 获取网页内容，网站页面是utf-8编码的。
type = sys.getfilesystemencoding()
print web_content.decode("UTF-8").encode(type)  # 解决中文乱码
