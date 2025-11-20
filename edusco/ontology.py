from typing import List, Dict

EQUIVALENCES = {
    "arttırmak": ["çoğaltmak", "yükseltmek", "artırmak", "geliştirmek"],
    "üretmek": ["oluşturmak", "yapmak", "üretilmek", "hazırlamak", "elde etmek"],
    "güneş": ["ışık", "güneş ışığı", "güneşten enerji", "güneş enerjisi"],
    "bitki": ["bitkiler", "yeşil bitkiler", "çiçek", "ağaç", "ot"],
    "glikoz": ["şeker", "karbonhidrat", "besin", "enerji kaynağı"],
    "oksijen": ["o2", "hava", "solunabilir gaz", "atmosfer gazı"],
    "fotosentez": ["fotosentez olayı","ışık enerjisi ile besin üretimi","şeker üretimi"]
}

class OntologyMatcher:
    def match(self, cevap_tokens: List[Dict], model_tokens: List[Dict]) -> List[str]:
        cevap_set = set([t["root"] for t in cevap_tokens])
        model_set = set([t["root"] for t in model_tokens])
        ortak = []
        for m in model_set:
            if m in cevap_set:
                ortak.append(m)
            elif m in EQUIVALENCES:
                for eq in EQUIVALENCES[m]:
                    if eq in cevap_set:
                        ortak.append(m)
        return ortak
