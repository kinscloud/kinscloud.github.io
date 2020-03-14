#本代码演示urllib的代理和用户头的基本用法
#先导入urllib   如果没有这个 请用pip install urllib安装一下
from urllib import request,parse
import random

#代理列表
proxy_list=[
    {"http" : "218.18.158.216:8000"},
    {"http" : "60.191.11.246:3128"},
    {"http" : "218.27.136.169:8085"},
    {"http" : "182.88.199.169:9797"},
    {"http" : "60.191.11.229:3128"}
]
#随机取出一个代理
proxy = random.choice(proxy_list)
#用户头列表
USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]
#随机取出一个用户头
user_agent = random.choice(USER_AGENTS)
headers = {
    'User-Agent':user_agent
}

# 这里要用到我们的request.ProxyHandler代理管理器
proxy_handler = request.ProxyHandler(proxy)
#制作发起请求管理器request.build_opener ，把我们管理器都放进去
openr = request.build_opener(proxy_handler)
#构建一个request对象
req = request.Request("http://httpbin.org/ip",headers=headers)
html=openr.open(req).read().decode("utf-8")
#不用opener的方法
#html=request.urlopen(req).read().decode("utf-8")
#不用headers直接访问的方法
#html=request.urlopen("http://httpbin.org/ip").read().decode("utf-8")
print(html)

#小细节，分析URL
# result =parse.urlparse('http://www.baidu.con/index.html;useer?id=5#comment')
# print(result)
# print(result.hostname)