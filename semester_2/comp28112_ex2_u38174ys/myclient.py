"""

IRC client exemplar.

"""

import sys
import time
from ex2utils import Client

import time

# record the number of users connected to the server
conn_c = 0
# record the name of the users connected to the server
conn_n = []
# links name to socket
conn_s = {}



class IRCClient(Client):
	
    # connect to server
    def onConnect(self, socket):

        global conn_c
        conn_c += 1

        # print when a client connects to the server
        time.asctime( time.localtime(time.time()) )
        print("One client connected at " + time.asctime( time.localtime(time.time()) ))


        print ("Welcome to the chat! Please type your name: (new + your name)".encode())
        name = input("Enter your name: ")

        if name in conn_n:
            print("This name is already taken. Please choose a different name.")
            name = input("Enter your name: ")
        else:
            conn_n.append(name)
            print("You are now connected to the chat. There are now " + str(conn_c) + " clients connected.")

        return super().onConnect(socket)

    # send message to server
    def onMessage(self, socket, message):
        
        return super().onMessage(socket, message)
    
    # disconnect from server
    def onDisconnect(self, socket):
        
        command = input("Type quit to disconnect: ")
        if command == "quit":
            self.stop()
            return False
        # return super().onDisconnect(socket)
    



# Parse the IP address and port you wish to connect to.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an IRC client.
client = IRCClient()

# Start server
client.start(ip, port)

#send message to the server
message = "hello world"
client.send(message.encode())

#stops client
client.stop()


