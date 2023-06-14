import itertools
s = input()
perm = itertools.permutations(s)
for i in perm:
    print(''.join(i))