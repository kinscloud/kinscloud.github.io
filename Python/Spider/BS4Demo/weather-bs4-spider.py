import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    # 爬取港澳台时因为HTML代码不规范用lxml会出错，要用html5lib修正
    #soup = BeautifulSoup(text,'lxml')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        # enumerate返回索引和项两个值
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = int(temp_td.string)
            ALL_DATA.append({"city": city, "min_temp": min_temp})


def main():
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    ]
    for url in urls:
        parse_page(url)

    # def sort_key(data):
    #     min_temp = data["min_temp"]
    #     return min_temp

    # ALL_DATA.sort(key=sort_key)
    ALL_DATA.sort(key=lambda data: data["min_temp"])
    data = ALL_DATA[0:10]
    cities = list(map(lambda x: x['city'],data))
    temps = list(map(lambda x: x['min_temp'],data))

    chart = Bar("中国天气最低气温排行榜")
    chart.add("",cities,temps)
    chart.render('temps.html')


if __name__ == "__main__":
    main()
