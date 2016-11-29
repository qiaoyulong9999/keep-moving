# _*_ coding=utf-8 _*_

for n in range(1,200):
   #N从1到199循环
   sq = n*n
   #sq是n的平方
   str_sq = str(sq)
   #把平方值转为字符串
   istr_sq = str_sq[::-1]
   #把字符串逆序
   #list中括号中冒号分割的第三个值表示步长
   #步长-1表示倒着每个值都取出来
   if str_sq == istr_sq:
       #如果正序倒序都一样
       print n
       #符合条件，输出结果
