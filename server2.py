import socket
import threading


HEADER = 1024
PORT = 9994
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "DISCONNECT"
dataBase = {}



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind(ADDR)

# loads the data to our server program
# dose the following simple validations:
    # makes sure that the data element has name or it ignore the record and print it
    # clear up spaces
    # and put "Not Available" as a place holder for the records that are missing(like a phone number) 
# eventually we add all data to a dictionary in which the key is customer name and the value is a tuple of record
def readDB():
    f = open("data.txt", "r")
    print(" Reading Data Base")
    for line in f:
        lineItems = line.split("|")
        if not lineItems[0]:
            print("line \n {} \n ignored".format(line))
            continue

        placeHolder = 'Not Available'
        
        t = ()
        for item in lineItems:
            item = item.strip()
            item = item.rstrip('\n')
            print(item)
        for i in lineItems:
                if not i.replace(" ", ""):
                    t = t + (placeHolder,)
                else:
                    t = t + (i,)
        dataBase[t[0]] = t[1:]
    print(" DataBase read Successfully!!")
    print("{} Valid record read from Database".format(len(dataBase)))
    
    f.close()


def handleRequest(msg):
    
    code,*name = msg.split("|")
    print("received {} {}".format(code,name))
    if name:
        return OPTIONS[int(code)](name)
    else:
        return OPTIONS[int(code)]()



def findCustomer(name):
     
    #print('creating {}'.format(name))
 
    if name[0] in dataBase.keys(): 
        tup = dataBase[name[0]]
        print(tup)
        return True, '|'.join(tup)
    else: 
        return True, "Customer Not Found"

def addCustomer(name):
    print('Customer {} added.'.format(name[0]))

    if name[0] in dataBase:
        return True , '{} already exists in database'.format(name[0])
    else:
        t =()
        placeHolder = 'not available'
        for i in name[1:]:
            if not i:
                t = t + (placeHolder,)
            else:
                t = t + (i,)
    
        dataBase[name[0]] = t
        return True , 'Customer {} added.'.format(name[0])


def deleteCustomer(name):
    # return True , '{} Deleted!.'.format(name[0])

    if name[0] in dataBase:
        del dataBase[name[0]]
        return True , '{} Deleted!.'.format(name[0])
    else:
        return True , '{} dose not exist in database. wanna add? select option1!.'.format(name[0])
 
    

def UpdateAge(name):
    #print('deleting {}'.format(name))
    if name[0] in dataBase:
        customerRecord = dataBase[name[0]]
        lst = list(customerRecord)
        lst[0] = name[1]
        t = tuple(lst)
        dataBase[name[0]] = t
        return True , ' age updated for {} '.format(name[0])
    else:
        return True, '{} dose not exist in our dataBase '.format(name[0])

def UpdateAddress(name):
    
    if name[0] in dataBase:
        customerRecord = dataBase[name[0]]
        lst = list(customerRecord)
        lst[1] = name[1]
        t = tuple(lst)
        dataBase[name[0]] = t
        return True , ' Address updated for {} '.format(name[0])
    else:
        return True, '{} dose not exist in our dataBase '.format(name[0])


def UpdateNumber(name):
    #print('deleting {}'.format(name))
    if name[0] in dataBase:
        customerRecord = dataBase[name[0]]
        lst = list(customerRecord)
        lst[2] = name[1]
        t = tuple(lst)
        dataBase[name[0]] = t
        print(dataBase[name[0]])
        return True , ' Number updated for {} '.format(name[0])
    else:
        return True, '{} dose not exist in our dataBase '.format(name[0])



def printState():
    print('printing state')
    resultToServer = ""

    for customer in dataBase:
        customerInformationTuple  = dataBase[customer]
        customerInformationString = '|'.join(customerInformationTuple)
        resultToServer = resultToServer + customerInformationString
        
    return True,str(resultToServer)

def exitServer():
    print('exiting server')
    return False,'Exit'
    
OPTIONS = {
    1:findCustomer,
    2:addCustomer,
    3:deleteCustomer,
    4:UpdateAge,
    5:UpdateAddress,
    6:UpdateNumber,
    7:printState,
    8:exitServer
}
def handle_client(conn,addr):
    print("NEW CONNECTION {}".format(addr))

    connected = True
    
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            # if msg == DISCONNECT_MESSAGE:
            #     connected = False
            
            print("address {} wrote {}".format(addr,msg))
            # handleRequest2(msg)
            connected,response = handleRequest(msg)
            
            conn.send( "Message received ".encode(FORMAT))
            conn.send(response.encode(FORMAT))
            # conn.send(resp)
            
    conn.close()
    print("disconnected client")
    
# Starts Server:
# the assignment requires only one connection but my code can work properly with multiple connections.
# the method starts the server and read the database from file data.txt which should be in the same directory
# database configuration are provided at the top of this file

def start():
    server.listen()
    print("server is listening on {}".format(SERVER))
    readDB()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("{} active connections".format(threading.activeCount()-1))

print("SERVER STARTING...")
start()

