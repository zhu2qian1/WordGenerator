class Language:
    """* requires a dictionary with keys named:
        consonants, vowels, phonetic_rules, and parameters.
    if any of them are missing, it will raise an exception."""

    def __init__(self, data):
        self.__data = data.copy()
        self.__consonants = data["consonants"].copy()
        self.__vowels = data["vowels"].copy()
        self.__phonetic_rules = data["phonetic_rules"].copy()
        self.__parameters = data["parameters"].copy()

    @property
    def data(self):
        return self.__data.copy()

    @property
    def consonants(self):
        return self.__consonants.copy()

    @property
    def vowels(self):
        return self.__vowels.copy()

    @property
    def phonetic_rules(self):
        return self.__phonetic_rules.copy()

    @property
    def parameters(self):
        return self.__parameters.copy()

    @property
    def vcluster_info(self):
        return (
            self.__phonetic_rules["min_vcluster"],
            self.__phonetic_rules["max_vcluster"],
        )

    @property
    def ccluster_info(self):
        return (
            self.__phonetic_rules["min_ccluster"],
            self.__phonetic_rules["max_ccluster"],
        )
