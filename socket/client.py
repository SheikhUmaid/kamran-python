import socket

print("creating server")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.connect(('192.168.42.236',80))
print("connected to server")


message = serversocket.recv(1024).decode()
print(f"Server: {message}")

a = input('you: ')
serversocket.send(f"client: {a}".encode())