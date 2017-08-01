# -*- coding: utf-8 -*-

import requests
from lxml import etree

def addproxy():
    proxy = {
        'http': 'http://114.235.81.147:8118',
        'https':'http://117.78.51.231:3128'
    }
    url = "http://1212.ip138.com/ic.asp"
    req = requests.get(url,proxies=proxy,timeout=10)
    req.encoding = "gbk"
    tree = etree.HTML(req.text)
    print(tree.xpath('//body/center/text()')[0])

if __name__ == '__main__':
    addproxy()