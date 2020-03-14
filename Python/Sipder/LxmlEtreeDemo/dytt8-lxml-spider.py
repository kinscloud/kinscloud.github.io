import requests
from lxml import etree

BASE_DOMAIN = "https://www.ygdy8.net"
START_URL = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
URLS = []

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Referer": "https://www.ygdy8.net/"
}


def get_detail_urls():
    for i in range(1, 7):
        url = START_URL.format(i)
        response = requests.get(url, headers=HEADERS)
        html = etree.HTML(response.text)
        ulinks = html.xpath("//a[@class='ulink']/@href")
        for link in ulinks:
            link = BASE_DOMAIN + link
            URLS.append(link)


def get_film():
    for url in URLS:
        response = requests.get(url, headers=HEADERS)
        html = etree.HTML(response.content.decode("gbk"))
        title = html.xpath('//div[@class="title_all"]//font/text()')
        if len(title) > 0:
            print(title[0])
        downloadurl = html.xpath('//td[@bgcolor="#fdfddf"]/a/@href')
        if len(downloadurl) > 0:
            print(downloadurl[0])

if __name__ == "__main__":
    get_detail_urls()
    get_film()
