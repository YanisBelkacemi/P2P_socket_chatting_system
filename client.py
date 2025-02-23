import socket
import threading

def receive_messages(sock , ip):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"{ip[0]}: {message}")
            else:
                break
        except:
            print("Connection closed.")
            break

def send_messages(sock):
    while True:
        message = input()
        sock.send(message.encode('utf-8'))
        print(f'Me : {message}')

def connect_to_server(host='127.0.0.1', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    threading.Thread(target=receive_messages, args=(client_socket, host)).start()
    send_messages(client_socket)

if __name__ == "__main__":
    connect_to_server()