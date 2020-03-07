#! /usr/bin python3
# --*-- encoding:utf-8 --*--

#输出1-100以内不是7的倍数且不包含7的数
for i in range(1,101):
    include = str(i).find('7')
    if include == -1 and int(i)%7 != 0:
        print(i)
        
