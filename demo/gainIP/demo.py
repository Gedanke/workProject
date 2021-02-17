# -*- coding:utf-8 -*-


import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features-AutomationControlled")
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')

driver = Chrome('chromedriver', options=chrome_options)
driver.set_window_size(1366, 768)
with open('/home/dfs/repository/py/stealth.min.js-main/stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})
driver.get('https://www.zbytb.com/s-jian-136965.html')
# 你可以保存源代码为 html 再双击打开，查看完整结果 https://bot.sannysoft.com/
source = driver.page_source
print(source)
with open('result.html', 'w') as f:
    f.write(source)
