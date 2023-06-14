# s = input()
# number4 = s.count("4")
# number7 = s.count("7")
# sum = number4+number7
# print("YES") if sum==4 or sum==7 else print("NO")


test = int(input())
while test>0:
    s = input()
    check = False
    for i in range(0,9):
        if i!=4 and i!=7 and str(i) in s:
            check = True
            break
    print("YES") if check==False else print("NO")
    test -= 1