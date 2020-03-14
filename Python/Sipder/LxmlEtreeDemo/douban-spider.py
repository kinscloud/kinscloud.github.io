import requests
from lxml import etree
url="https://movie.douban.com/cinema/nowplaying/shenzhen/"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Referer":"https://movie.douban.com/"
}

response = requests.get(url,headers=headers)
#print(response.text)
text = response.text
movies = []
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[1]
films = ul.xpath("li/ul")
for film in films:
    #print(etree.tostring(film,encoding="utf-8").decode("utf-8"))
    title = film.xpath("li[@class='stitle']/a/@title")[0]
    poster = film.xpath("li[@class='poster']//img/@src")[0]
    movie ={
        'title':title,
        'poster':poster
    }
    movies.append(movie)

print(movies)