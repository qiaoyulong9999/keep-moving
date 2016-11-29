# -*- coding: utf-8 -*-
for i in range(1,1001):
    if i%3 == 2 and i%5 == 2 and i%7 == 2:
    #'%'符号是取整除后的余数
    #用'and'连接三个判断条件，只有三个条件同时满足才为True
       print i

