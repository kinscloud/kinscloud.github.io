#encodeing=utf-8

import time
import os, sys

with open('tmp.txt','rb') as f:
    f.seek(0,2)
    while True:
        line =f.read()
        if line:
            print(line.decode('utf-8'),end='')
        else:
            time.sleep(0.2)
            
with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    # data = read_f.read()
    # data = data.replace('str1', 'str2')
    # write_f.write(data)
    for line in read_f:
        line = line.replace('str1', 'str2')
        write_f.write(line)
    
os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')