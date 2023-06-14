import socket
import threading
import hashlib
HOST = '127.0.0.1'
PORT = 8080
secret_key = 'b20dcat109_linh_nd'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tham số đầu tiên là Address Family: kiểu thiết lập kết nối. Python hỗ trợ 3 dạng:
# AF_INET: Ipv4
# AF_INET6: Ipv6
# AF_UNIX
# tham số thứ hai là Socket Type: cách thiết lập giao thức
# SOCK_STREAM: TCP
# SOCK_DGRAM: UDP
server_address = (HOST,PORT) #đăng kí tên và ràng buộc địa chỉ
print(f'Connecting to {str(server_address)} port')
s.connect(server_address)

def sent_message():
    while True:
        msg = input('Sent to Server: ')
        if len(msg) == 0:
            continue
        hash_code = hashlib.sha512((msg+secret_key).encode()).hexdigest()
        data_sent = msg + '|' + hash_code
        s.sendall(bytes(data_sent,"utf8")) #gửi dữ liệu thông qua TCP
def receive_message():
    while True:
        data = s.recv(1024) #nhận dữ liệu
        msg, hash_code = data.decode("utf8").split('|') #phân tích dữ liệu vừa nhận
        # Kiểm tra tính toàn vẹn
        check_hash_code = hashlib.sha512((msg+secret_key).encode()).hexdigest()
        if hash_code == check_hash_code:
            print("The received message from server is:",msg)
        else:
            print("The received message has lost its integrity")

try:
    t1 = threading.Thread(target=sent_message)
    t2 = threading.Thread(target=receive_message)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
finally:
    s.close() #đóng kết nối