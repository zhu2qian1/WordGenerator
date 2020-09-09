import sys


class Constants:
    heb_path = r"./src/heb.json"
    porl_path = r"./src/porl.json"
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
            "w": ["voiced", "bilabial", "approximant"],
            "m": ["voiced", "bilabial", "nasal"],
            "n": ["voiced", "dental", "nasal"],
            "r": ["voiced", "dental", "trill"],
            "l": ["voiced", "dental", "lateral approximant"],
            "j": ["voiced", "palatal", "approximant"],
        },
        "parameters": {"absolute_open": False,},
        "phonetic_rules": {
            "min_vcluster": 1,
            "max_vcluster": 1,
            "min_ccluster": 1,
            "max_ccluster": 2,
        },
    }
