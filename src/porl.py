porl_data = {
    "vowels": {
        "a": ["low", "center", "unrounded", "short"],
        "aa": ["low", "center", "unrounded", "long"],
        "e": ["mid", "front", "unrounded", "short"],
        "i": ["high", "front", "unrounded", "short"],
        "ii": ["high", "front", "unrounded", "long"],
        "o": ["mid", "back", "rounded", "short"],
        "u": ["high", "back", "rounded", "short"],
        "uu": ["high", "back", "rounded", "long"],
    },
    "consonants": {
        "": [None],
        "p": ["voiceless", "bilabial", "plosive"],
        "t": ["voiceless", "dental", "plosive"],
        "s": ["voiceless", "dental", "fricative"],
        "k": ["voiceless", "velar", "plosive"],
        "h": ["voiceless", "glottal", "fricative"],
        "b": ["voiced", "bilabial", "plosive"],
        "w": ["voiced", "bilabial", "approximant"],
        "m": ["voiced", "bilabial", "nasal"],
        "d": ["voiced", "dental", "plosive"],
        "n": ["voiced", "dental", "nasal"],
        "r": ["voiced", "dental", "trill"],
        "l": ["voiced", "dental", "lateral approximant"],
        "j": ["voiced", "palatal", "approximant"],
        "g": ["voiced", "velar", "plosive"],
    },
    "parameters": {"absolute_open": False,},
    "phonetic_rules": {
        "min_vcluster": 1,
        "max_vcluster": 1,
        "min_ccluster": 1,
        "max_ccluster": 2,
    },
}
if __name__ == "__main__":
    try:
        from Paths import porl_path
        from JsonTools import JsonTools
    except ImportError:
        from .Paths import porl_path
        from .JsonTools import JsonTools
    finally:
        from sys import argv

        save = JsonTools.save
        dest = porl_path
        obj = porl_data
        if "-save" in argv[:]:
            save(dest=dest, obj=obj)
            print(f"saved an object to dest ({dest})")
        else:
            print("not saved; you can save by putting -save when run this file")
