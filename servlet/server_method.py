import json
import math


# 対応したメソッドを処理した後にencode()して返す
class server_method:
    def __init__(self, data):
        request = json.loads(data)
        self.method = request["method"]
        self.params = request["params"]
        self.param_types = request["param_types"]
        self.id = request["id"]
        print("request is :", request)

    def unpack(self):
        self.methods = {
            "floor": self.floor(),
            "nroot": self.nroot(),
            "reverse": self.reverse(),
            "validAnagram": self.validAnagram(),
            "sort": self.sort(),
        }
        if self.method not in self.methods:
            err = json.dumps({"err": "different method"})
            # type(byte) & responseとして返す
            return err.encode()
        else:
            print("ok unpack")
            return self.methods[self.method]

    def floor(self):
        if self.param_types == ["double"]:
            res = json.dumps(
                {"results": math.floor(self.params), "result_types": "int", "id": 1}
            )
            print("ok floor")
            print(res)
            return res
        err = json.dumps({"err": "different param_types"})
        return err

    def nroot(self):
        if self.param_types != ["int", "int"]:
            err = json.dumps({"err": "different param_types"})
            return err
        print("ok nroot")
        res = json.dumps(
            {
                "results": pow(self.params[1], 1 / self.params[0]),
                "result_types": "float",
                "id": 1,
            }
        )

        return res

    def reverse(self):
        if self.param_types != ["string"]:
            err = json.dumps({"err": "different param_types"})
            return err.encode()
        res = json.dumps(
            {
                "results": self.params[0][::-1],
                "result_types": "string",
                "id": 1,
            }
        )
        return res.encode()

    def validAnagram(self):
        if self.param_types != ["string", "string"]:
            err = json.dumps({"err": "different param_types"})
            return err
        isAnagram = sorted(self.params[0]) == sorted(self.params[1])
        res = json.dumps(
            {
                "results": isAnagram,
                "result_types": "boolean",
                "id": 1,
            }
        )
        return res

    def sort(self):
        if self.param_types != ["strArr"]:
            err = json.dumps({"err": "different param_types"})
            return err
        res = json.dumps(
            {
                "results": sorted(self.params),
                "result_types": "strArr",
                "id": 1,
            }
        )
        return res
