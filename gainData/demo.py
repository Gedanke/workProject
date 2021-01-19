# -*- coding:utf-8 -*-

import re
import csv
import requests
from pyquery import PyQuery as pq

url = "http://yss.mof.gov.cn/2018czjs/index.htm"

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
doc = pq(content)

"""
<a href="./201907/t20190718_3303107.htm" target="_blank">2018年全国一般公共预算收入决算表National General Public Budget Revenue</a>
"""

pattern = '<a href="./(.*?)" target="_blank">(.*?)</a>'

content_str = str(doc("td"))

content_list = re.findall(pattern, str(content), re.S)

print(len(content_list))
for line in content_list:
    print(line[0], line[1])
