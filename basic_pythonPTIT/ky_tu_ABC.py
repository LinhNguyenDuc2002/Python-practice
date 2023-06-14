import itertools
def generate(n,s):
    if len(s)<=n:
        if s.count('A')<=s.count("B")<=s.count("C"):
            ds = list(itertools.permutations(s))
            for i in ds:
                print(''.join(i))
        generate(n,s+"A")
        generate(n,s+"B")
        generate(n,s+"C")
n = int(input())
kq = list()
generate(n,"ABC")