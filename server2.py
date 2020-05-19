import socket
import threading


HEADER = 1024
PORT = 9998
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "DISCONNECT"
dataBase = {}



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind(ADDR)


def readDB():
    f = open("data.txt", "r")
    print(" Reading Data Base")
    for line in f:
        lineItems = line.split("|")
        if not lineItems[0]:
            print("line \n {} \n ignored".format(line))
            continue
            

        t = ()
        for item in lineItems:
            item = item.strip()
            t = t + (item,)
        dataBase[len(dataBase)] = t
    print(" DataBase read Successfully!!")
    print("{} Valid record read from Database".format(len(dataBase)))
    
    f.close()


def handleRequest(msg):
    
    code,*name = msg.split("|")
    print("received {} {}".format(code,name))
    if name:
        return OPTIONS[int(code)](name[0])
    else:
        return OPTIONS[int(code)]()



def create(name):
    print('creating {}'.format(name))
    return True

def read(name):
    print('reading {}'.format(name))
    return True

def update(name):
    print('updating {}'.format(name))
    return True

def delete(name):
    print('deleting {}'.format(name))
    return True

def printState():
    print('printing state')
    return True,str(dataBase)

def exitServer():
    print('exiting server')
    return False
    
OPTIONS = {
    1:create,
    2:read,
    3:update,
    4:delete,
    5:printState,
    8:exitServer

}
def handle_client(conn,addr):
    print("NEW CONNECTION {}".format(addr))

    connected = True
    readDB()
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
    

def start():
    server.listen()
    print("server is listening on {}".format(SERVER))
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("{} active connections".format(threading.activeCount()-1))

print("SERVER STARTING...")
start()

