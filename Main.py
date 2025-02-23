import socket
import threading

def RecieveMessage(connection , adr):
    while True:
        try:
            message = connection.recv(1024).decode('utf-8')
            if message :
                print(f'[{adr}] : {message}') 
            else:
                break
        except:
            break
def SendMessage(connection):
    while True:
        message = input()
        connection.send(message.encode('utf-8'))
        print(f'Me : {message}')
def server(ip = "0.0.0.0" , port = 2096):
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f'Server is waiting on {ip}:{port}')
    conn , adr = server_socket.accept()
    print(f'connected {adr}')
    receive_message =threading.Thread(target = RecieveMessage, args=(conn , adr))
    receive_message.start()
    send_message = threading.Thread(target= SendMessage , args=(conn,))
    send_message.start()
    receive_message.join()
    send_message.join()

server()