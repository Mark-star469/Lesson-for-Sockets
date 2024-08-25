import socket

HOST = (socket.gethostname(),10000)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(HOST)
s.listen()

print("I am listening your connecting!")

while True:
    conn, addr = s.accept()
    print("Connected -",addr)
    
    sms = "Hello Bro You are WELCOME"
    res = (sms.encode("UTF-8"))
    conn.send(res)
    
    conn.close()