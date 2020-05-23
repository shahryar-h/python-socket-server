import socket


# Client configurations
HEADER = 1024
PORT = 9994
SERVER = socket.gethostbyname(socket.gethostname())

FORMAT = "utf-8"
DISCONNECT_MESSAGE = "8"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) 




# sends and recives message to/from Server
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+= b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    resp= client.recv(HEADER).decode(FORMAT)
    result = client.recv(HEADER).decode(FORMAT)
    print("##############################################################################")
    print(r"                               server's Response: ")
    print("##############################################################################")
    print(result)
    print("##############################################################################")
    
# prints clients menu
# it reprint every time a request served so there is no need for client to scroll up for options 
def printMenu():
    menuItems = ["1. Find customer", "2. Add customer", "3. Delete customer", "4. Update customer age", "5. Update customer address", "6. Update customer phone", "7. Print report", "8. Exit"]
    print("\n\n")
    print("DB Menu")
    print(*menuItems , sep= '\n')
    

# keeps getting the requests from client until they close the connection by selecting 8
# it only accepts values 1-8 and dose error handling in case of invalid input

while True:
    printMenu()
    message = input('Select:')
    if message.isnumeric() and int(message) in range(1,9):
        if int(message) == 1: 
            name = input('please enter name:')
            mes = message +"|"+ name
            send(mes)
        elif int(message) == 2:
            newCustomer = ""        
            thename = input('please name:')
            if thename:
                newCustomer = newCustomer + thename
                age = input('please enter age:')
                if age:
                    newCustomer = newCustomer + "|" + age
                
                address = input('please enter address:')
                if address:
                    newCustomer = newCustomer + "|" + address

                phoneNumber = input('please enter phone number:')
                if phoneNumber:
                    newCustomer = newCustomer + "|" + phoneNumber

                mes = message +"|"+ newCustomer
                send(mes)
            else:
                print("can't add a customer without name")
        elif int(message) == 3:
                customerDelete = input('please Provide the name of the customer you want to delete:')
                mes = message +"|"+ customerDelete
                send(mes)
        elif int(message) == 4:
                updateCustomer = input('please the name of the customer you want to update name:')
                if updateCustomer:
                    customerAge = input('please the provide the age: ')
                    mes = message + "|" + updateCustomer + "|" + customerAge
                    send(mes)
                else:
                    print("can't Update a customer without name")
        elif int(message) == 5:
                updateCustomer = input('please the name of the customer you want to update Address: ')
                if updateCustomer:
                    customerAddress = input('please the provide the Address: ')
                    mes = message + "|" + updateCustomer + "|" + customerAddress
                    send(mes)
                else:
                    print("can't Update a customer without name")
        elif int(message) == 6:
                updateCustomer = input('please the name of the customer you want to update name:')
                if updateCustomer:
                    customerAge = input('please the provide the age: ')
                    mes = message + "|" + updateCustomer + "|" + customerAge
                    send(mes)
                else:
                    print("can't Update a customer without name")

        if int(message) == 7: 
            send(message)
    else:
        print('Invalid menu option. you must select a number in range 1 to 8')
 
    if message == DISCONNECT_MESSAGE:
        send(message)
        break

# send(DISCONNECT_MESSAGE)
