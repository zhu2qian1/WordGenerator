from typing import OrderedDict as OrderedDictType


class PhoneticArray:
    def __init__(self, pa: OrderedDictType):
        self.__pa = pa

    def __repr__(self):
        return repr(self.__pa)

    @property
    def written(self) -> str:
        return str("".join(self.__pa.keys()))

    @property
    def features(self) -> list:
        return [i for i in [j for j in list(self.__pa.values())]]

