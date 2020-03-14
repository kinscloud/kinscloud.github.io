import requests
import random
import json
from urllib import request

# 获取网站返回的代理列表
url = 'http://api.newday.me/proxy/extract'
params={"token":"970eba4e11d70f47","format":"json"}
#通过format为json接收代理
response = requests.get(url, params=params)
response_json = json.loads(response.text)
ip_list = response_json["data"]["list"]
proxy_list = []
for ip in ip_list:
      proxy_list.append("%s:%d"%(ip['ip'],ip['port']))
      
#通过format为text接收代理
#proxy_list = str(response.text).split('\r\n')

# 获取proxy.list文件中的代理列表
# with open(r'proxy.list')as b:
#     proxy_list=b.readlines()
# proxy_list = list(map(lambda x:x.replace('\n', ''),proxy_list))

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 根据协议类型，选择不同的代理
proxies = {
  "http": proxy,
  "https": proxy,
}
response = requests.get("http://httpbin.org/ip", proxies = proxies)
print(response.text)

# 使用urllib选择的代理构建代理处理器对象
httpproxy_handler = request.ProxyHandler(proxies)
opener = request.build_opener(httpproxy_handler)
request = request.Request("http://httpbin.org/ip")
html=opener.open(request).read().decode("utf-8")
print(html)