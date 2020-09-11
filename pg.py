from src.Paths import porl_path
from src.JsonTools import JsonTools as jt
from src.Language import Language as lang
from src.GenerateSyllable import GenerateSyllable as gs

porl = lang(jt.load(porl_path))
