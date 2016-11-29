# -*- coding: utf-8 -*-

n = input()
for i in range(1,n+1):  #一共循环n行，从1到n
    for j in range(0,n-i): #第i行前面要空n-i个空格
      print '', #输出一个空字符加逗号，起到输出空格的作用
    for j in range(0,i): #第i行输出i个*
      print '*', #输出*
    print                      #换行


