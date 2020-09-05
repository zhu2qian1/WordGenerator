from src.Language import Language as lang


class GenerateSyllable:
    def __init__(self, data: dict) -> object:
        self.__data = data.deepcopy()
