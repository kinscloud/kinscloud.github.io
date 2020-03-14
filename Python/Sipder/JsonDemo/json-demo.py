import json

books = [
    {
        'title':'晚春江晴寄友人 / 晚春别',
        'price':9.8
    },
     {
        'title':'虞美人·韶华争肯偎人住',
        'price':9.8
    }
]
json_str = json.dumps(books,ensure_ascii=False)
# print(json_str)

with open('books.json','w',encoding='utf-8') as f:
    #f.write(json_str)
    json.dump(json_str,f,ensure_ascii=False)

# py_str = json.loads(json_str)
# print(py_str)
with open('books.json','r',encoding='utf-8') as f:
    py_str = json.load(f)
    
print(py_str)