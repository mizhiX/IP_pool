import requests

# 如果代理需要认证, 在代理前面加上用户名密码即可
# proxy = 'username:password@113.200.56.13:8010'
proxy = '113.200.56.13:8010'

# 键名: 协议类型
# 键值: 代理
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
url = 'http://httpbin.org/get'
try:
    response = requests.get(url, proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
