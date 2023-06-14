def find(n,k):
    if k==2**(n-1):
        return chr(n+64)
    if k<=(2**(n-1)-1):
        return find(n-1,k)
    else:
        return find(n-1,k-2**(n-1))
test = int(input())
while test > 0:
    n,k = map(int,input().split())
    print(find(n,k))
    test -= 1
# a 
# aba
# abacaba
# abacabadabacaba 4 8