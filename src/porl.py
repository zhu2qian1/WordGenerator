porl_data = {
    "vowels": {
        "a": ["vowel", "low", "center", "unrounded", "short"],
        "ā": ["vowel", "low", "center", "unrounded", "long"],
        "e": ["vowel", "mid", "front", "unrounded", "short"],
        "i": ["vowel", "high", "front", "unrounded", "short"],
        "ī": ["vowel", "high", "front", "unrounded", "long"],
        "o": ["vowel", "mid", "back", "rounded", "short"],
        "u": ["vowel", "high", "back", "rounded", "short"],
        "ū": ["vowel", "high", "back", "rounded", "long"],
    },
    "consonants": {
        "’": ["consonant", "voiceless", "glottal", "plosive"],
        "p": ["consonant", "voiceless", "bilabial", "plosive"],
        "t": ["consonant", "voiceless", "dental", "plosive"],
        "s": ["consonant", "voiceless", "dental", "fricative"],
        "k": ["consonant", "voiceless", "velar", "plosive"],
        "h": ["consonant", "voiceless", "glottal", "fricative"],
        "b": ["consonant", "voiced", "bilabial", "plosive"],
        "w": ["consonant", "voiced", "bilabial", "approximant"],
        "m": ["consonant", "voiced", "bilabial", "nasal"],
        "d": ["consonant", "voiced", "dental", "plosive"],
        "n": ["consonant", "voiced", "dental", "nasal"],
        "r": ["consonant", "voiced", "dental", "trill"],
        "l": ["consonant", "voiced", "dental", "lateral approximant"],
        "j": ["consonant", "voiced", "palatal", "approximant"],
        "g": ["consonant", "voiced", "velar", "plosive"],
    },
    "parameters": [{"Null_onset": False}, {"Null_coda": False}],
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
    except ImportError as e:
        from .Paths import porl_path
        from .JsonTools import JsonTools

        print(f"Caution {e}: could not load from Paths:")
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
