import socket

PORT = 8080
IP = "212.128.253.108"
# Number of clients, if it's full the client will receive a message
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Info must be decode and encode to use in the connection
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    # Sending the message back to the client
    # (because we are an echo server)
    cs.send(str.encode(msg))

    cs.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# One parameter but it's a tuple
serversocket.bind((IP, PORT))

# Special socket to listen to the client, we pass the, maximum clients that can be at the same time
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    process_client(clientsocket)

    # -- Process the client request
    print("Attending client: {}".format(address))
