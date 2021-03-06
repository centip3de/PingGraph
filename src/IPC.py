import queue

class IPC():

    clients = {}

    def add(client):
        if(client not in IPC.clients):
            IPC.clients[client] = queue.Queue()
            return True
        else:
            return False

    def getMessages(client):
        if(client in IPC.clients):
            item = IPC.clients[client].get()
            return item

        return None
    
    def sendTo(client, msg):
        if(client in IPC.clients):
            IPC.clients[client].put(msg)
            return True

        return False

    def sendToAll(msg):
        print("Putting: " + str(msg))
        for client in IPC.clients:
            IPC.clients[client].put(msg)

    def remove(client):
        if(client in IPC.clients):
            del IPC.clients[client]
            return True

        return False
            
        
