from urllib import request
from http.cookiejar import MozillaCookieJar

url="https://www.baidu.com/"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

cookiejar = MozillaCookieJar("cookie.txt")
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open(url)

for cookie in cookiejar:
    print(cookie)

cookiejar.save(ignore_discard=True)