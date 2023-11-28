import os
import socket
import server_method


class server_socket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.address = "/tmp/socket_file"
        self.__startSock()

    def __startSock(self):
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
                        response = server_method(request.decode())
                        self.sock.sendall(response)
                    finally:
                        break
            finally:
                print("Closing current connection")
                connection.close()
