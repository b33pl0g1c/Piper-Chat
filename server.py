import socket
import threading

HOST='127.0.0.1'
PORT=9988

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(HOST,PORT)

clients=[]
nicknames=[]

#broadcast
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break

#receive
def receive():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is{nickname}")
        broadcast(f"{nickname} joined the chat".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))
        thread=threading.Thread(target=handle,args=(client,))


#handle-errors
print("Server Up and Running....")
receive()



