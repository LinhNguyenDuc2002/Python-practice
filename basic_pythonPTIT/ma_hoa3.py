test = int(input())
while test > 0:
    s = input()
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:]
    sum1 = sum2 = 0
    for i in s1:
        sum1 += ord(i)-65
    for i in s2:
        sum2 += ord(i)-65
    kq1 = kq2 = ''
    for i in s1:
        kq1 += chr((ord(i)-65+sum1)%26+65)
    for i in s2:
        kq2 += chr((ord(i)-65+sum2)%26+65)
    s = ''
    for i in range(len(kq1)):
        s += chr((ord(kq1[i])-65+ord(kq2[i])-65)%26+65)
    print(s)
    test -= 1
    

