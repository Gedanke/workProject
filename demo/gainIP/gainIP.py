# -*- coding: utf-8 -*-

import requests
import json

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

api_url = "http://www.xiladaili.com/api/?uuid=ab0954a7b09e494baa8001eeed2c7d3c&num=10&place=中国&category=1&protocol=2&sortby=0&repeat=1&format=3&position=1"
split_character = " "
check_url = 'https://www.ip.cn/'

index = 0


def gain_ip(api_url):
    """

    :param api_url:
    :return:
    """
    proxies = {
        'http': 'http://120.83.110.147:9999',
        'https': 'https://120.83.110.147:9999',
    }
    ip_list = str(requests.get(api_url).text).split(" ")
    for ip in ip_list:
        for key, value in proxies.items():
            proxies[key] = str(key) + "://" + ip
        print(proxies)
        print(test(proxies))


def test(proxies: dict):
    """

    :param proxies:
    :return:
    """
    res = False
    try:
        request = requests.get(url=check_url, headers=headers, proxies=proxies, timeout=3)
        if request.status_code == 200:
            res = True
    except Exception as error_info:
        global index
        index += 1
        res = False
    return res


if __name__ == '__main__':
    """"""
    gain_ip(api_url)
    # print("True : " + str(index))
    # proxies = {
    #     'http': 'http://103.26.247.130:8080',
    #     'https': 'https://103.26.247.130:8080',
    # }
    # r = requests.get(url=check_url, headers=headers, proxies=proxies, timeout=5)
    # print(r.status_code)
