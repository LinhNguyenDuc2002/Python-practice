import socket
import threading
import time
import hashlib
HOST = '127.0.0.1'
PORT = 8080
secret_key = 'b20dcat109'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT)) #đăng ký tên socket và ràng buộc address
s.listen(2) #cho phép socket lắng nghe tối đa 2 bên

def sent_message(client):
    while True:
        msg = input('Sent to client: ')
        if len(msg)==0:
            continue
        hash_code = hashlib.sha512((msg+secret_key).encode()).hexdigest()
        data_sent = msg + '|' + hash_code
        client.sendall(bytes(data_sent,"utf8")) #gửi dữ liệu thông qua TCP
def receive_message(client):
    while True:
        data = client.recv(1024) #nhận dữ liệu
        msg, hash_code = data.decode("utf8").split('|') #phân tích dữ liệu vừa nhận
        # Kiểm tra tính toàn vẹn
        check_hash_code = hashlib.sha512((msg+secret_key).encode()).hexdigest()
        if hash_code == check_hash_code:
            print("The received message from server is:",msg)
        else:
            print("The received message has lost its integrity")

while True:
    # Khi một client gõ cửa, server chấp nhận kết nối 
    # và 1 socket mới được tạo ra. Client và server bây giờ 
    # đã có thể truyền và nhận dữ liệu với nhau
    client, addr = s.accept()
    try:
        print('Connected by', addr)
        t1 = threading.Thread(target=sent_message, args=(client,))
        t2 = threading.Thread(target=receive_message, args=(client,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    finally:
        client.close()
s.close()