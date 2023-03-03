# Summary: For user A and user B, when User A get in the server, the server will told user A whether there is someone
# is typing message according to the status of typing. 
# If there is someone is typing, user A will wait until he/she received the message and then type the message in.

import im
import time
server= im.IMServerProxy('https://web.cs.manchester.ac.uk/g48534lw/comp28112_ex1/IMserver.php')
								  # Question 1:
def type_message():
	print("Input your message: ") # Note user to input message
	server["typing"] = "true"     # set status of typing to true, which means there is someone typing
	message = input()			  # get the message from user 
	server["message"]=message     # store the message in the key called "message"
	server["typing"] = "false"    # set status of typing to false, which means no one is typing
	server["printed"] = "false"   # set the status of the message, which means the message haven't print yet
	print("Sending...")    		  # Let the user feels that the message is sending

def print_message():
	print(server["message"])	  # Print the message to another user
	server["printed"]="true"	  # set the status of the message to true, which means the message has printed

# MAIN PROGRAM
# check whether there are keys in the server(for a cleared server)
if(server.keys()== [b'']):		  # if there are no keys in the server
	type_message()				  # Let user type the message and set keys in the server
else:							  # if there are keys in the server, check the status of the keys then decide the 
								  # following steps
	count = 0   				  # initialize the count, which is used to break deadlock
	while True:					  # start the infinite loop
		if(count>5):			  # if the count is greater then 5, which means maybe both of the users are waiting for messages.
								  # we suppose that deadlock appears
			if(server["printed"]==b'true\n'):		# if there is no message which is not printed
				server["typing"]="false"  			# then set type to false
		if(server["typing"]==b'false\n'):			# if no one is typing 
			if(server["printed"]==b'false\n'):		# and the message did not printed yet
				count = 0							# initialize the count 
				print_message()						# print the message 
				type_message()						# then let the user type new message 

			elif(server["printed"]==b'true\n'):		# if the message has printed
				type_message() 						# let the user type message directly

		elif(server["typing"]==b'true\n'):			# if there is someone is typing
			if count == 1:							# if count is one 
				print("Waiting for a message")		# let the user know he/she is waiting for someone's message 
			count += 1  							# add one to the count
			
		time.sleep(10)								# stop for 10 seconds so that count will not add up too fast
													# and the program will not think deadlock occurs

# Question2: 
# Give one example of a limitation of this system architecture, 
# and one example of one way by which this limitation could be overcome, 
# towards the realisation of a more realistic messaging system. (3 marks)

# Actually there are many limitations of the system which I developed. 
# I think the most obvious one is that the user can not send several messages during continuous time.
# When we using whatsapp it is really general that someone will send message continously.
# So I think we can add more keys as queue which can use the time token as the name of the key and store the messages in the key.
# Then store each key in the queue. 
# When another user get in the server, the user can get all the messages in the queue. (which is first in first out so that we can
# get the messages in the correct order) 


