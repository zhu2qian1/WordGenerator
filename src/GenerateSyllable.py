try:
    from .Language import Language
    from .PhoneticArray import PhoneticArray as pa
except ImportError as e:
    print(f"caution: {e}")
    from Language import Language
    from PhoneticArray import PhoneticArray as pa


class GenerateSyllable:
    """an function that generates a syllable.
    
    音節を生成する関数です．"""

    def __init__(self, lang):
        assert isinstance(lang, Language)
        self.lang = lang

    def random_auto(self) -> str:
        """generate a syllable randomly.
        
        ランダムに音節を生成します．"""
        from random import choices
        from random import randint as rint

        vmin, vmax = self.lang.vcluster_info
        cmin, cmax = self.lang.ccluster_info
        v, c = list(self.lang.vowels), list(self.lang.consonants)

        onset = "".join(choices(c, k=rint(cmin, cmax))[:])
        necleus = "".join(choices(v, k=rint(vmin, vmax))[:])
        coda = "".join(choices(c, k=rint(cmin, cmax))[:])

        return onset + necleus + coda

    def phonetic_array(self, mode="r") -> dict:
        """returns a phonetic array with information. refer to ./src/PhoneticArray.py.
        
        音配列を情報付きで返します．詳細は PhoneticArray を参照してください．"""
        from collections import OrderedDict as odict

        if mode == "r":
            dct = odict()
            s = self.random_auto()
            for i in s:
                try:
                    dct[i] = self.lang.consonants[i]
                except KeyError:
                    dct[i] = self.lang.vowels[i]
        return pa(dct)
