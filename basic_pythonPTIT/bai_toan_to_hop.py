#CodePTIT PY01072
from itertools import combinations #thư viện tổ hợp
s = input()
n = int(s.split()[0])
k = int(s.split()[1])
my_list = input().split()
my_set = set()
for i in my_list:
    my_set.add(int(i))
a = list(my_set)
a.sort()
combine = combinations(a,k)
for i in combine:
    for j in i:
        print(j, end = ' ')
