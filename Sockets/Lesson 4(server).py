import socket, select

HEADER_LENGTH = 10
HOST = ("localhost", 10000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(HOST)
server.listen()

print("I am listening to your connections!")

# Add the server socket to the socket_list
socket_list = [server]
client_list = {}

def receive_msg(client: socket.socket):
    try:
        msg_header = client.recv(HEADER_LENGTH)
        if not len(msg_header):
            return False
        
        msg_length = int(msg_header.decode("UTF-8").strip())
        return {
            "header": msg_header,
            "data": client.recv(msg_length)
        }
    
    except:
        return False

while True:
    rs, _, xs = select.select(socket_list, [], socket_list)
    
    for _socket in rs:
        if _socket == server:
            client, addr = server.accept()
            user = receive_msg(client)
            
            if user is False:
                continue
            
            socket_list.append(client)
            client_list[client] = user
            data = user["data"]
            print(f"New connection from {addr} with data {data.decode('UTF-8')}")
        
        else:
            msg = receive_msg(_socket)  # It should be _socket, not client
            
            if msg is False:
                print(f"Connection from {addr} has been interrupted")
                socket_list.remove(_socket)
                del client_list[_socket]
                continue
            
            user = client_list[_socket]
            
            for client in client_list:
                if client is not _socket:
                    client.send(user["header"] + user["data"] + msg["header"] + msg["data"])
    
    for _socket in xs:
        socket_list.remove(_socket)
        del client_list[_socket]
