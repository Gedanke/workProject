# -*- coding:utf-8 -*-

import re
import csv

import requests

url = 'http://yss.mof.gov.cn/2019qgczjs/202007/t20200706_3544615.htm'
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

content = response.text

"""
<p align="justify">　　（2）中央政府国外债务发行费用支出预算数为0.52亿元，决算数为0.52亿元，完成预算的100%。</p>
"""
match_pattern = '<p align="justify">(.*?)</p>'

results = re.findall(match_pattern, str(content), re.S)

for result in results:
    print(result)
