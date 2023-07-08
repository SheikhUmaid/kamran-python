import socket

print("creating server")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("binding server")
serversocket.bind(('127.0.0.1', 80))
print("listening to clients")
serversocket.listen(5)

addr1, client = serversocket.accept() # client1
print(f"connected to {addr1}")
addr1.send('Connected to server'.encode())

addr2, client = serversocket.accept() # client1
print(f"connected to {addr2}")
addr2.send('Connected to server'.encode())


while True:

    # a = input("you: ")
    # if a == 'q':
    #     break
    # addr1.send(a.encode())
    # addr2.send(a.encode())

    message = addr1.recv(1024).decode()
    addr2.send(message.encode())
    message = addr2.recv(1024).decode()
    addr1.send(message.encode())

    # print(f"Client: {message}")

