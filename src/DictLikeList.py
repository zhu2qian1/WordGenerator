class DictLikeList:
    def __init__(self, arg) -> object:
        if type(arg) == dict:
            self.__keys = list(arg.keys())
            self.__values = list(arg.values())
        elif type(arg) == list or tuple:
            self.__keys = arg[0]
            self.__values = arg[1]

    def __repr__(self) -> str:
        return repr([self.__keys, self.__values])

    @property
    def keys(self) -> list:
        return self.__keys

    @property
    def values(self) -> list:
        return self.__values

    def add(self, key, value) -> None:
        assert type(key) is str
        self.__keys.append(key)
        self.__values.append(value)


dll = DictLikeList
a = ["a", "b"]
b = [1, 2]
c = {"c": 3, "d": 4}
