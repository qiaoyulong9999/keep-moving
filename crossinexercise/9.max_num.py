# -*- coding: utf-8 -*-

x = input()
y = input()
z = input()

max_num = x        #再定义一个参数为最大值是很重要的思想
if y > max_num:
    #如果y大于x,最大值设为y
    max_num = y

if z > max_num:
    #如果z大于x,y间最大值，最大值设为z
    max_num = z

print max_num
