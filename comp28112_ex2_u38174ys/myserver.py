import sys
import time
from ex2utils import Server

# calculate how many users are connected to the server
conn_c = 0
# collect theb name of the users connected to the server
conn_n = []
# links name to socket
conn_s = {}

# Create an echo server class  
class EchoServer(Server):

    conn_c = 0
    conn_n = []
    conn_s = {}

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

        self.socket = socket
        socket.send("Welcome to the chat! Please type your name: (new + your name)".encode())
    
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

        # Parse the message into a command and parameters
        command, sep, parameter = message.strip().partition(' ')

        # one client has one socket
        self.socket = socket

        # deal with the command
        # for new clients to declare their name
        if command == "new":

            global clientName
            clientName = parameter

            # one name can only be used by one client
            if clientName in conn_n:

                socket.send("This name has been used. Please choose another name.".encode())
                socket.send("Type 'new + your name' to declare your name.".encode())
            
            else:

                # add new client into the list
                conn_n.append(clientName)
                # link the name to the socket
                conn_s[clientName] = socket

                # print the name of the client who has connected to the server
                print(f"{clientName} has joined the chat.")
                # print the list of clients connected to the server
                print("The clients connected to the server: " + str(conn_n))

                if len(conn_n) == 1:

                    # tell the client that they are the only client connected to the server
                    socket.send("You are the only client connected to the server. You can't send message.".encode())
                    socket.send("Wait a few minutes. You can type 'give list' to see who join in".encode())

                    # tell them how to leave the chat
                    socket.send("Type 'quit + your name' to disconnect.".encode())
                    
                else:

                    # tell them how to leave the chat
                    socket.send("Type 'quit + your name' to disconnect.".encode())

                    # tell them how to send messages to all clients
                    socket.send("Type 'send + your message' to send a message to all clients.".encode())

                    # tell them how to send messages to a specific client
                    socket.send("Type 'one + target client + your message' to send a message to a specific client.".encode())
                    l = "Those are the clients connected to the server: " + str(conn_n)
                    socket.send(l.encode())

        
        # clients can check the list of clients connected to the server
        elif command == "give":

            message = parameter

            # send the list of clients connected to the server to the client
            message = message.encode()
            
            # send the list of clients connected to the server to the client
            socket.send(str(conn_n).encode())

            if len(conn_n) == 1:

                socket.send("You are the only client connected to the server. You can't send message.".encode())
                socket.send("Wait a few minutes. You can type 'give list' to see who join in".encode())

            else:   

                # tell them how to leave the chat
                socket.send("Type 'quit + your name' to disconnect.".encode())

                # tell them how to send messages to all clients
                socket.send("Type 'send + your message' to send a message to all clients.".encode())

                # tell them how to send messages to a specific client
                socket.send("Type 'one + target client + your message' to send a message to a specific client.".encode())


        # for clients to send messages to all other clients
        elif command == "send":

            message = parameter

            # send the message to all clients connected to the server
            message = message.encode()

            # send the message to all clients connected to the server, except the client who sent the message
            for i in conn_s:
                    
                    if i != clientName:
    
                        socket = conn_s[i]
                        socket.send(message)
                        print ("Message sent")
                        # wait a few seconds, make sure the client receives the message and responds
                        time.sleep(5)
                        print("Other clients has received the message.")

                        # tell the client need response
                        socket.send("Please reply.".encode())
                        socket.send("Please type 'send + your message' to send a message to all clients.".encode())
                        socket.send("Please type 'one + target client + your message' to send a message to a specific client.".encode())
                        l = "Those are the clients connected to the server: " + str(conn_n)
                        socket.send(l.encode())
                        socket.send("Please type 'quit + your name' to disconnect.".encode()) 


        # for clients to send messages to a specific client
        elif command == "one":

            # The parameter should be the target user and message
            target_client, sep, message = parameter.partition(' ')

            # send the message to the target user
            for i in conn_s:

                if i == target_client:

                    socket = conn_s[i]
                    socket.send(message.encode())
                    print("Message sent")
                    # wait a few seconds, make sure the client receives the message and responds
                    time.sleep(5)
                    print("The target client has received the message.")

                    # tell the client need response
                    socket.send("Please reply.".encode())
                    socket.send("Please type 'send + your message' to send a message to all clients.".encode())
                    socket.send("Please type 'one + target client + your message' to send a message to a specific client.".encode())
                    l = "Those are the clients connected to the server: " + str(conn_n)
                    socket.send(l.encode())
                    socket.send("Please type 'quit + your name' to disconnect.".encode())


        # for clients to disconnect from the server
        elif command == "quit":
                
                # remove the client from the list
                for i in conn_n:
                    clientName = i
                    if i == parameter:
                        conn_n.remove(i)
                        print(f"{clientName} has left the chat.")
                        print("The clients connected to the server: " + str(conn_n))

                socket.send("Goodbye!".encode())
                socket.close()
                
                return False


        
        else:
            print("Invalid command.")
    

        # return True to keep the connection open
        return True
        
 



# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = EchoServer()

# Start server
server.start(ip, port)



        









