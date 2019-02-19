import socket
import termcolor

PORT = 8081
IP = "212.128.253.108"
# Number of clients, if it's full the client will receive a message
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Info must be decode and encode to use in the connection
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    if msg == "EXIT":
        cs.send(str.encode("Server finished"))

        cs.close()
        return False
    msg_print = termcolor.colored(msg, 'green')
    print("Message from the client: {}".format(msg_print))

    # Sending the message back to the client
    # (because we are an echo server)
    msg_send = termcolor.colored(msg, 'grey')
    cs.send(str.encode(msg_send))

    cs.close()
    return True


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# One parameter but it's a tuple
serversocket.bind((IP, PORT))

# Special socket to listen to the client, we pass the, maximum clients that can be at the same time
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))
active = True
while active:

    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    if process_client(clientsocket):

        # -- Process the client request
        print("Attending client: {}".format(address))
    else:
        active = False
