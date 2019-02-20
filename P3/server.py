import socket
from Seq import Seq

PORT = 8085
IP = "212.128.253.110"
# Number of clients, if it's full the client will receive a message
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Info must be decode and encode to use in the connection
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    actions = {}

    if msg == "EXIT":
        cs.send(str.encode("Server finished"))

        cs.close()
        return False
    elif msg == "":
        cs.send(str.encode("ALIVE"))
    else:
        msg = msg.split("\n")
        seq = Seq(msg.pop(0))
        for request in msg:
            print(request)
            if "count" in request or "perc" in request:
                base = request[-1]
                request = request[:-1]
                action = seq.call_function(request, base)
                actions.update({request + base: action})
            else:
                print(request)
                action = seq.call_function(request)
                actions.update({request: action})

    # Sending the message back to the client
    # (because we are an echo server)
    msg = ["OK"]
    for values in actions.values():
        msg.append(str(values))
    msg = "\n".join(msg)
    cs.send(str.encode(msg))
    cs.close()
    return True


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

while True:

    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    process_client(clientsocket)

    # -- Process the client request
    print("Attending client: {}".format(address))
