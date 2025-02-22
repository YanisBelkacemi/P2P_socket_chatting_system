import socket
import threading

def RecieveMessage(connection):
    while True:
        try:
            message = connection.recv(1024).decode('utf-8')
            if message :
                print('received message') 
            else:
                break
        except:
            pass
def SendMessage(connection):
    while True:
        message = input()
        connection.send(message.encode('utf-8'))
def server(ip = "127.0.0.1" , port = 12345):
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f'Server is waiting on {ip}:{port}')
    conn , adr = server_socket.accept()
    print(f'connected {adr}')
    threading.Thread(RecieveMessage, args=(conn ,)).start()
    SendMessage(conn)

server()