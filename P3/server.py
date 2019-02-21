import socket
from Seq import Seq


def process_client(cs):
    # Info must be decode and encode to use in the connection
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    actions = {}

    if msg == "EXIT":
        cs.send(str.encode("Server finished"))
        cs.close()
        return False
    elif msg == "empty":
        cs.send(str.encode("ALIVE"))
    else:
        msg = msg.split("\n")
        seq = Seq(msg.pop(0).upper())
        for request in msg:
            if "count" in request or "perc" in request:
                base = request[-1]
                request = request[:-1]
                action = seq.call_function(request, base)
                actions.update({request + base: action})
            else:
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


PORT = 8000
IP = "127.0.0.1"
# Number of clients, if it's full the client will receive a message
MAX_OPEN_REQUEST = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

server_activity = True
while server_activity:

    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    if not process_client(clientsocket):
        server_activity = False
    # -- Process the client request
    print("Attending client: {}".format(address))
