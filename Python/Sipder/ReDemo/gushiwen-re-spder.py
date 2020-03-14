import requests
import re

def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.text
    #re.S == re.DOTALL
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text)
    content_tags = re.findall(r'<div\sclass="contson"\s.*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        content1 = re.sub(r'<.*?>','',content)
        contents.append(content1.strip())
    
    #用zip函数打包，示例如下
    # a = [1,2,3]
    # b = [4,5,6]
    # c = [4,5,6,7,8]
    # zipped = zip(a,b)     # 打包为元组的列表
    # 结果为：[(1, 4), (2, 5), (3, 6)]
    # zip(a,c)              # 元素个数与最短的列表一致
    # 结果为：[(1, 4), (2, 5), (3, 6)]
    # zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    # 结果为：[(1, 2, 3), (4, 5, 6)]
    poems=[]
    for value in zip(titles,dynasties,authors,contents):
        #从value中取对应的值
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynastie':dynasty,
            'author':author,
            'content':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print("="*40)


    

def main():
    url = 'https://www.gushiwen.org/default_{}.aspx'
    for i in range(1,11):
        parse_page(url.format(i))
        #break

if __name__ == "__main__":
    main()