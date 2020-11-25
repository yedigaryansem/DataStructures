class Map:
    def __init__(self):
        self.__psina = []

    def put(self, key, value):
        self.__psina.append([key, value])

    def get(self, key):
        for i in range(0, len(self.__psina)):
            if self.__psina[i][0] == key:
                return self.__psina[i][1]
        return None

    def pop(self, key):
        for i in range(0, len(self.__psina)):
            if self.__psina[i][0] == key:
                self.__psina.pop(i)
                break

    def size(self):
        return len(self.__psina)

    def has_key(self, key):
        for i in range(0, len(self.__psina)):
            if self.__psina[i][0] == key:
                return True
        return False


""""checks for methods"""
# m = Map()
# assert m.size() == 0
# m.put("b", 8)
# m.put("k", "t")
# assert m.size() == 2
# assert m.has_key("b") is True
# assert m.has_key("k") is False
# assert m.get("b") == 8
# assert m.get("k") == "t"
# m.pop("b")
# assert m.size() == 1
# assert m.has_key("b") is False
# assert m.has_key("k") is True
# m.put("nonekey", None)
# assert m.get("nonekey") is None
# assert m.size() == 2
#
# exit()
# m = {
#     "q": 1,
#     "c": None,
# }
#
# print(m["q"])
# print(m["c"])
#
# m["a"] = 9000
# print(m["a"])
# m["a"] = None
# print(m["a"])
# print("before pop: ", "a" in m)
# m.pop("a")
# print("after pop: ", "a" in m)
# print(m["a"])
