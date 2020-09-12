from typing import OrderedDict as OrderedDictType


class PhoneticArray:
    def __init__(self, pa: OrderedDictType):
        self.__pa = pa

    @property
    def written(self) -> str:
        return str("".join(self.__pa.keys()))

    @property
    def dictrepr(self) -> OrderedDictType:
        return self.__pa

    @property
    def feature_arr(self) -> list:
        return [i for i in [j for j in list(self.__pa.values())]]
