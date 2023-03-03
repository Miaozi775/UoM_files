# # initialise the imclient
    # def __init__(self):
    #     self.im = im.IMServerProxy('https://web.cs.manchester.ac.uk/username/COMP28112_ex1/IMserver.php')      

    # # connect to the server
    


    # def connect(self, url): 
    #     self.im.connect(url)
    #     print('Connected to server.')
    #     time.sleep(1)
    #     print('Server URL: ' + url)


    # def quit(self):
    #     self.im.clear()
    #     print('Disconnected from server.')
    #     exit()


    # def message(self,mymsg):
    #     self.mymsg = mymsg
    #     mymsg = ''
    #     mymsg = input('Type your message: ')
    #     self.im.set('mymsg', mymsg)
    #     print('Message sent to server.')
    #     print('Waiting for response...')
    #     time.sleep(5)

    #     print('Message received from server: ' + self.im.get('mymsg'))
        
    #     return mymsg

    # quit the server
    def quit(self):
        self.im.clear()
        print('Server cleared.')
        print('Goodbye.')
    

    











        














    # # def set(self, key, value):
    # #     self.im.set(key, value)

    # # def get(self, key):
    # #     return self.im.get(key)
    
    # # def unset(self, key):
    # #     self.im.unset(key)

    # # def clear(self):
    # #     self.im.clear()

    # # def keys(self):
    # #     return self.im.keys()
    
    # # def __getitem__(self, key):
    # #     return self.im.get(key)
    


# initialise the imclient
    def __init__(self, url):

        # create a server proxy and connect to the server
        self.im = self.server 
        self.server = self.im.IMServerProxy(url)
        self.url = 'https://web.cs.manchester.ac.uk/u38174ys/comp28112_ex1/IMserver.php'
        print ('Connected to server.')



    def quit(self):

        # clear the server, when the user quits
        self.server.clear()
        print('Server cleared.')
        print('Goodbye.')
        


    def send_Message(self, msg):

        # store the message in the server
        self.server[msg] = msg
        msg = input('Type your message: ')
        print('Message sent: ' + msg)
        print('Message sent to server.')

        # wait for 5 seconds
        print('Waiting for response...')
        time.sleep(5)

        # retrieve the message from the server
        print('Retrieving message from server...')
        msg = self.server[msg]
        print('Message received: ' + msg)
        
        # respond to the message
        print('Responding to message...')
        msg = input('Type your message: ')
        self.server[msg] = msg
        print('Message sent: ' + msg)
        print('Message sent to server.')

        return self.server[msg]
    


    def get_Message(self):

        # wait for 5 seconds
        print('Waiting for message...')
        time.sleep(5)

        # retrieve the message from the server
        print('Retrieving message from server...')
        msg = self.server[msg]
        print('Message received: ' + msg)
        
        # respond to the message
        print('Responding to message...')
        msg = input('Type your message: ')
        self.server[msg] = msg
        print('Message sent: ' + msg)
        print('Message sent to server.')

        return self.server[msg]
    








#  # send a message to the server
    def send(self, myMessage):

        
            if myMessage == 'quit':
                self.quit()
                break

            # for storing the message
            else:
                self.im['message'] = myMessage
                myMessage = input('Type your message: ')
                myMessage.send(myMessage.encode())
                print('Message sent.')
                print('')
                
                # wait for a response
                print('Waiting for response...')
                time.sleep(5)

                # retrieve the message from the server
                print('Retrieving message from server...')
                print('Message received: ' + myMessage)
                print('')


    # get a message from the server
    def get(self, myMessage):

        # wait for a message
        print('Waiting for message...')
        time.sleep(5)

        # retrieve the message from the server
        print('Retrieving message from server...')
        myMessage.receive(myMessage.decode())
        print('Message received: ' + myMessage)
        print('')

        # respond to the message
        print('Responding to message...')
        myMessage = input('Type your message: ')
        self.im['message'] = myMessage
        print('Message sent.')
        print('')



imclient_u38174ys()


    # send message between two users
    def send(self, user1, user2, myMessage):
        
        msg = myMessage

        # send message
        msg = ''
        msg = input('Type your message: ')
        self.im.set('mymsg', msg)
        print('Message sent to server.')

        # wait for response
        print('Waiting for response...')
        time.sleep(30)
        print('')

    # receive message from another user
    def receive(self, user1, user2):
            
            # get message
            msg = self.im.get('mymsg')
            print('Message received: ' + msg)
            print('')

            # respond to message
            msg = ''
            msg = input('Type your message: ')


            # initialise the server
    def __init__(self):

        # connect to the server
        self.im = im.IMServerProxy('https://web.cs.manchester.ac.uk/u38174ys/comp28112_ex1/IMserver.php')
        if True:
            print ('Connected to server.')
            print ('')


    # quit the server
    def quit(self):
        self.im.clear()
        print ('You have quit the server')
        print ('')

    
    # user enter server
    def enter(self, user1, user2):
        self.im.set(user1, user2)
        self.im.set(user2, user1)
        print ('You have entered the server')
        print ('')

    # user leave server
    def leave(self, user1, user2):
        self.im.unset(user1)
        self.im.unset(user2)
        quit()
    





imclient_u38174ys()


   

        
            