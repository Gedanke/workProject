# -*- coding:utf-8 -*-

import re
import time
import json
import random
from pyquery import PyQuery
import requests

'''以中标公告为例'''
root_url = "https://csbidding.csair.com/cms/channel/bidzbgg/index.htm?pageNo="
url_dict = dict()
url_file = "url.json"

'''请求头'''
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}


def gain_urls(page_num: int):
    """
    gain all url
    :param page_num: 待爬取的页数
    :return:
    """
    page = "https://csbidding.csair.com"
    for i in range(page_num):
        now_url = root_url + str(i)
        '''随机休眠，防止请求过于频繁'''
        t = random.randint(0, 100) / 200
        time.sleep(t)
        response = requests.get(now_url, headers=headers)
        content = str(response.text)
        '''使用 css 选择器选择 id 为 list1 的节点，该节点下含有待爬的ulr'''
        pp = PyQuery(content)("#list1")
        '''url 是放在 <a> 节点里的，继续选择 <a> 节点'''
        for i in pp("a").items():
            '''构造 url'''
            url = page + str(i.attr("href"))
            '''构造url对应的公告名称'''
            if str(i.text()).find(" ") != -1:
                name_list = str(i.text()).split(" ")
                name = name_list[1] + ":" + name_list[2]
                '''存放到字典里'''
                url_dict[name] = url
    '''写入 json 文件中'''
    json_str = json.dumps(url_dict)
    with open(url_file, 'w') as json_file:
        json_file.write(json_str)


def gain_data(url_name: str):
    """

    :param url_name:
    :return:
    """
    url = url_dict[url_name]
    file = "data/" + url_name + ".txt"
    response = requests.get(url, headers=headers)
    content = str(response.text)
    '''公告内容存放在 main-text class 节点下'''
    p = PyQuery(content)(".main-text")
    files = open(file, "w")
    for i in p.items():
        '''获取其文本内容，写入文本文件'''
        files.write(i.text())
    files.close()


if __name__ == '__main__':
    """"""
    '''待爬的页面数'''
    page_num = 114
    '''鉴于需要的链接都已经保存到json文件了，gain_urls 运行一次就可以了'''
    gain_urls(page_num=1)
    with open(url_file, 'r') as f:
        url_dict = json.load(f)
    for url_name, url in url_dict.items():
        '''随机休眠，防止请求过于频繁'''
        t = random.randint(0, 100) / 200
        gain_data(url_name)
