import re

text=r"the number is 20.10"
r = re.compile(r'''
    \d+ #整数位
    .?  #小数点
    \d* #小数位
    ''',re.VERBOSE)
ret = re.search(r,text)
if (ret != None):
    print(ret.group())
else:
    print("no found")
