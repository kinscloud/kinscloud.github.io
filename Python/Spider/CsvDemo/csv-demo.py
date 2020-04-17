import csv

def write_csv_demo1():
    headers=['name','age','classroom']
    values = [
        ("张三",20,"502班"),
        ("李四",22,"508班"),
        ("王五",23,"508班")
    ]

    #newline默认是\n,不加行间有空行
    with open('classroom.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(values)

def read_csv_demo1():
    with open('classroom.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f)
        #next跳过标头
        next(reader)
        for x in reader:
            #print(x) #只能通过下标取值
            print({'name':x[0],'age':x[1],'classroom':x[2]})

def  write_csv_demo2():
    headers=['name','age','classroom']
    values = [
        {'name':'张三','age':20,'classroom':'502班'},
        {'name':'李四','age':22,'classroom':'508班'},
        {'name':'王五','age':23,'classroom':'508班'}
    ]

    with open('classroom.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(values)

def read_csv_demo2():
    with open('classroom.csv','r',encoding='utf-8') as f:
        #用DictReader不会包含标头
        reader= csv.DictReader(f)
        for x in reader:
            #print(x) #x是有序字典，可通过key的方式取值
            print(x["name"])


if __name__ == "__main__":
    #write_csv_demo2()
    read_csv_demo2()
