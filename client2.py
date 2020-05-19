import socket



HEADER = 1024
PORT = 9998
SERVER = socket.gethostbyname(socket.gethostname())

FORMAT = "utf-8"
DISCONNECT_MESSAGE = "8"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) 

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+= b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    resp= client.recv(HEADER).decode(FORMAT)
    result = client.recv(HEADER).decode(FORMAT)
    print('server wrote {}'.format(resp))
    print(result)
    
    
def printMenu():
    menuItems = ["1. Find customer", "2. Add customer", "3. Delete customer", "4. Update customer age", "5. Update customer address", "6. Update customer phone", "7. Print report", "8. Exit"]
    print("Python DB Menu")
    print(*menuItems , sep= '\n')
    
printMenu()

# send(message)
# print("1) Create <name> \n 2) Read <name> \n 3) Update <name> \n 4) delete <name> \n 5) Print state \n 6) Exit server")
while True:
    message = input('Enter command \n')
    if message
    send(message)
    if message[0] == DISCONNECT_MESSAGE:
        break
    
    


# send(DISCONNECT_MESSAGE)
