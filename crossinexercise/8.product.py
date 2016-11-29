# -*- coding: utf-8 -*-

for i in range(1, 10):      #左边乘数1-9循环
    for j in range(1, i+1):  #右边乘数1-i循环
        print '%d * %d = %d' % (j, i, j*i)
