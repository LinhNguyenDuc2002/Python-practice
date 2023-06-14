# tg = [0]*11
# def Load(n,a):
#     if n==0:
#         return
#     s = str(n)
#     l = len(s)
#     for i in range(10):
#         a[i] += tg[l-1]
#     for i in range(l-1):
#         a[0] -= pow(10,i)
#     for i in range(l):
#         j = 0
#         p = 0
#         if i==0:
#             p=1
#             j=1
#             a[0] += tg[l-i-1]*(ord(s[i])-48-p)
#         sum = tg[l-i-1]*(ord(s[i])-48-p)
#         while j < ord(s[i])-48:
#             a[j] += pow(10,l-i-1)+sum
#             j+=1
#         a[j]+=n%(pow(10,l-i-1))+sum+1
#         for k in range(j+1,10):
#             a[k] += sum
# test = int(input())
# for i in range(10):
#     tg[i] = int(i*pow(10,i-1))
# while test > 0:
#     a,b = map(int,input().split())
#     aa = [0]*20
#     bb = [0]*20
#     Load(a-1,aa)
#     Load(b,bb)
#     for i in range(10):
#         print(bb[i]-aa[i],end = ' ')
#     print()
#     test -= 1

def f(x, n):
    ret = 0
    for i in range(0, 10):
        m = 10**i
        if m > n: 
            break
        a = n // m
        b = n % m
        z = a % 10
        if z > x: 
            ret += ((a // 10) + 1) * m
        elif z == x: 
            ret += (a // 10) * m + (b + 1)
        else: 
            ret += (a // 10) * m
        if x == 0: 
            ret -= m
    return ret
def digitsCount(d, low, high):
    return f(d,high) - f(d,low-1)
test = int(input())
while test > 0:
    a,b = map(int,input().split())
    for i in range(0, 10): 
        print(digitsCount(i,a,b), end=' ')
    print()
    test -= 1
