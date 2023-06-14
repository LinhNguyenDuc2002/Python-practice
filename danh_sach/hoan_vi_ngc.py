import itertools
test = int(input())
while test > 0:
    n = int(input())
    ds = list()
    sum = 1
    for i in range(n,0,-1):
        ds.append(str(i))
        sum *= i
    per = itertools.permutations(ds)
    print(sum)
    for i in per:
        print("".join(i),end = ' ')
    print()
    test -= 1
