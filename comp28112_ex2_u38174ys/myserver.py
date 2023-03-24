import sys
import time
from ex2utils import Server

# calculate how many users are connected to the server
conn_c = 0
# collect theb name of the users connected to the server
# conn_n = []

# Create an echo server class  
class EchoServer(Server):

    conn_c = 0
    # conn_n = []

    # connect to the server
    def onStart(self):

        print("Echo server has started.")

    # disconnect from the server
    def onStop(self):

        print("Echo server has stopped.")

    # client connects to the server
    def onConnect(self, socket):

        global conn_c
        conn_c += 1

        # print when a client connects to the server 
        time.asctime( time.localtime(time.time()) )
        print("One client connected at " + time.asctime( time.localtime(time.time()) ))

        # print the number of clients connected to the server
        print("One client connected. There are now " + str(conn_c) + " clients connected.")

    # client disconnects from the server
    def onDisconnect(self, socket):

        global conn_c
        conn_c -= 1

        # print when a client disconnects from the server
        time.asctime( time.localtime(time.time()) )
        print("One client disconnected at " + time.asctime( time.localtime(time.time()) ))

        # print the number of clients connected to the server
        print("One client disconnected. There are now " + str(conn_c) + " clients connected.")

    # process incoming messages
    def onMessage(self, socket, message):

        # tell the client that the message has been sent
        print("Message sent")

        # wait a few seconds, make sure the client receives the message and responds
        time.sleep(5)

        # send the message back to the client
        message = message.encode()
        socket.send(message)

        # tell the client that the message has been received
        print("Message received")

        # return True to keep the connection open
        return True
        
 



# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = EchoServer()

# Start server
server.start(ip, port)



        









