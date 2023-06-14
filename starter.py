"""
1. Sử dụng # để cmt
2. sử dụng \ để code trên nhiều dòng
3. Có thể đặt chuỗi trong dấu nháy đơn và nháy kép đều dc
4. Chú ý các cách code sau đây đều được chấp nhận
    a,b,c = 1,2,3
    a=b=c=5
5. eval()
    ví dụ: s = '5'
    int(s) = eval(s) = 5 (integer)
    ví dụ: s = '1+1'
    int(s) => error
    eval(s) = 2 (integer)
6. 
-----------------Nhập xuất---------------------
    print(9, 10, 11, 12, sep='#', end='&')
    => 9#10#11#12&

    print('I like {1} but hate {0}'.format('fish','meat'))
    => I like meat but hate fish

    x = 26.394852
    print('The value of x is %5.1f' %x)
    => The value of x is 26.4

    i = 2
    j = 4
    print(f'Phep tinh {i}^{j}', end = '')
    => Phep tinh 2^4

    join()
    ví dụ: s = ('1','2','3','4','5','6')
    print(' # '.join(s)) => 1 # 2 # 3 # 4 # 5 # 6
-----------------itertool--------------------
    1. permutations(ds): hoán vị
    2. combinations(ds,chập): tổ hợp
------------------LÀM TRÒN--------------------
    1. 123 => 120  125 => 130  235 => 200
        ví dụ: s = 123 muốn làm tròn thành 120
        s = int(Decimal(s).quantize(Decimal('1E1'),ROUND_HALF_UP))
        
        ví dụ: s = 123 muốn làm tròn thành 100
        s = int(Decimal(s).quantize(Decimal('1E2'),ROUND_HALF_UP))

        *Một số module decimal
        ROUND_CEILING. nó sẽ tròn về phía Vô cực,
        ROUND_DOWN. nó sẽ làm tròn giá trị về 0,
        ROUND_FLOOR. nó sẽ quay về phía -Infinity,
        ROUND_HALF_DOWN. nó sẽ làm tròn đến giá trị gần nhất tiến về 0,
        ROUND_HALF_EVEN. nó sẽ làm tròn đến giá trị gần nhất với số nguyên chẵn gần nhất,
        ROUND_HALF_UP. nó sẽ làm tròn đến gần nhất với giá trị đi từ 0
        ROUND_UP. nó sẽ làm tròn nơi giá trị sẽ đi từ 0

        Ngoài ra cũng có thể dùng round() hoặc %.5f ...
        Với round: round(0.1218,6) => 0.1218
        với %.xf: print('%.6f' %(0.1218)) => 0.121800

-----------------Chuỗi----------------------
note: 
Không thay đổi được các phần tử của chuỗi nhưng thay đổi được cả chuỗi
1. Cắt chuỗi:
    s = "hello ptit"
    s[1:4] = ello

    *Cắt các từ trong chuỗi
    mylist = s.split() => mylist = ['hello', 'ptit']
2. Độ dài chuỗi
    len(s) = 10
3. Mã ASCII
    chr(65)/unichr(65) => output: 'A'
    ord('A') => output: 65
4. Đảo ngược chuỗi
    Ví dụ: s2 = "Hello"
    s2 = s2[::-1] => s2 = "olleH"
    s2 = s2[slice(None,None,-1)] => s2 = "olleH"
    s2 = "".join(reversed(s2)) => s2 = "olleH"
5. count()
    ví dụ: s='12#232#231#'
    s.count('#') => 3
-------------Danh sách------------------------------
1. Khai báo
    mylist = []
    ví dụ: mylist = [1, 'hello', 3]
    => mylist[0] = 1
    => mylist[1] = 'hello'
    => mylist[1][2] = 'l'
    => mylist[-1] = mylist[2] = 3
2. Thêm phần tử vào danh sách
    mylist.append(phần tử) != mylist.extend(phần tử)
    ví dụ: mylist = ['a','b','c']
    mylist.append('GKH') => mylist = ['a','b','c','GKH']
    mylist.extend('GKH') => mylist = ['a','b','c','G','K','H']

    mylist.insert(vị trí, phần tử)
3. Xóa phần tử
    del mylist[vị trí]
"""

'''
*CÁC HÀM VÀ THƯ VIỆN ĐẶC BIỆT
1. title(): 
    s = "RED"
    s.title() //output: "Red"

2. gcd(a,b): (import math) tìm ước chung lớn nhất của a và b
'''

'''
'''