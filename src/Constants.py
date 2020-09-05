class Constants:
    lang_heb = r"./src/heb.json"
    lang_porl = r"./src/porl.json"
    porl = {
        "vowels": {
            "a": ["low", "center", "unrounded"],
            "e": ["mid", "front", "unrounded"],
            "i": ["high", "front", "unrounded"],
            "o": ["mid", "back", "rounded"],
            "u": ["high", "back", "rounded"],
        },
        "consonants": {
            "": [None],
            "p": ["voiceless", "bilabial", "plosive"],
            "t": ["voiceless", "dental", "plosive"],
            "k": ["voiceless", "velar", "plosive"],
            "r": ["voiced", "dental", "trill"],
            "l": ["voiced", "dental", "lateral approximant"],
        },
        "parameters": {},
        "phonetic_rules": {
            "min_vcluster": 1,
            "max_vcluster": 1,
            "min_ccluster": 1,
            "max_ccluster": 2,
        },
    }
