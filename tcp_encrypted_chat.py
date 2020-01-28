#!/usr/bin/env python3

import socket
import sys

CONNECTION_BUFFER_SIZE = 1024000000  # 1024 MB


def parseArguments():
    argumentLength = len(sys.argv)
    if argumentLength < 5:
        print("Correct syntax: "
              + sys.argv[0]
              + " <host_name_to_chat_with>"
              + " <port_to_chat_on>"
              + " <file_to_read_DES_key_from"
              + " <client | server>")
        return None

    arguments = []
    arguments.append(str(sys.argv[1]))
    arguments.append(int(sys.argv[2]))
    arguments.append(str(sys.argv[3]))
    arguments.append(str(sys.argv[4]))

    return arguments


def getDESKeyFromFile(filename):
    DES_key = None
    with open(filename, "r") as key_file:
        DES_key = key_file.readline().strip("\r\n")

    print("The shared DES Key is: " + DES_key)
    return DES_key


def startTCPEncryptedChat(host, port, DES_key, clientserver):
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    # "Client" Side
    if clientserver == "client":
        socket_.connect(server_address)

        while True:
            print("Waiting to receive message..")
            received = socket_.recv(CONNECTION_BUFFER_SIZE)
            received = received.decode("utf-8").strip("\r\n")
            # TODO: print(ciphertext)
            # TODO: decrypt with DES_key
            # TODO: print(plaintext)

            message = input("Message to send: ").strip("\r\n")
            # TODO: print(plaintext)
            # TODO: encrypt with DES_key
            # TODO: print(ciphertext)
            socket_.send(bytearray(message, "utf-8"))

    # "Server" side
    else:
        socket_.bind(server_address)
        socket_.listen()
        connection, client_address = socket_.accept()

        while True:
            message = input("Message to send: ").strip("\r\n")
            # TODO: print(plaintext)
            # TODO: encrypt with DES_key
            # TODO: print(ciphertext)
            connection.send(bytearray(message, "utf-8"))

            print("Waiting to receive message..")
            received = connection.recv(CONNECTION_BUFFER_SIZE)
            received = received.decode("utf-8").strip("\r\n")
            # TODO: print(ciphertext)
            # TODO: decrypt with DES_key
            # TODO: print(plaintext)

    return


# This function will start a new TCP socket if none exists
# and will join an existing one if it does exist on a given port
def main():
    args = parseArguments()
    if args is None:
        return

    DES_key = getDESKeyFromFile(args[2])

    startTCPEncryptedChat(args[0], args[1], DES_key, args[3])
    return


# This snippet of code verifies that this file was called through the command
# line and not through another python file. (reduces unnecessary errors)
if __name__ == "__main__":
    main()
