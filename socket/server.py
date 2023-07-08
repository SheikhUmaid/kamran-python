import socket

print("creating server")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("binding server")
serversocket.bind(('192.168.42.236', 80))
print("listening to clients")
serversocket.listen(5)

addr, client = serversocket.accept() # client1
print(f"connected to {addr}")

a = input("you: ")
addr.send(a.encode())

message = addr.recv(1024).decode()
print(f"Client: {message}")

