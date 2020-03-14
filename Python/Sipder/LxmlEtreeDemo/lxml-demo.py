from lxml import etree

text='''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-2"><a href="link3.html">third item</a></li>
        <li class="item-3"><a href="link4.html">forth item</a></li>
        <li class="item-4"><a href="link5.html">fifth item</a></li>
    </ul>
</div>'''

#parser = etree.HTMLParser(encoding="utf-8")
#html = etree.parse("xxx.html",parser=parser)
html = etree.HTML(text)
#print(etree.tostring(html))

# lis = html.xpath("//li")
# for li in lis:
#     print(etree.tostring(li))

# lis = html.xpath("//li[2]")
# print(etree.tostring(lis[0]))

# lis = html.xpath("//li[contains(@class,'item')]")
# print(etree.tostring(lis[0]))

# lblas=html.xpath("//a/@href")
# for lbla in lblas:
#     print(lbla)

lis = html.xpath("//li[position()>1]")
for li in lis:
    #text = li.xpath(".//a/text()")[0]
    text = li.xpath("*/text()")[0]
    print(text)


