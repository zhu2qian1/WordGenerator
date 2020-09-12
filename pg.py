from src.Paths import porl_path
from src.JsonTools import JsonTools as jt
from src.Language import Language as lang
from src.GenerateSyllable import GenerateSyllable as gs

porl = lang(jt.load(porl_path))
pgentor = gs(porl)
ls = []
for i in range(16):
    ls.append(pgentor.phonetic_array())
lswrittens = [i.written for i in ls]
