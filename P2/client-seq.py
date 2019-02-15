# Programming our first client
import socket
from Seq import Seq

while True:
    # Create a socket for communicating with the server
    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    IP = "192.168.56.1"
    # Connect to server
    s.connect((IP, PORT))

    # Ask the user for a sequence
    msg = Seq(input("Write a sequence: "))

    # Getting the reverse and the complement of the sequence
    s_reverse = msg.reverse().strbases
    s_comp = msg.complement().strbases
    new_seq = s_reverse, s_comp

    # Encode convert a string to bytes
    s.send(str.encode(str(new_seq)))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER")
    print(msg)
