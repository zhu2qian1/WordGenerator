try:
    from .Language import Language
except ImportError:
    from Language import Language


class GenerateSyllable:
    def __init__(self, lang):
        assert isinstance(lang, Language)
        self.lang = lang

    def random_auto(self):
        from random import choices
        from random import randint as rint

        vmin, vmax = self.lang.vcluster_info
        cmin, cmax = self.lang.ccluster_info
        v, c = list(self.lang.vowels), list(self.lang.consonants)

        onset = "".join(choices(c, k=rint(cmin, cmax))[:])
        necleus = "".join(choices(v, k=rint(vmin, vmax))[:])
        coda = "".join(choices(c, k=rint(cmin, cmax))[:])

        return onset + necleus + coda
