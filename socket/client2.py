import socket
import playsound
print("creating server")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.connect(('127.0.0.1',80))
print("connected to server")


message = serversocket.recv(1024).decode()
print(f"Server: {message}")

while True:

    message = serversocket.recv(1024).decode()
    playsound.playsound('recv.mp3')
    print(f"Server: {message}")

    a = input('you: ')
    serversocket.send(f"{a}".encode())