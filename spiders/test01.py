# -*- coding: utf-8 -*-
import requests

url = 'https://95o9.com/'

html = requests.get(url).text
print(html)