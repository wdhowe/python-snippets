#!/usr/bin/env python3
"""
Title: sockets_client.py
Description: Client Sockets example
"""

# socket for transmitting data
import socket

## Main Program Control ##
def main():
    connect_client()
    return 0


## End of Main ##

## Client Connect ##
def connect_client():
    # Create the client socket object (INET Type, TCP Stream)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server IP and Port to Connect to
    host = "192.168.1.5"
    port = 9000

    # Connect to the server
    client_socket.connect((host, port))

    # Receive up to 1024 bytes
    data_received = client_socket.recv(1024)

    # Close connection
    client_socket.close()

    # Print data received
    print("We got this from the server: %s" % data_received.decode("ascii"))

    return 0


## End of Client Connect ##

## Execute Main Program ##
if __name__ == "__main__":
    main()
