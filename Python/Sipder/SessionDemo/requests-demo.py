import requests
import time
import json
url_start = "https://www.lagou.com/jobs/list_运维?"
url_parse = "https://www.lagou.com/jobs/positionAjax.json?"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
proxy = {"HTTP": "171.35.211.234:9999"}

getkey = {
    'city':'成都',
    'cl':'false',
    'fromSearch':'true',
    'labelWords':'',
    'suginput':''
}
postkey = {
    'needAddtionalResult':'false'
}

for x in range(1, 5):
    data = {
        'first': 'true',
        'pn': str(x),
        'kd': '运维'
    }
    #构建一个session对象
    session = requests.Session()
    #用GET方法读取源网页
    #如果ssl证书没验证的话，加上verify=False
    session.get(url_start, headers=headers, params=getkey, proxies=proxy,timeout=3)
    #将源网页的cookies存入变量
    cookie = session.cookies
    #通过源网页的session访问目的网页，可以不传cookies作为参数
    #response = session.post(url_parse, data=data,params=postkey, headers=headers, cookies=cookie,  timeout=3)
    response = session.post(url_parse, data=data,params=postkey, headers=headers,  timeout=3)
    #暂停5秒
    time.sleep(5)
    #response.encoding = response.apparent_encoding
    print(response.json())
    #text = json.loads(response.text)
    #print(text)