import socket

HOST = ("localhost",10000)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

s.bind(HOST)
s.listen()

print("Listening")

while 1:
    client, addr = s.accept()
    print (f"New connection from - {addr}")
    
    data = client.recv(1024)
    while data :
        print(data)
        
        data = client.recv(1024)
        
    print("All data has been received!")
    client.close()