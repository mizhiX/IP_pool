from selenium import webdriver

url = 'http://httpbin.org/get'
service_args = [
    '--proxy=113.200.56.13:8010',
    '--proxy-type=http',
    # 如果需要认证, 那么再加入--proxy-auth选项即可
    '--proxy-auth=username:password'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get(url)
print(browser.page_source)