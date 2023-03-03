import im 
import time

# connect to the server
server = im.IMServerProxy('https://web.cs.manchester.ac.uk/u38174ys/comp28112_ex1/IMserver.php')
# tell the user that he/she is connected to the server
print ('Connected to server')


# send message to another user
def send():
	
    # input the message from user
    print ('Type your message: ')
    myMessage = input()
    # store the message in the server
    server['message'] = myMessage 
    # tell the user that the message is sending
    print ('Sending...')
    # tell the user that he/she is waiting for reply
    print ('Waiting for message...')    		


# receive message from another user
def recieve():
        
    # print the message from another user
	print(server['message'])
    # tell the user that the message is recieved  
	print ('Message recieved & please reply / no other message')


# main function
# check whether there are keys in the server
# if there are no keys in the server, first user sends message directly

if server.keys() == [b'']:
    server.clear()
    send()

# if there are keys in the server, do the following
else:
    
    while True:

        # if the message is empty, send message
        if server['message'] == b'':
            send()
        
        # if the message is not empty, receive message
        else:
            recieve()
            server['message'] = b''
            send()
        
        # stop a while, make sure user can read the message and reply
        time.sleep(15)

        













    # # avoiding the system deadlocking
    # count = 0

    # # the loop
    # while True:

    #     #  avoid the system deadlocking
    #     if count == 0:
    #         # if the message is empty, send message
    #         if server['message'] == b'':
    #             send()
    #         # if the message is not empty, receive message
    #         else:
    #             recieve()
    #             server['message'] = b''
    #             send()
            
    #         # change the count, means the user has sent message
    #         count = 1
        
    #     else:
    #         if server['message'] != b'':
    #             recieve()
    #             server['message'] = b''
    #         else:
    #             send()
            
    #         # means the user has received message and ready to reply
    #         count = 0

    #     # stop a while, make sure user can read the message and reply
    #     time.sleep(10)

  




		
