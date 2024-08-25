import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",10000))
#client.setblocking(0) # danylan hemmesi barmayan etya


data = "Hello World"*1024*1024
sent = client.send(data.encode("UTF-8"))
print(sent,len(data))
