import socket



HEADER = 1024
PORT = 9994
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
# while True:
    
    
#         try:
#             message = int(input('Select:'))
#             break
#         except:
#             print("That's not a valid option!")
#     m = str(message)
#     send(m)

#     if m[0] == DISCONNECT_MESSAGE:
#         break
# while True:

    # try:
    #     # 1|asdsda|1211
        
    #     message = int(input('Select:'))
    #     if message in range(1,9):
    #         validatedMessage = str(message)
    #         send(validatedMessage)
    #     else:
    #         print('Invalid command. Command must be in range 1 to 8')
    #     if validatedMessage == DISCONNECT_MESSAGE:
    #         break
    #     printMenu()
    # except:
    #         print("That's not a valid option! Please enter command in range 1 to 8")\
while True:
    message = input('Select:')
    if message.isnumeric() and int(message) in range(1,9):
        if int(message) == 1: 
            name = input('please enter name:')
            mes = message +"|"+ name
            send(mes)
        

        if int(message) == 5: 
            send(message)
    else:
        print('Invalid command. Command must be in range 1 to 8')
 
    if message == DISCONNECT_MESSAGE:
        break

# send(DISCONNECT_MESSAGE)
