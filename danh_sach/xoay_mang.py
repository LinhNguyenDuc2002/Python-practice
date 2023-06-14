test = int(input())
while test>0:
    n,k = map(int,input().split())
    list1 = list(map(int,input().split()))
    list2 = list1.copy()
    for i in range(0,len(list1)):
        list2[i] = list1[(i+k)%n]
    for i in list2:
        print(i, end = ' ')
    print()
    test-=1