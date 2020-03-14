import requests
from bs4 import BeautifulSoup

url= "http://www.baidu.com"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content.decode(),'lxml')

title = soup.select('title')
print(title[0].string)
print(title[0].get_text())
print("="*30)
lista = soup.select('a')
print(lista[1])
print("="*30)
lista = soup.select('a[class="mnav"]')
#lista = lista.select('.mnav')
#print(lista[0].string)
print(lista[0].get("href"))
print(lista[0].href)
print("="*30)
print(type(lista))
print(type(lista[0]))
print(type(lista[0].strings))
print(type(lista[0].string))
print("="*30)
str='''
<p><!-- a comment test --></p>
'''
soup = BeautifulSoup(str,'lxml')
p = soup.select('p')
t = p[0]
print(type(t.string))
print(type(t.contents))
print(type(t.children))