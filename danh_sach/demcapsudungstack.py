from math import* 
import re 

class Data:
    def __init__(self, height, check, same):
        self.height = height
        self.check = check
        self.same = same

def info(h, behind, same):
    return Data(h, behind, same)

def solve():
    S = []
    cnt = 0
    n = int(input())
    while n>0:
        h = int(input())
        if len(S)>0:
            t = S[-1] 

        if len(S) == 0:
            S.append(info(h, 0, 0))
        elif len(S) > 0 and t.height == h:
            cnt += 1
            cnt += t.same
            if t.check == 1:
                cnt += 1
            S.append(info(h, t.check, t.same+1))
        elif len(S) > 0 and t.height > h:
            S.append(info(h, 1, 0))
            cnt += 1
        elif len(S) > 0 and t.height < h:
            while len(S) > 0 and t.height < h:
                cnt += 1
                S.pop()
                if len(S) == 0:
                    break
                t = S[-1]
            if len(S) > 0:
                t = S[-1]
            if len(S) > 0 and t.height == h:
                cnt += 1
                cnt += t.same
                if t.check == 1:
                    cnt += 1
                S.append(info(h, t.check, t.same+1))
            elif t.height > h and len(S) > 0 :
                cnt += 1
                S.append(info(h, 1, 0))
            else:
                S.append(info(h, 0, 0))
        n -= 1
    print(cnt)
if __name__=='__main__':
    solve()