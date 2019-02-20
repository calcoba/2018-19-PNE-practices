import socket

# SERVER IP, PORT
PORT = 8085
IP = "212.128.253.110"
activity = True


msg = """AGTGTGTAGTGCGTG
len
countA
reverse
complement
countC
countG
countT"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))
# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers respoinse
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))


s.close()
