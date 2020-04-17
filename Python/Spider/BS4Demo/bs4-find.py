import requests
from bs4 import BeautifulSoup

url= "http://www.baidu.com"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content.decode(),'lxml')
#print(soup.title)
title = soup.find('title')
print(title.string)
print(title.get_text())
print("="*30)
#print(soup.a)
lista = soup.find_all('a',limit=2)
print(lista[1])
print("="*30)
#lista = soup.find_all('a',class_='mnav')
lista = soup.find_all('a',attrs={"class":"mnav"})
print(lista[0].string)
print("="*30)
#lista = soup.find_all('a',href="https://www.hao123.com",class_="mnav")
lista = soup.find_all('a',attrs={"href":"https://www.hao123.com","class":"mnav"})
print(lista)
print("="*30)
lista = soup.find_all('a')
for a in lista:
    # href = a.attrs["href"]
    # print(href)
    str = a["href"]
    if str.startswith("http"):
        print(str)
print("="*30)
info = soup.find_all('div')
#lists = list(info[0].strings)
lists = list(info[0].stripped_strings)
print(lists)
