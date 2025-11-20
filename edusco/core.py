from typing import Dict, List
from difflib import SequenceMatcher
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .morphology import MorphologyAnalyzer
from .ontology import OntologyMatcher
from .extractor import Extractor
from .pronoun_resolver import PronounResolver
from .models import EduscoModel

class Edusco:
    """Edusco motoru: yazım düzeltme, anlamsal eşleşme, rubrik puanlama"""

    def __init__(self):
        self.spell = SpellingCorrector()
        self.tokenizer = Tokenizer()
        self.parser = POSParser()
        self.morph = MorphologyAnalyzer()
        self.ontology = OntologyMatcher()
        self.extractor = Extractor()
        self.pronoun_resolver = PronounResolver()

    def semantik_skor(self, student: str, model: str) -> float:
        model_cumleler = [c.strip() for c in model.split(",")]
        student_cumleler = [c.strip() for c in student.split(",")]
        skorlar = []
        for mc in model_cumleler:
            max_skor = max([SequenceMatcher(None, mc.lower(), sc.lower()).ratio() for sc in student_cumleler])
            skorlar.append(max_skor)
        return sum(skorlar) / len(skorlar) if skorlar else 0

    def değerlendir(self, model: EduscoModel, cevap: str) -> Dict:
        duzeltmis = self.spell.correct(cevap)
        tokens = self.tokenizer.tokenize(duzeltmis)
        tokens = self.pronoun_resolver.resolve(tokens)
        parsed = self.parser.parse(tokens)
        morph_tokens = [self.morph.analyze(t) for t in tokens]
        relations = self.extractor.extract(tokens)
        model_tokens = self.tokenizer.tokenize(" ".join(model.yanitlar))
        model_tokens_morph = [self.morph.analyze(t) for t in model_tokens]
        ortak = self.ontology.match(morph_tokens, model_tokens_morph)
        sem_score = self.semantik_skor(cevap, " ".join(model.yanitlar))
        skor = (len(ortak)/len(model_tokens) * 0.4 + sem_score * 0.6) if model_tokens else sem_score

        if skor >= 0.49:
            seviye, etiket = 4, "Tam Doğru"
        elif skor >= 0.35:
            seviye, etiket = 3, "Büyük Oranda Doğru"
        elif skor >= 0.25:
            seviye, etiket = 2, "Kısmen Doğru"
        elif skor >= 0.15:
            seviye, etiket = 1, "Yüzeysel Doğru"
        else:
            seviye, etiket = 0, "Yanlış"

        return {
            "duzeltmis": " ".join([t["text"] for t in morph_tokens]),
            "skor": round(skor, 2),
            "seviye": seviye,
            "etiket": etiket,
            "ortak_kelimeler": ortak,
            "relations": relations
        }
