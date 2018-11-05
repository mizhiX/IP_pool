"""
urllib设置代理方法
"""

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 如果代理需要认证, 在代理前面加上用户名密码即可
# proxy = 'username:password@113.200.56.13:8010'
proxy = '113.200.56.13:8010'

# 键名: 协议类型
# 键值: 代理
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
url = 'http://httpbin.org/get'
opener = build_opener(proxy_handler)
try:
    response = opener.open(url)
    print(response.read().decode('utf8'))
except URLError as e:
    print(e.reason)

