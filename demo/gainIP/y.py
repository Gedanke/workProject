# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery
import selenium


session = requests.session()
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}
url = "https://www.zbytb.com/s-jian-136965.html"
# url = "https://www.zbytb.com/skin/default/flexpaper/flexpaper_flash.js"
r = session.get(url, headers=headers)
cookies = r.cookies
r = session.get(url, headers=headers, cookies=cookies)
print(r.text)
