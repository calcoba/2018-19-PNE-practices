import socket
from Seq import Seq


def process_client(cs):
    # Info must be decode and encode to use in the connection
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    actions = {}

    # Check if the message is exit or empty to return to the main program
    if msg =="\n":
        cs.send(str.encode("ALIVE"))
        cs.close()
        return True

    # The function makes the computations
    else:
        msg = msg.split("\n")
        seq = Seq(msg.pop(0).upper())
        bases = "ACTG"

        # Check if the characters of the DNA sequence are all allowed
        if not all(c in bases for c in seq.strbases):
            cs.send(str.encode("ERROR"))
            cs.close()
            return True

        # Possible functions the program could perform
        for request in msg:
            if "count" in request or "perc" in request:
                base = request[-1]
                if base in bases:
                    request = request[:-1]
                    action = seq.call_function(request, base)
                    actions.update({request + base: action})
                else:
                    actions.update({request: "ERROR"})
            else:
                try:
                    action = seq.call_function(request)
                    actions.update({request: action})
                # If the request action is not allowed then send back an empty variable
                except AttributeError:
                    actions.update({request: "ERROR"})

    # Sending the message back to the client
    msg = ["OK"]
    for values in actions.values():
        msg.append(str(values))
    msg = "\n".join(msg)
    cs.send(str.encode(msg))
    cs.close()
    return True


PORT = 8001
IP = "212.128.253.110"
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
