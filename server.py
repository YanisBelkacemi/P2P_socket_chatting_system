import socket
import threading


def server(ip = "0.0.0.0" , port = 60):
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_socket.bind(ip, port)