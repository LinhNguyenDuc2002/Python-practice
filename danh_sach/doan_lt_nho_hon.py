test = int(input())
while test>0:
    n = int(input())
    a = list(map(int,input().split()))
    st = list()
    for i in range(0,len(a)):
        while len(st)>0 and a[st[-1]]<=a[i]:
            st.pop()
        if len(st)==0:
            print(i+1,end=" ")
        else:
            print(i-st[-1],end=" ")
        st.append(i)
    print()
    test -= 1