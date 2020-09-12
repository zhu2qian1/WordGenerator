class Language:
    """* requires a dictionary with keys named:
        consonants, vowels, phonetic_rules, and parameters.
    if any of them are missing, it will raise KeyNotFoundError.
    
    consonants, vowels, phonetic_rules, parameters のキーを持つ辞書が必要です．
    これらのキーが一つでも欠けている場合，KeyNotFoundErrorを送出します．"""

    def __init__(self, data):
        self.__data = data.copy()
        self.__consonants = data["consonants"].copy()
        self.__vowels = data["vowels"].copy()
        self.__phonetic_rules = data["phonetic_rules"].copy()
        self.__parameters = data["parameters"].copy()

    @property
    def data(self):
        """the given dict itself.
        
        受け取った辞書です．"""
        return self.__data.copy()

    @property
    def consonants(self):
        """the consonants contained in the given dictionary.
        
        受け取った辞書の子音です．"""
        return self.__consonants.copy()

    @property
    def vowels(self):
        """the vowels contained in the given dictionary.
        
        受け取った辞書の母音です．"""
        return self.__vowels.copy()

    @property
    def phonetic_rules(self):
        """the phonetic rules in the given dictionary.
        
        受け取った辞書の音韻規則です．"""
        return self.__phonetic_rules.copy()

    @property
    def parameters(self):
        """the parameters in the given dictionary.
        
        受け取った辞書のパラメターです．"""
        return self.__parameters.copy()

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

