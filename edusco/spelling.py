from spellchecker import SpellChecker

class SpellingCorrector:
    def __init__(self):
        self.spell = SpellChecker(language="tr")

    def correct(self, text: str) -> str:
        kelimeler = text.strip().lower().split()
        duzeltilmis = []
        for k in kelimeler:
            c = self.spell.correction(k)
            duzeltilmis.append(c if c else k)
        return " ".join(duzeltilmis)
