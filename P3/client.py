import socket

# SERVER IP, PORT
PORT = 8001
IP = "127.0.0.1"

msg = """AGTGTCTGT
len
countH"""
# Verify if the message is empty
if not msg:
    msg = "empty"

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
