#CodePTIT ICPC0108
test = int(input())
while test >0:
    n = int(input())
    list1 = list(map(int,input().split()))
    count = 0
    list1.sort()
    for i in range(0,len(list1)-2):
        j = i+1
        k = len(list1)-1
        while j<k:
            if list1[i]+list1[j]+list1[k]==0:
                count += 1
                j += 1
            elif list1[i]+list1[j]+list1[k]>0:
                k -= 1
            else:
                j += 1
    print(count)
    test -=1