import socket

# SERVER IP, PORT
PORT = 8002
IP = "212.128.253.106"
activity = True

while activity:
    msg = input(">")
    msg = msg.replace(" ", "\n")
    if not msg:
        msg = "empty"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))
    # Send the request message to the server
    s.send(str.encode(msg))
    print("conected")

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))


    s.close()
