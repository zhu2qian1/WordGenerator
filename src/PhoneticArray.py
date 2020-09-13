from typing import OrderedDict as OrderedDictType


class PhoneticArray:
    def __init__(self, phonetic_array: OrderedDictType):
        self.__phonetic_array = phonetic_array

    def __repr__(self):
        return repr(self.__phonetic_array)

    @property
    def written(self) -> str:
        return str("".join(self.__phonetic_array.keys()))

    @property
    def features(self) -> list:
        return [i for i in [j for j in list(self.__phonetic_array.values())]]

    @property
    def chart(self) -> list:
        return [self.__phonetic_array.keys(), self.__phonetic_array.values()]
