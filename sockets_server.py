#!/usr/bin/env python3
"""
Title: sockets_server.py
Description: Server socket example
"""

# sockets for connections
import socket

## Server Listen ##
def server_listen():
    # Create the server socket object (INET Type, TCP Stream)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define Server listening IP and Port
    host = "0.0.0.0"
    port = 9000

    # Bind to the port
    server_socket.bind((host, port))

    # Wait for client connection; queue up to 10 requests
    server_socket.listen(10)

    while True:
        # Accept client connections
        client_socket, address = server_socket.accept()
        print("Got connection from %s" % str(address))

        # Send data to client
        client_socket.send("Hello %s!" % str(address))

        # Close client connection
        client_socket.close()

    return 0


## End of Server Listen ##

## Main Program Control ##
def main():
    server_listen()
    return 0


## End of Main ##

## Execute Main Program ##
if __name__ == "__main__":
    main()
