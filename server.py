import os, socket, json, math, time


class server_socket:
    def __init__(self):
        config = json.load(open("./config.json"))
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.address = config["filepath"]
        print(self.address)

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
                        print("=== Request is :", request, "===")
                        # リクエストの処理とレスポンスの送信の処理をする。
                        response = server_method.controller(request.decode("utf-8"))
                        print("=== response is :", response, "===")
                        connection.sendall(response.encode())
                    finally:
                        break
            finally:
                print("Closing current connection")
                connection.close()


class server_method:
    def controller(data):
        print("=== Hello controller ===")
        received_Data = json.loads(data)
        function_Hashmap = {
            "floor": server_Function.floor,
            "nroot": server_Function.nroot,
            "reverse": server_Function.reverse,
            "validAnagram": server_Function.validAnagram,
            "sort": server_Function.sort,
        }
        method = received_Data["method"]
        params = received_Data["params"]
        params = server_Function.change_Type(method, params)
        id = received_Data["id"]
        if method in function_Hashmap:
            result = function_Hashmap[method](params)
            response_Data = {"results": result, "id": id}
        else:
            response_Data = {"results": "error method", "id": id}
        response_Data = json.dumps(response_Data)
        return response_Data


class server_Function:
    def floor(x):
        print("=== hello floor ===")
        return math.floor(x)

    def nroot(arr):
        print("=== hello nroot ===")
        x, n = arr
        return math.floor(x ** (1 / n))

    def reverse(s):
        print("=== hello reverse ===")
        return s[::-1]

    def validAnagram(arr):
        print("=== hello validAnagram ===")
        s1, s2 = arr
        return sorted(s1) == sorted(s2)

    def sort(arr):
        print("=== hello sort ===")
        return sorted(arr)

    def change_Type(method, params):
        print("=== hello change_Type ===")
        if method == "floor":
            return float(params)
        elif method == "nroot":
            return [int(x) for x in params]
        elif method == "reverse":
            return str(params)
        elif method == "validAnagram":
            return [str(s) for s in params]
        else:
            return str(params)


def main():
    sock = server_socket()
    sock.startSock()


if __name__ == "__main__":
    main()
