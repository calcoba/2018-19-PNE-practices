import socket

# Change this IP to yours!!!!!
IP = "212.128.253.111"
PORT = 8080


MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    """Need to look for the GET message"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging

    if "GET" in msg:
        print()
        print("Request https://github.com/calcoba/2018-19-PNE-practices.gitessage: ")
        print(msg)
        url = msg.split("\n")[0]
        try:
            request = url.split()[1]
        except IndexError:
            cs.close()
            return
        print(request)
        if "blue" in request:
            f = open("blue.html", 'r')
            content = f.read()
            f.close()

        elif "pink" in request:
            f = open("pink.html", 'r')
            content = f.read()
            f.close()
        elif len(request) > 1:
            f = open("error.html")
            content = f.read()
            f.close()

        else:
            f = open("index.html", 'r')
            content = f.read()
            f.close()

    status_line = "HTTP/1.1 200 OK\r\n"
    heather = "Content-Type: text/html\r\n"
    heather += "Content-Lenth: {}\r\n".format(len(str.encode(content)))

    response_msg = status_line + heather + "\r\n" + content

    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()
    print("This is the clientsocket: ", clientsocket)

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
