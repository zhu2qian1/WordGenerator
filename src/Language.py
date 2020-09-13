from random import choices
from random import randint


class Language:
    """* requires a dictionary with keys named:
        consonants, vowels, phonetic_rules, and parameters.
    if any of them are missing, it will raise KeyNotFoundError.

    consonants, vowels, phonetic_rules, parameters のキーを持つ辞書が必要です．
    これらのキーが一つでも欠けている場合，KeyNotFoundErrorを送出します．"""

    def __init__(self, data):
        self.__data = data
        self.__consonants = data["consonants"]
        self.__vowels = data["vowels"]
        self.__phonetic_rules = data["phonetic_rules"]
        self.__parameters = data["parameters"]

    @property
    def data(self):
        """the given dict itself.

        受け取った辞書です．"""
        return self.__data

    @property
    def consonants(self):
        """the consonants contained in the given dictionary.

        受け取った辞書の子音です．"""
        return self.__consonants

    @property
    def vowels(self):
        """the vowels contained in the given dictionary.

        受け取った辞書の母音です．"""
        return self.__vowels

    @property
    def phonetic_rules(self):
        """the phonetic rules in the given dictionary.

        受け取った辞書の音韻規則です．"""
        return self.__phonetic_rules

    @property
    def parameters(self):
        """the parameters in the given dictionary.

        受け取った辞書のパラメターです．"""
        return self.__parameters

    @property
    def vcluster_info(self) -> tuple:
        """the information for vowel cluster.
        returns a tuple of (min_size, max_size)."""
        return (
            self.__phonetic_rules["min_vcluster"],
            self.__phonetic_rules["max_vcluster"],
        )

    @property
    def ccluster_info(self) -> tuple:
        """the information for consonant cluster.
        returns a tuple of (min_size, max_size)."""
        return (
            self.__phonetic_rules["min_ccluster"],
            self.__phonetic_rules["max_ccluster"],
        )

    @property
    def c_symbols(self) -> list:
        s = set()
        for x in self.__consonants.keys():
            for y in x:
                s.add(y)
        return list(s)

    @property
    def c_features(self) -> list:
        s = set()
        for x in self.__consonants.values():
            for y in x:
                s.add(y)
        return list(s)

    @property
    def v_symbols(self) -> list:
        s = set()
        for x in self.__vowels.keys():
            for y in x:
                s.add(y)
        return list(s)

    @property
    def v_features(self) -> list:
        s = set()
        for x in self.__vowels.values():
            for y in x:
                s.add(y)
        return list(s)

    def generate_syllable(self):
        vmin, vmax = self.vcluster_info
        cmin, cmax = self.ccluster_info
        v, c = self.v_symbols, self.c_symbols

        onset = "".join(choices(c, k=randint(cmin, cmax))[:])
        necleus = "".join(choices(v, k=randint(vmin, vmax))[:])
        coda = "".join(choices(c, k=randint(cmin, cmax))[:])

        return onset + necleus + coda
