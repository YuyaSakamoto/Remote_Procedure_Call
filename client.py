import socket
import sys
import json

config = json.load(open("config.json"))
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = config["filepath"]

try:
    print("accept connect")
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit()

try:
    request = json.dumps(
        {"method": "nroot", "params": [10, 100], "param_types": ["int", "int"], "id": 1}
    )
    print("Request is :", request)
    sock.sendall(request.encode())

    sock.settimeout(2)

    try:
        while True:
            response = sock.recv(4096)
            if response:
                print("Response is :", response)
            else:
                break

    except TimeoutError:
        print("Socket timeout")

finally:
    print("closing socket")
    sock.close()
