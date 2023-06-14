def encrypt(s,n):
    kq = ""
    for i in s:
        if ord(i)+n>ord('Z'):
            kq += chr(((ord(i)+n)%ord('Z'))+64)
        else:
            kq += chr((ord(i)+n))
    return kq
def decrypt(s,n):
    kq = ""
    for i in s:
        if ord(i)-n<ord('A'):
            kq += chr((ord(i)-n)+26)
        else:
            kq += chr((ord(i)-n))
    return kq
s = input()
# print('encode',encrypt(s,n))
for i in range(1,26):
    print('decode',i,decrypt(s,i))
