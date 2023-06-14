#CodePTIT PY01023
import math
test = int(input())
while test>0:
    s = int(input())
    my_dict = {}
    while s%2==0:
        my_dict.update([(2,my_dict.get(2,0)+1)])
        s //= 2
    for i in range(3,int(math.sqrt(s))+1,2):
        while s%i==0:
            my_dict.update([(i,my_dict.get(i,0)+1)])
            s //= i
    if s>1:
        my_dict.update([(s,1)])
    print("1", end = '')
    for i in my_dict:
        print(f' * {i}^{my_dict[i]}', end = '')
    print()
    test -= 1