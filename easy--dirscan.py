# use  sys- requests module

#coding:utf-8

import sys
reload(sys)
#sys.setDefaultencoding('utf-8')
import requests


#url = 'http://192.168.10.23/'
headers = {
    'Accept': '*/*',
    'Referer': 'http://wwww.baidu.com',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
    'Cache-Control': 'no-cache',
}
url = sys.argv[1]  #传递第一个参数，要扫描的url地址
#dict='dict.txt'
dict = sys.argv[2] #传递第二个参数，要扫描的字典文件

with open(dict, 'r') as s:  #打开字典文件，由第二哥参数传入，‘r'只读模式
    for i in s.readlines():   #把字典循环进 i
        i = i.strip()  # strip去除换行
        c = requests.get(url=url+i, headers=headers, timeout=30, allow_redirects=False)
        print '%s' % c.url
        if c.status_code != 200:
            #paass
            print '"%s" + not' % c.url
        else:
            print '"%s" + yes' % c.url
            

