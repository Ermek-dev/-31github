import socket
from datetime import datetime


HOST = '127.0.0.1'
PORT = 8001
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen()
    print(f"Ожидаем подключение на порту {PORT}")
    conn, addr = s.accept()
    print(f"Подключен {addr}")
    conn.sendall(b'Input your age: \n')
    age = conn.recv(1024)
    try:
        real_age = int(age)
    except ValueError:
        conn.sendall(b'error!!! \n') 
        conn.close()
        s.close()
    else:
        if real_age>=21:
            message = b'Hello!!!\n'
        else:
            message = b'Access is denied!!!\n'
        conn.sendall(message)           
    
    conn.close()
    s.close()