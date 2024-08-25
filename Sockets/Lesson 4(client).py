import socket, sys

HEADER_LENGTH = 10  # Corrected the spelling
SERVER = ("localhost", 10000)

username = input("Please type a username at first: ").encode("UTF-8")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER)
s.setblocking(0)

# Corrected the format string
header = f"{len(username):<{HEADER_LENGTH}}".encode("UTF-8")
s.send(header + username)

while True:
    print("Please write a message:")
    msg = input().encode("UTF-8")
    
    if msg:
        # Corrected the format string here as well
        msg_header = f"{len(msg):<{HEADER_LENGTH}}".encode("UTF-8")
        s.send(msg_header + msg)
        print(msg_header, msg)
    
    try:
        while True:
            user_header = s.recv(HEADER_LENGTH)
            if not len(user_header):
                sys.exit()
            
            user_length = int(user_header.decode("UTF-8").strip())
            username = s.recv(user_length)
            
            msg_header = s.recv(HEADER_LENGTH)
            msg_length = int(msg_header.decode("UTF-8").strip())
            
            data = s.recv(msg_length).decode("UTF-8")
            print(f"New message from: {username.decode('UTF-8')} - {data}")
    
    except IOError as _ex:
        pass
