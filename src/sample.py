sample_data = {
    "consonants": {
        "p": [1, "consonant", "voiceless", "bilabial", "plosive"],
        "t": [1, "consonant", "voiceless", "dental", "plosive"],
        "k": [1, "consonant", "voiceless", "velar", "plosive"],
    },
    "vowels": {
        "a": [1, "vowel", "low", "center", "unrounded"],
        "i": [1, "vowel", "high", "front", "unrounded"],
        "u": [1, "vowel", "high", "back", "rounded"],
    },
    "phonetic_rules": {"vcluster": [1, 1], "ccluster": [1, 2],},
    "parameters": {"null_onset": True, "null_coda": True},
}

if __name__ == "__main__":
    try:
        from Paths import sample_path
        from JsonTools import JsonTools
    except ImportError as e:
        from .Paths import sample_path
        from .JsonTools import JsonTools

        print(f"Caution {e}: could not load from Paths:")
    finally:
        from sys import argv

        save = JsonTools.save
        dest = sample_path
        obj = sample_data
        if "-save" in argv[:]:
            save(dest=dest, obj=obj)
            print(f"saved an object to dest ({dest})")
        else:
            print("not saved; you can save by putting -save when run this file")
