from JsonTools import JsonTools as jt
import sys


class Constants:
    path_heb = r"./src/heb.json"
    path_porl = r"./src/porl.json"
    porl_data = {
        "vowels": {
            "a": ["low", "center", "unrounded", "short"],
            "e": ["mid", "front", "unrounded", "short"],
            "i": ["high", "front", "unrounded", "short"],
            "o": ["mid", "back", "rounded", "short"],
            "u": ["high", "back", "rounded", "short"],
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
        "parameters": {},
        "phonetic_rules": {
            "min_vcluster": 1,
            "max_vcluster": 1,
            "min_ccluster": 1,
            "max_ccluster": 2,
        },
    }


if __name__ == "__main__":
    try:
        if sys.argv[1] == "save":
            jt.save(Constants.path_porl, Constants.porl_data)
    except IndexError:
        pass
