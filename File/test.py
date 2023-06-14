# # with open('File/test_file.txt','r') as my_file:
# with open('File/test_file.txt','w') as my_file:
#     my_file.write('hello')
#     # contents = my_file.read()
#     # my_file.close()

#     # đọc từng dòng
#     # for line in my_file:
#     #     print(line.strip())
# # print(contents) 

# # 'a': nối thêm vào file

# # xử lý ngoại lệ
# try:
#     # lệnh gây lỗi
#     print(5/0)
# except:
#     # xử lý khi gặp lỗi
#     print('error')

a = list()
b = list()
n = int(input())
with open('./File/A.txt','r') as my_file:
    for line in my_file:
        try: 
            a+=map(int,line.split())
        except:
            print('File A error')
with open('./File/B.txt','r') as my_file:
    for line in my_file:
        try: 
            b+=map(int,line.split())
        except:
            print('File B error')
for i in range(n):
    kq = a[i]**b[i]
    print(f'{a[i]}^{b[i]}={kq}')