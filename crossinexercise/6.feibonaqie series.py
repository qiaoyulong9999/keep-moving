n = input()
a1 = 1
a2 = 1
x = 3
print a1
print a2
while x <= n:
    a3 = a1+a2
    print a3
    a1 = a2
    a2 = a3
    x += 1
