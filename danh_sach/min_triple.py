import sys
test = int(input())
while test > 0:
    n = int(input())
    s = input()
    s = s.strip()
    s += " "
    while s.find("  ")>=0:
        s = s.replace("  "," ")
    min1, min2, min3 = 10**9, 10**9, 10**9
    a = ''
    for i in s:
        if i!=" ":
            a += i
        else:
            x = int(a)
            if x<=min3:
                min3, min2, min1 = x, min3, min2
            elif x<=min2:
                min2, min1 = x, min2
            elif x<=min1:
                min1 = x
            a = ''
    print(min1+min2+min3)
    test -= 1
