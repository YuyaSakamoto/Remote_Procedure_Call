import os
import socket
from servlet.server_method import server_method
import json


class server_socket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.address = "/tmp/socket_file"

    def startSock(self):
        try:
            os.unlink(self.address)
        except FileNotFoundError:
            pass

        print("Starting up on {}".format(self.address))
        self.sock.bind(self.address)
        self.sock.listen(1)

        while True:
            connection, client_address = self.sock.accept()

            try:
                print("connection from", client_address)

                while True:
                    try:
                        request = connection.recv(4096)
                        ("Received", request)
                        # リクエストの処理とレスポンスの送信の処理をする。
                        response = server_method(request.decode()).unpack()
                        print("response is:", response)
                        connection.sendall(response.encode())
                    finally:
                        break
            finally:
                print("Closing current connection")
                connection.close()
