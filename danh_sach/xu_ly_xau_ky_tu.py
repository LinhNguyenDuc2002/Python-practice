
s1 = set(input().lower().split())
s2 = set(input().lower().split())
a = list(s1.union(s2))#hợp
b = list(s1.intersection(s2))#giao
a.sort()
b.sort()
print(*a)
print(*b)
