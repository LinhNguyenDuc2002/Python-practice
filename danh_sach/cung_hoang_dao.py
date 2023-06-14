test = int(input())
def findstt(day,month):
    return month*30+day
while test > 0:
    a,b = map(int,input().split())
    x = findstt(a,b)
    if x>=findstt(21,3) and x<=findstt(19,4):
        print('Bach Duong')
    elif x>=findstt(20,4) and x<=findstt(20,5):
        print('Kim Nguu')
    elif x>=findstt(21,5) and x<=findstt(20,6):
        print('Song Tu')
    elif x>=findstt(21,6) and x<=findstt(22,7):
        print('Cu Giai')
    elif x>=findstt(23,7) and x<=findstt(22,8):
        print('Su Tu')
    elif x>=findstt(23,8) and x<=findstt(22,9):
        print('Xu Nu')
    elif x>=findstt(23,9) and x<=findstt(22,10):
        print('Thien Binh')
    elif x>=findstt(23,10) and x<=findstt(22,11):
        print('Thien Yet')
    elif x>=findstt(23,11) and x<=findstt(21,12):
        print('Nhan Ma')
    elif x>=findstt(23,11) and x<=findstt(21,12):
        print('Nhan Ma')
    elif x>=findstt(22,12) or x<=findstt(19,1):
        print('Ma Ket')
    elif x>=findstt(20,1) and x<=findstt(18,2):
        print('Bao Binh')
    else:
        print('Song Ngu')
    test -= 1