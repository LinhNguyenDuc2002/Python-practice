import sympy # Thư viện hỗ trợ random số nguyên tố
class RSA_algorithm:
    def __init__(self) -> None:
        self.public_key = []
        self.private_key = []
        self.generate()

    # Tạo cặp khóa public and private key
    def generate(self):

        # Tạo 2 số nguyên tố lớn p và q sao cho p#q
        # Độ dài khóa khoảng từ 1024 đến 2048 bit
        p = sympy.randprime(2**1024//2, 2**1024)
        q = p
        while q==p:
            q = sympy.randprime(2**1024//2, 2**1024)

        n = p*q
        phi = (p-1)*(q-1) # Hàm số Euler

        # 0<e<phi và e là số nguyên tố cùng nhau với phi
        e = sympy.randprime(2**1024//2, 2**1024)

        d = pow(e,-1,phi) # d = pow(e,-1) mod phi

        self.public_key = [e,n] # n: modun, e: số mũ mã hóa
        self.private_key = [d,n] # n: modun, d: số mũ giải mã

        print(f'q = {q}\np = {p}\nn = {n}\nphi = {phi}\ne = {e}\nd = {d}')

    # Mã hóa    
    def encrypt(self,message):
        e,n = self.public_key[0],self.public_key[1]
        encode = []
        for i in message:
            encode.append(pow(ord(i),e,n)) # c = m^e mod n
        return encode
    
    # Giải mã
    def decrypt(self,message):
        d,n = self.private_key[0],self.private_key[1]
        decode = ''
        for i in message:
            decode += str(chr(pow(i,d,n))) # m = c^d mod n
        return decode

rsa = RSA_algorithm()
message = input('Enter your message: ')
print('------')
print(f'Plain text: {message}')
encode = rsa.encrypt(message)
decode = rsa.decrypt(encode)
print(f'Encrypt message: {encode}')
print(f'Decrypt message: {decode}')
