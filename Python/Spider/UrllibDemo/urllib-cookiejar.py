#本代码演示urllib的Cookiejar的基本用法
from urllib import request,parse
from http.cookiejar import CookieJar

login_url = "http://www.renren.com/PLogin.do"
dapeng_url= "http://www.renren.com/880151247/profile"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    data = {
        'email':'970138074@qq.com',
        'password':'pythonspider'
    }
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)

def visit_profile(opener):
    resp = opener.open(dapeng_url)
    print(resp.read().decode())

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)