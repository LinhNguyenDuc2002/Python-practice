#CodePTIT PY01007
import math
test = int(input())
while test>0:
    s = input()
    # mylist = s.split()
    n = float(s.split()[0])
    x = float(s.split()[1])
    m = float(s.split()[2])
    i = 1
    while True:
        if n*(math.pow(x/100+1,i))>=m:
            print(i)
            break
        i += 1
    test -= 1