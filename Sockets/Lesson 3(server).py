import socket,pickle

HOST = (socket.gethostname(),10000)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(HOST)
s.listen()

print("I am listening your connecting!")


d = {
     "Client" : "Maks",
     "Pasword": 12345
     }


while True:
    conn, addr = s.accept()
    print("Connected -",addr)
    
    res = pickle.dumps(d)
    conn.send(res)
    conn.close()