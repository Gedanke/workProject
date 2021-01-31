# -*- coding:utf-8 -*-

import re
import csv
import requests

# url = 'http://yss.mof.gov.cn/2018czjs/index.htm'
url = 'http://yss.mof.gov.cn/2012zhongyangyusuan/'
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
<a href="./201907/t20190718_3303107.htm" target="_blank">2018年全国一般公共预算收入决算表National General Public Budget Revenue</a>
"""
match_pattern = '<a href=".(/2.*?)".*?target="_blank".*?>(.*?)</a>'

results = re.findall(match_pattern, str(content), re.S)
#
# for result in results:
#     print(result)
# print(len(results))
d = "• 广州南联航空食品有限公司调整10kV电增容进线电缆及配套电柜项目中标候选人公示 2021-01-28"
# print(d.split(" "))
import random

print(random.randint(0, 100) / 200)
