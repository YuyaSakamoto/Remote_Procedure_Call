from servlet.server_socket import server_socket


def main():
    sock = server_socket()
    sock.startSock()


if __name__ == "__main__":
    main()
